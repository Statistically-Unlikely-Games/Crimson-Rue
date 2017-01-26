# Encyclopaedia Framework for Ren'Py
# Copyright 2014 Joshua Fehler <jsfehler@gmail.com>
# Last Updated: 10/26/2014
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

init -1500 python:
    from operator import itemgetter
    from math import floor
     
     
    class EncyclopaediaAction(Action):
        """Action that requires an encyclopaedia object as an argument."""
        def __init__(self, encyclopaedia):
            self.enc = encyclopaedia
    
    
    class EncyclopaediaEntryAction(EncyclopaediaAction):
        """EncyclopaediaAction that acts using a specific Encyclopaedia Entry"""
        def __init__(self, encyclopaedia, entry_number):
            super(EncyclopaediaEntryAction, self).__init__(encyclopaedia)
            self.entry_number = entry_number    

        """If the entry text is a list, use it. If not, turn it into a list. """
        def string_to_list(self, given_text):
            if type(given_text) is list:
                return given_text
            return [given_text]
 

    class SetEntryAction(EncyclopaediaEntryAction):
        """Action that sets the selected encyclopaedia entry into the displaying frame."""       
        def __call__(self):
            self.given_entry = self.enc.getEntry(self.entry_number)
            self.given_text = self.given_entry.getText()
            
            #entry_text is the entry_numberiable used on the encyclopaedia_entry screen for whatever entry's text we're displaying            
            self.enc.entry_text = self.string_to_list(self.given_text)
 
            #index the list to get what the new current_position should be
            if self.enc.showLockedEntry:
                self.target_position = self.enc.all_entries.index([self.given_entry.number,self.given_entry])
   
            else:
                self.target_position = self.enc.unlocked_entries.index([self.given_entry.number,self.given_entry])
   
            #The EntryData is based on the target_position gotten
            self.enc.setEntryData(self.target_position)
   
            self.enc.current_position = self.target_position
  

    class ChangeEntryAction(EncyclopaediaEntryAction):
        """  
        Scroll through the current entry being viewed. 
        Used by Encyclopaedia's PreviousEntry and NextEntry functions
        """    
        def __init__(self, encyclopaedia, direction, block,*args,**kwargs):  
            self.enc = encyclopaedia
            self.block = block #If the button is active or not
            self.dir = direction  #Determines if it's going to the previous or next entry 
  
        def __call__(self):
            if self.block == False:
                self.enc.setEntryData(self.enc.current_position+self.dir)
 
                if self.enc.showLockedEntry == False:
                    self.enc.unlocked_entries[self.enc.current_position+self.dir][1].status = True 
                    given_text = self.enc.unlocked_entries[self.enc.current_position + self.dir][1].getText()
    
                else: 
                    self.enc.all_entries[self.enc.current_position+self.dir][1].status = True   
                    given_text = self.enc.all_entries[self.enc.current_position + self.dir][1].getText()
 
                self.enc.entry_text = self.string_to_list(given_text)
    
                self.enc.current_position += self.dir
      
                self.enc.sub_current_position = 1 #When changing an entry, the sub-entry page number is set back to 1
                renpy.restart_interaction()
    
        def get_sensitive(self):
            if self.block:
                return False
            return True 
 

    class ChangePageAction(ChangeEntryAction):
        """Change the current sub-entry being viewed."""        
        def __init__(self, encyclopaedia, direction, direction2, block,*args,**kwargs):
            super(ChangePageAction,self).__init__(encyclopaedia, direction, block,*args,**kwargs)

            self.dir1 = direction
            self.dir2 = direction2

        def __call__(self):
            if self.block == False: 
                given_text = self.enc.getUnlockedEntry(self.enc.current_position).getSubEntry(self.enc.sub_current_position + self.dir1)
   
                self.enc.entry_text = self.string_to_list(given_text)
                
                self.enc.sub_current_position += self.dir2
    
                renpy.restart_interaction()
 

    class SortEncyclopaedia(Action):
        """Sorts the entries based on sorting_mode"""        
        def __init__(self, encyclopaedia, sorting_mode="Number"):
            self.enc = encyclopaedia
            self.unlocked_entries = self.enc.unlocked_entries
            self.all_entries = self.enc.all_entries
            self.reverse = False
            if sorting_mode == "Z to A":
                self.reverse = True
            self.sortingMode = sorting_mode

        def _getKey(self,item):
            if self.sortingMode == "Number":
                return item[0]
            return item[1].name

        def __call__(self):
            self.enc.unlocked_entries = sorted(self.unlocked_entries, reverse=self.reverse,key=self._getKey)
            self.enc.all_entries = sorted(self.all_entries, reverse=self.reverse,key=self._getKey)
            self.enc.sortingMode = self.sortingMode
            renpy.restart_interaction()
 

    class SaveStatusAction(Action):
        """
        Saves the "New!" status of every entry in an encyclopaedia. 
        Only necessary if using Persistent Data 
        """
        def __init__(self, encyclopaedia, enc_dict, tag_string):
            self.enc = encyclopaedia
            self.enc_dict = enc_dict
            self.tag_string = tag_string
        
        def __call__(self):
            for x in range(self.enc.size_all):
                self.enc_dict[self.tag_string + str(x)] = self.enc.all_entries[x][1].status   
   

    class ChangeStatusAction(EncyclopaediaEntryAction): 
        """Change the "New!" status of an EncEntry"""    
        def __call__(self):
            self.changed_entry = self.enc.getEntry(self.entry_number)
            self.changed_entry.status = True
 
 
    class ResetSubPageAction(EncyclopaediaAction):
        """Resets the sub-page count to 1. Used when closing the entry screen."""    
        def __call__(self):
            self.enc.sub_current_position = 1
            renpy.restart_interaction()

    
    class ToggleEntryListViewAction(EncyclopaediaAction):    
        def _set_entry_list_size_and_restart_interaction(self):
            """Forces the Entry List to recheck."""
            self.enc.setEntryListSize()
            renpy.restart_interaction()
   
    
    class ToggleShowLockedButtonsAction(ToggleEntryListViewAction):
        """
        Toggles if locked Entries will be shown in the list of Entries or not.
        For the sake of User Experience, this is best left as a debug option.
        """    
        def __call__(self):
            if self.enc.showLockedButtons:
                self.enc.showLockedButtons = False

            else:
                self.enc.showLockedButtons = True
  
            self._set_entry_list_size_and_restart_interaction()
  

    class ToggleShowLockedEntryAction(ToggleEntryListViewAction):
        """
        Toggles if locked Entries can be viewed or not.
        For the sake of User Experience, this is best left as a debug option.
        """    
        def __call__(self):
            if self.enc.showLockedEntry:
                self.enc.showLockedEntry = False

            else:
                self.enc.showLockedEntry = True
  
            self._set_entry_list_size_and_restart_interaction()
    

    class Encyclopaedia(store.object): 
        """Container that manages the display and sorting of a group of EncEntries"""
        def __init__(self, sortingMode="Number", showLockedButtons=False, showLockedEntry=False):
            self.subjects = [] #List of all subjects
            self.unlocked_entries = [] #List of unlocked entries
            self.all_entries = [] #List of all entries, regardless of if locked or not 
            self.size = 0  #Hold the length of self.unlocked_entries  
            self.size_all = 0 #Hold the length of self.all_entries  
            self.entry_list_size = 0 #Is either size or size_all, depending on if locked entries are shown
            self.max_size = 0

            self.sortingMode = sortingMode #Default type of sorting for list screen. Defaults to "Number"

            self.reverseSorting = False
            if sortingMode == "Z to A":
                self.reverseSorting = True
   
            self.showLockedButtons = showLockedButtons #If True, locked entries show "???" on the listing screen. Defaults to True
            self.showLockedEntry = showLockedEntry

            self.current_position = 0 #Indicates the current entry open. Is the current position based on the unlocked list.
            self.sub_current_position = 1 #1 because the main entry is the first page in the sub-entry list

            self.index_page = 0
            self.index = 0

            self.entry_text = ""
  
        def setLockedImageTint(self, tint_amount):
            """Sets all the locked images in an Encyclopaedia to use the same tint."""
            for itemA,itemB in self.all_entries:
                itemB.tintLockedImage((tint_amount[0],tint_amount[1],tint_amount[2]))
  
        def getPercentageUnlocked(self): 
            """Returns string representation of the percentage of the encyclopaedia that's unlocked."""
            float_size = float(self.size)
            float_size_all = float(self.size_all)
            percentage = floor((float_size / float_size_all) * 100)
            return str(int(percentage)) + "%"
  
        def setEntryListSize(self):
            """The entry list size is determined by whether or not locked buttons or locked entries should be shown."""
            if self.showLockedButtons:
                self.entry_list_size = self.size_all
            else:
                self.entry_list_size = self.size
   
            if self.showLockedEntry:
                self.max_size = self.size_all
  
            else:
                self.max_size = self.size
  
        def _getKey(self, item):
            return item[1].name
  
        def unlockEntry(self, item, unlock_flag):
            """Unlocks an EncEntry and adds it to the list of unlocked entries."""
            item.locked = unlock_flag
            self.addEntry(item)
   
        def addEntry(self, item): 
            """Adds an entry to the encyclopaedia and sorts it."""
            if not [item.number,item] in self.all_entries: #Prevent duplicate entries
                self.all_entries.append([item.number,item])
    
            if not [item.number,item] in self.unlocked_entries: #Prevent duplicate entries
                if item.locked == False:
                    self.unlocked_entries.append([item.number,item])
  
            if self.sortingMode == "Number":
                self.unlocked_entries = sorted(self.unlocked_entries,key=itemgetter(0))
                self.all_entries = sorted(self.all_entries,key=itemgetter(0))
            else:
                self.unlocked_entries = sorted(self.unlocked_entries,reverse=self.reverseSorting,key=self._getKey)
                self.all_entries = sorted(self.all_entries,reverse=self.reverseSorting,key=self._getKey)
    
            self.size = len(self.unlocked_entries)
            self.size_all = len(self.all_entries)
            self.setEntryListSize()
 
        def addEntries(self, *new_entries): 
            """Adds multiple new entries at once"""
            for item in new_entries:
                self.addEntry(item)
   
        def addSubject(self, new_subject): 
            """Adds a new subject to the Encyclopaedia, won't allow duplicates"""
            if not new_subject in self.subjects:
                self.subjects.append(new_subject)
  
        def addSubjects(self, *new_subjects): 
            """Adds multiple new subjects at once"""
            for item in new_subjects:
                self.addSubject(item)
     
        def getEntry(self, entry_number): 
            """
            Returns the entry of the specified entry_number. 
            Used for displaying the buttons.
            Depends on if locked entries should be in the entry list or not.
            """
            if self.showLockedButtons:
                return self.all_entries[entry_number][1]
            elif self.showLockedButtons == False:
                return self.unlocked_entries[entry_number][1]
  
        def getAllEntry(self, entry_number): 
            """#Returns the entry of entry_number from all_entries list"""
            return self.all_entries[entry_number][1]

        def getUnlockedEntry(self, entry_number): 
            """Returns the entry matching from unlocked_entries list"""
            return self.unlocked_entries[entry_number][1]
   
        def setEntryData(self, val): 
            """
            Sets the current Entry Data to show on the entry screen.
            Depends on if Locked Entries should be shown or not.
            """
            if self.showLockedEntry == False:
                self.index_page, self.index = self.getUnlockedEntry(val).number, self.getUnlockedEntry(val)
  
            if self.showLockedEntry:
                self.index_page, self.index = self.getAllEntry(val).number, self.getAllEntry(val)
   
        def getEntryData(self):
            """Return whatever the current EntryData should be based on the current index."""
            return self.index_page, self.index
  
        #Checks the current_position against the min or max of the encyclopaedia, returns Boolean
        #Used to determine if the Prev/Next Actions should be active
        def checkMin(self, check_position, min):
            if check_position <= min:
                return True
            return False
 
        def checkMax(self, check_position, max):
            if check_position >= max:
                return True
            return False
     
        def _make_persistent_new_dict(self, total, dk, dv):
            """
            Takes two strings for a series of keys and values. 
            Creates lists and evaluates the values to variables. 
            Combines the lists into a dictionary.
            """
            keys = [dk % x for x in range(total)]
            vals_s = [dv % x for x in range(total)]
            vals = [eval(item) for item in vals_s]
            combo = zip(keys, vals)
            return dict(combo)  

        def setPersistentStatus(self, entries_total=0, master_key="new", name="new"):
            """
            Create the persistent status variables to manage "New!" status if the encyclopaedia is save game independent.
            This will set the variables up, but it's up to you to use them in the "status" argument for an EncEntry.
            
            If you want a save game specific "New!" status, don't use persistent variables and create the EncEntry after the start label, 
            not in an init block.
            """    
            global persistent
            #Set the status variables to the dictionary values.
            master_key = master_key + "_0%s"
            vals_name = name + "_vals"
            dict_name = name + "_dict"

            try:
                setattr(persistent, vals_name, self._make_persistent_new_dict(entries_total, master_key, 'persistent.new_dict["%s"]' % master_key))
                
            except (TypeError, KeyError) as e:
                #The first time the encyclopaedia is launched, the persistent dictionary doesn't exist yet causing a TypeError. This is passed over.
                #In development, the dictionary may already exist, but without the correct number of keys, causing a KeyError. This is passed over. 
                setattr(persistent, vals_name, {master_key % k: None for k in range(entries_total)})
                
            #Set the dictionary values to the status values   
            setattr(persistent, dict_name, self._make_persistent_new_dict(entries_total, master_key, 'persistent.new_vals["%s"]' % master_key))   

        #The following functions all bind Actions to the Encyclopaedia Object.
        def PreviousEntry(self):
            return ChangeEntryAction(self, -1, self.checkMin(self.current_position,0))

        def NextEntry(self):
            return ChangeEntryAction(self, 1, self.checkMax(self.current_position,self.max_size-1))

        def PreviousPage(self):
            return ChangePageAction(self, -2, -1, self.checkMin(self.sub_current_position, 1))

        def NextPage(self):
            return ChangePageAction(self, 0, 1, self.checkMax(self.sub_current_position, self.getEntryData()[1].pages))

        def Sort(self, sorting_mode):
            return SortEncyclopaedia(self, sorting_mode)

        def SetEntry(self,given_entry):
            return SetEntryAction(self, given_entry) 

        def SaveStatus(self, enc_dict, tag_string):
            return SaveStatusAction(self, enc_dict, tag_string)

        def ChangeStatus(self,position):
            return ChangeStatusAction(self,position)

        def ResetSubPage(self):
            return ResetSubPageAction(self)

        def ToggleShowLockedButtons(self):
            return ToggleShowLockedButtonsAction(self) 

        def ToggleShowLockedEntry(self):
            return ToggleShowLockedEntryAction(self)  
            
            
    class EncEntry(store.object):
        """Stores Entry content. Has to be added to an Encyclopaedia or else it will do nothing."""
        def __init__(self, number=0, name="Entry Name", text="Entry Text", subject=None, status=None, locked=False, image=None, locked_image=None):  
            self.number = number
            self.name = name
            self.text = text
            self.status = status
            self.subject = subject
            self.locked = locked
            self.locked_name = "???"
            self.locked_text = "???"
            self.locked_image = locked_image
            self.locked_image_tint = (0.0,0.0,0.0) #Tuple used to set the numbers that tintLockedImage() uses to change the colour of a locked image 

            self.pages = 0 #holds an integer for the number of pages in the entry

            self.hasImage = False  
            if image != None: #If no image is specified, it's assumed the entry was meant to have no image
                self.image = image
                self.hasImage = True  

                if self.locked_image == None: #If no locked image is specified, take the entry image and tint it.
                    self.tintLockedImage(self.locked_image_tint)
   
            self.sub_entry_list = [[1,self]]
            self.hasSubEntry = False #Default status for an Entry is to have no sub-entries
  
        def __repr__(self):
            return str(self.name)
  
        def _get_entry_data(self, data, locked_data):
            """Determines if the locked place-holder should be returned or not?"""
            if self.locked or self.locked == None:
                return locked_data
            return data
  
        def getName(self): 
            """Returns the name of the entry."""
            return self._get_entry_data(self.name, self.locked_name)
 
        def getText(self):
            """Returns the text of the entry."""
            return self._get_entry_data(self.text, self.locked_text)

        def getImage(self):
            """Returns the image of the entry."""
            return self._get_entry_data(self.image, self.locked_image)

        def tintLockedImage(self, tint_amount):
            if self.hasImage:
                matrix = im.matrix.tint(tint_amount[0],tint_amount[1],tint_amount[2] )
                self.locked_image = im.MatrixColor(self.image, matrix)
  
        def addSubEntry(self,sub_entry): #Adds multiple pages in the form of sub-entries
            if not [sub_entry.number,sub_entry] in self.sub_entry_list:
                if not sub_entry in self.sub_entry_list:
                    if sub_entry.locked == False:
                        self.sub_entry_list.append([sub_entry.number,sub_entry])
                        self.sub_entry_list = sorted(self.sub_entry_list,key=itemgetter(0))
                        self.hasSubEntry = True
  
                self.pages = len(self.sub_entry_list)
  
        def addSubEntries(self, *new_sub_entries): #Adds multiple new sub-entries at once
            for item in new_sub_entries:
                self.addSubEntry(item)
 
        def getSubEntry(self,page): #accepts Integer. returns the text on given page 
            return self.sub_entry_list[page][1].text
  
        def unlockSubEntry(self, item, unlock_flag):
            item.locked = unlock_flag
            self.addSubEntry(item)
            self.status = False #If an entry gets sub-entries unlocked, the unread status is restored
            
init -1 python:
 #Function that creates the buttons for each entry.
 #It makes one button, based on the value "x", associated to the given encyclopaedia "enc".
 #Used in a "for loop" on a screen to generate the correct buttons for every entry 
    def generateEntryButton(x,enc):  
        ui.hbox()
        if enc.showLockedButtons:
            if enc.all_entries[x][1].locked == False: #If the entry is unlocked, make the button to go to it. If it's locked, make an inactive "???" button
                ui.textbutton(enc.all_entries[x][1].name, clicked= [ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")] )
                if enc.all_entries[x][1].status == None or enc.all_entries[x][1].status == False:
                    ui.textbutton ("New!")
          
            else: #If locked entries should be shown in the list, the "???" button should go to the entry. If not, it's an inactive button
                if enc.showLockedEntry:
                    ui.textbutton("???", clicked=[ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")])
                else:
                    ui.textbutton("???")
    
        if enc.showLockedButtons == False: #Only showing unlocked entries in this case, no need for the "???" button
            ui.textbutton(enc.unlocked_entries[x][1].name, clicked= [ enc.ChangeStatus(x), enc.SetEntry(x), Show("encyclopaedia_entry")] )
            if enc.unlocked_entries[x][1].status == None or enc.unlocked_entries[x][1].status == False:  
                ui.textbutton ("New!")
        ui.close()

##############################################################################
# Encyclopaedia List
#
# Screen that's used to display the list of entries 
screen encyclopaedia_list:
    tag menu
 
    window:
        style "gm_root"

        vbox:
            spacing 10
  
            frame:
                style_group "mm_root"
                xfill True
                xmargin 10
                top_margin 10
                text "Welcome to the Demo Encyclopaedia"
    
            frame:
                style_group "mm_root"
                xfill True
                xmargin 10
    
                hbox:
                    xfill True
                    text encyclopaedia.getPercentageUnlocked() + " Complete" #Percentage display

            frame:
                style_group "mm_root"  
                xmargin 10
                yfill True
                xmaximum 400
                bottom_margin 10
   
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
     
                    vbox: 
                        text encyclopaedia.sortingMode xalign 0.5 #Flavour text to display the current sorting mode.
     
                        python:
                            #If sorting by subject, display the subject heading and add an entry under it if it's the same subject
                            if encyclopaedia.sortingMode == "Subject":
                                for x in range(len(encyclopaedia.subjects) ):
                                    ui.text(encyclopaedia.subjects[x])
                                    for y in range(encyclopaedia.entry_list_size):  
                                        if encyclopaedia.getEntry(y).subject == encyclopaedia.subjects[x]:
                                            generateEntryButton(y,encyclopaedia)   
       
                            #If sorting by number, add the number next to the entry
                            elif encyclopaedia.sortingMode == "Number":    
                                for x in range(encyclopaedia.entry_list_size):
                                    ui.hbox()
                                    ui.textbutton (str(encyclopaedia.getEntry(x).number))
                                    generateEntryButton(x,encyclopaedia)   
                                    ui.close()
      
                            #If sorting Alphabetically or Reverse-Alphabetically, don't add anything before the entry
                            else:
                                for x in range(encyclopaedia.entry_list_size):
                                    generateEntryButton(x,encyclopaedia) 
    
    frame:
        xalign .98
        yalign .98
        vbox:
            textbutton "Sort by Number" action encyclopaedia.Sort(sorting_mode="Number") #Buttons to sort entries
            textbutton "Sort A to Z" action encyclopaedia.Sort(sorting_mode="A to Z")
            textbutton "Sort Z to A" action encyclopaedia.Sort(sorting_mode="Z to A")
            textbutton "Sort by Subject" action encyclopaedia.Sort(sorting_mode="Subject")
   
            textbutton "Show/Hide Locked Buttons" action encyclopaedia.ToggleShowLockedButtons()
            textbutton "Show/Hide Locked Entry" action encyclopaedia.ToggleShowLockedEntry()
   
            #Sort and SaveStatus are unnecessary if you're not using persistent data
            textbutton "Return"  action [encyclopaedia.Sort(sorting_mode="Number"), encyclopaedia.SaveStatus(persistent.new_dict, "new_0"), Return()] #Sorting mode has to be number to save properly. "new_0" needs to be the prefix for the persistent dictionary.

##############################################################################
# Encyclopaedia Entry
#
# Screen that's used to display each entry 
screen encyclopaedia_entry:
    tag menu
 
    window:
        style "gm_root"  

        xfill True
        yfill True
        vbox:
            spacing 10
  
            frame:
                style_group "mm_root"
                xfill True
                xmargin 10
                top_margin 10
                $page_indicator = "0%d : %s" % (encyclopaedia.getEntryData()[1].number, encyclopaedia.getEntryData()[1].getName()) # Flavour text to indicate which page we're current on
                text page_indicator
  
            frame:
                id "entry_nav"
                style_group "mm_root"
                xfill True
                xmargin 10
                hbox:
                    xfill True
                    textbutton "Previous Entry" xalign .02 action encyclopaedia.PreviousEntry() #Relative to the sorting mode
                    textbutton "Next Entry" xalign .98 action encyclopaedia.NextEntry() #Relative to the sorting mode  
       
            hbox:
                $ddd = config.screen_width
                $dd = config.screen_width/1.46
                $pp = config.screen_height/1.46
                $pp2 = config.screen_height/2
                if encyclopaedia.getEntryData()[1].hasImage: #If the entry or sub-entry has an image, add it to the screen   
                    frame:
                        xmargin 10
                        yfill True
                        xfill True

                        xmaximum dd
                        ymaximum pp  

                        $current_image = encyclopaedia.getEntryData()[1].getImage()
                        add current_image crop (0,10,dd-33,pp-13)
   
                window:
                    id "entry_window"
                    xmargin 10
                    xfill True
                    yfill True
                    xalign 0.5
                    xmaximum ddd
                    ymaximum pp2
                    viewport:
                        scrollbars "vertical"
                        mousewheel True  
                        draggable True
                        xfill True
                        yfill True  
                        vbox:
                            spacing 15
                            for item in encyclopaedia.entry_text: #entry_text is a list of paragraphs from what whatever the current entry is
                                text item

            frame:
                style_group "mm_root"  
                xfill True
                yfill False
                xmargin 10
   
                hbox:
                    xfill True  
  
                    if encyclopaedia.getEntryData()[1].hasSubEntry: #If there's a sub-entry, add Prev/Next Page buttons     
                        textbutton "Previous Page" xalign .02 action encyclopaedia.PreviousPage()

                        text "Page %d / %d" % (encyclopaedia.sub_current_position, encyclopaedia.getEntryData()[1].pages) #Flavour text to indicate which sub-page is being viewed

                        textbutton "Next Page" xalign .98 action encyclopaedia.NextPage()  
 
                    else:
                        text("")
 
        frame:
            xfill True
            xmargin 10

            yalign .98
            hbox:
                xfill True
                text "Sorting Mode: %s" % (encyclopaedia.sortingMode,) #Flavour text that displays the current sorting mode
                textbutton "Close Entry" id "close_entry_button" xalign .98 clicked [encyclopaedia.ResetSubPage(), Show("encyclopaedia_list")] 


##############################################################################
# Encyclopaedia Button
#
# Contains a button to open the encyclopaedia at any time during the game
screen show_enc_button:
    textbutton "Open Encyclopaedia" xalign .98 yalign .02 action ShowMenu("encyclopaedia_list")
    