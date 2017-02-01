init -1500 python:
    # Import the Encyclopaedia
    from encyclopaedia import Encyclopaedia
    from encyclopaedia import EncEntry


################################################################################
# Entry Button
#
# Sub-screen to determine what sort of button to show for an entry.
# Used by the Vertical List sub-screen.
#
# Args:
#   enc (Encyclopaedia): The encyclopaedia to use on this screen.
#   entry (EncEntry): The entry to associate with the button.
################################################################################
screen entry_button(enc, entry):
    if enc.show_locked_buttons:
        # If the entry is unlocked, add an active button.
        if entry.locked is False:
            textbutton entry.name action enc.SetEntry(entry) style "encyclopaedia_entry_button"

            if not entry.viewed:
                text enc.labels.unread_entry_label

        # If the entry is locked, add a button depending on what should be shown.
        else:
            if enc.show_locked_entry:
                textbutton enc.labels.locked_entry_label action enc.SetEntry(entry) style "encyclopaedia_entry_button"
            else:
                textbutton enc.labels.locked_entry_label style "encyclopaedia_entry_button"

    elif enc.show_locked_buttons is False:
        textbutton entry.name action enc.SetEntry(entry) style "encyclopaedia_entry_button"

        # Add tag next to the button, if it hasn't been viewed yet.
        if not entry.viewed:
            text enc.labels.unread_entry_label

################################################################################
# Vertical List
#
# Sub-screen that displays a vertical list of entry buttons.
# Used by the Encyclopaedia List screen.
#
# Args:
#   enc (Encyclopaedia): The encyclopaedia to use on this screen.
################################################################################
screen vertical_list(enc):
    # The list used is chosen based on if we want to show locked entries on
    #   the entry select screen or not.

    if enc.sorting_mode == enc.SORT_SUBJECT:
        # Split entries by subject
        for key, group in groupby(enc.current_entries, attrgetter("subject")):
           text key  # The subject heading
           for entry in group:
               hbox:
                   use entry_button(enc, entry)

    elif enc.sorting_mode == enc.SORT_NUMBER:
        for entry in enc.current_entries:
            hbox:
                spacing 10
                text "{:02}".format(entry.number)
                use entry_button(enc, entry)

    # If sorting Alphabetically, Reverse-Alphabetically, or by Unread.
    else:
        if enc.nest_alphabetical_sort:
            # Split entries by first letter
            for key, group in groupby(enc.current_entries, key=lambda x: x.name[0]):
                text key  # The letter heading
                for entry in group:
                    hbox:
                        use entry_button(enc, entry)

        else:
            for entry in enc.current_entries:
                hbox:
                    use entry_button(enc, entry)

################################################################################
# Encyclopaedia List
#
# Screen that's used to display the list of entries.
# Args:
#   enc (Encyclopaedia): The encyclopaedia to use on this screen.
################################################################################
screen encyclopaedia_list(enc):
    tag menu
    modal True

    window:
        style_prefix "encyclopaedia"

        vbox:
            spacing 10
  
            frame:
                style_prefix "encyclopaedia"
                xfill True

                text "Welcome to the Demo Encyclopaedia"
    
            frame:
                style_prefix "encyclopaedia"
                xfill True
    
                hbox:
                    xfill True
                    # Percentage unlocked display
                    text "{} Complete".format(enc.labels.percentage_unlocked)

            frame:
                style_prefix "encyclopaedia"
                xfill True

                vbox:
                    text "Filters"
                    hbox:
                        xfill True
                        # Percentage unlocked display
                        textbutton "All" action enc.ClearFilter() style "encyclopaedia_button"
                        for subject in enc.subjects:
                            textbutton subject action enc.FilterBySubject(subject) style "encyclopaedia_button"

            hbox:
                frame:
                    style_prefix "encyclopaedia"
                    yfill True
                    xmaximum 600
                    bottom_margin 10

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        vbox:
                            # Flavour text to display the current sorting mode.
                            text enc.labels.sorting_mode xalign 0.5

                            use vertical_list(enc) id "vertical list"

                frame:
                    style_prefix "encyclopaedia"
                    xfill True
                    bottom_margin 10
                    yalign 0.95

                    vbox:
                        # Buttons to sort entries.
                        textbutton "Sort by %s" % enc.labels.sort_number_label action enc.Sort(sorting_mode=enc.SORT_NUMBER) style "encyclopaedia_button" xfill True
                        textbutton "Sort by %s" % enc.labels.sort_alphabetical_label action enc.Sort(sorting_mode=enc.SORT_ALPHABETICAL) style "encyclopaedia_button" xfill True
                        textbutton "Sort by %s" % enc.labels.sort_reverse_alphabetical_label action enc.Sort(sorting_mode=enc.SORT_REVERSE_ALPHABETICAL) style "encyclopaedia_button" xfill True
                        textbutton "Sort by %s" % enc.labels.sort_subject_label action enc.Sort(sorting_mode=enc.SORT_SUBJECT) style "encyclopaedia_button" xfill True
                        textbutton "Sort by %s" % enc.labels.sort_unread_label action enc.Sort(sorting_mode=enc.SORT_UNREAD) style "encyclopaedia_button" xfill True

                        # Buttons to show different styles of hiding locked data.
                        textbutton "Show/Hide Locked Buttons" action enc.ToggleShowLockedButtons() style "encyclopaedia_button" xfill True
                        textbutton "Show/Hide Locked Entry" action enc.ToggleShowLockedEntry() style "encyclopaedia_button" xfill True

                        # Sort and SaveStatus are unnecessary if you're not using persistent data (ie: if the encyclopaedia is save game independent)
                        # Sorting mode has to be by Number to save properly. "new_0" should be whatever the prefix you choose for the persistent dictionary is.
                        textbutton "Return"  action [enc.Sort(sorting_mode=enc.default_sorting_mode),
                                                     enc.SaveStatus(persistent.new_status, "new"),
                                                     Hide("encyclopaedia_list"),
                                                     Return()] style "encyclopaedia_button" xfill True

################################################################################
# Encyclopaedia Entry
#
# Screen that's used to display an individual entry.
# Args:
#   enc (Encyclopaedia): The encyclopaedia to use on this screen.
################################################################################
screen encyclopaedia_entry(enc):
    tag menu
    modal True

    window:
        style_prefix "encyclopaedia"

        vbox:
            spacing 10
  
            frame:
                style_prefix "encyclopaedia"
                xfill True
                # Flavour text to indicate which entry we're currently on
                text enc.active.label
  
            frame:
                style_prefix "encyclopaedia"
                id "entry_nav"
                xfill True
                hbox:
                    xfill True
                    # Previous / Next is relative to the sorting mode
                    textbutton "Previous Entry" xalign .02 action enc.PreviousEntry() style "encyclopaedia_button"
                    textbutton "Next Entry" xalign .98 action enc.NextEntry() style "encyclopaedia_button"
       
            hbox:
                # If the entry or sub-entry has an image
                if enc.active.current_page.has_image:
                    frame:
                        style_prefix "encyclopaedia"
                        yfill True
                        xfill True

                        xmaximum img_screen_width
                        ymaximum img_screen_height
                        
                        $current_image = enc.active.current_page.image
                        add current_image crop (0,10,img_screen_width-33,img_screen_height-25)

#                        viewport:
#                            scrollbars False
#                            draggable True
#                            mousewheel True
#                            edgescroll (1.0, 1.0)
#                            add enc.active.current_page.image
   
                    frame:
                        style_prefix "encyclopaedia"
                        id "entry_window"
                        xfill True
                        yfill True
                        xmaximum img_text_width
                        ymaximum half_screen_height
                        viewport:
                            scrollbars "vertical"
                            mousewheel True  
                            draggable True
                            xfill True
                            yfill True  
                            vbox:
                                spacing 15
                                # Display the current entry's text
                                for item in enc.active.current_page.text:
                                    text item

                # If there's no image                        
                else:
                    frame:
                        style_prefix "encyclopaedia"
                        id "entry_window"
                        xfill True
                        yfill True
                        xmaximum config.screen_width
                        ymaximum half_screen_height
                        viewport:
                            scrollbars "vertical"
                            mousewheel True  
                            draggable True
                            xfill True
                            yfill True  
                            vbox:
                                spacing 15
                                # Display the current entry's text
                                for item in enc.active.current_page.text:
                                    text item

            frame:
                style_prefix "encyclopaedia"
                xfill True
                yfill False

                if enc.active.has_sub_entry:
                    hbox:
                        xfill True

                        # If there's a sub-entry, add Prev/Next Page buttons
                        textbutton "Previous Page" xalign .02 action enc.PreviousPage() style "encyclopaedia_button"

                        # Flavour text to indicate which sub-page out of the total is being viewed
                        text enc.labels.entry_current_page

                        textbutton "Next Page" xalign .98 action enc.NextPage() style "encyclopaedia_button"

                else:
                    xpadding 10
                    ypadding 14
                    text " "

        frame:
            style_prefix "encyclopaedia"
            xfill True

            yalign .98
            hbox:
                xfill True
                # Flavour text that displays the current sorting mode
                text "Sorting Mode: {}".format(enc.labels.sorting_mode)
                textbutton "Close Entry" id "close_entry_button" xalign .98 clicked [enc.ResetSubPage(), Show("encyclopaedia_list", None, enc)] style "encyclopaedia_button"


########################
# Encyclopaedia Styles
########################
style encyclopaedia_window is default:
    background color_enc_bg
    xsize config.screen_width
    ysize config.screen_height
    xfill True
    yfill True

style encyclopaedia_frame is default:
    background color_enc_frame
    size 16
    padding (8, 8)
    xmargin 8
    top_margin 8

style encyclopaedia_scrollbar is scrollbar:
    base_bar Frame(Solid(color_scroll_empty), gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid(color_scroll_bar), gui.scrollbar_borders, tile=gui.scrollbar_tile)

style encyclopaedia_vscrollbar is vscrollbar:
    base_bar Frame(Solid(color_scroll_empty), gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid(color_scroll_bar), gui.scrollbar_borders, tile=gui.scrollbar_tile)

style encyclopaedia_button:
    background color_enc_button
    hover_background color_scroll_bar
    insensitive_background color_alt_frame

style encyclopaedia_button_text:
    color color_hover_text
    idle_color color_enc_text
    insensitive_color color_alt_text

style encyclopaedia_entry_button is encyclopaedia_button:
    xfill True

style encyclopaedia_entry_button_text is encyclopaedia_button_text


############################
# Encyclopaedia Misc Setup
############################
init -1500:
    python:
        from itertools import groupby
        from operator import attrgetter

        half_screen_width = config.screen_width / 2
        half_screen_height = config.screen_height / 2
        img_screen_width = config.screen_width / 1.46
        img_screen_height = config.screen_height / 1.575
        img_text_width = config.screen_width / 3
        img_text_height = config.screen_height / 1.575 #For some reason, this can only be an integer or it breaks

        # Encyclopaedia Colours
        color_scroll_bar = "#003C78"
        color_scroll_empty = "#DCEBFF"
        color_alt_frame = "#DCEBFF"

        color_enc_bg = "#DCEBFF"
        color_enc_frame = "#6496C8"
        color_enc_button = "#003C78"

        color_alt_text = "#003C78"
        color_enc_text = "#C8FFFF"

        color_hover_text = "#FFFFFF"


###############################################################################
## Encyclopaedia Button
## Contains a button to open the encyclopaedia at any time during the game
#screen show_enc_button: