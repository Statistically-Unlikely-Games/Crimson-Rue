##############################################################################
# Overworld Map
#
# Explore the town.

label overworld01_loop:
    $ renpy.pause()
    jump overworld01_loop

label overworld01:

    $ current_loc = "overworld01"

#    $ in_overworld01 = True
#    $ in_overworld02 = False
#    $ in_apothecary = False
#    $ in_kitchen = False
#    $ in_cellar = False
#    $ in_itemshop = False
#    $ in_forest001 = False
#    $ in_forest002 = False
#    $ in_forest003 = False
#    $ in_forest004 = False
#    $ in_forest005 = False
#    $ in_forest006 = False
#    $ in_forest007 = False
#    $ in_forest008 = False
#    $ in_forest009 = False

    show screen basic_overlay
    show screen overworld

    if time_cnt > 5:
        call timecount_nomsg
        hide screen basic_overlay
        hide screen overworld01
        jump return_home
    call timecount_nomsg

#    "The town where I live."
    jump overworld01_loop

screen overworld:
    tag menu2

    add "images/bg/bg overworld01.png"

    imagebutton:
         auto "gui/button.overworld.apothecary_%s.png"
         focus_mask True
         clicked [ Hide("basic_overlay"), SetVariable('in_overworld01', False), Jump("apothecary_shop") ]
         action Jump("apothecary_shop")
         xpos 717 ypos 427
         xanchor 0 yanchor 0

    if time_cnt < 5:

        imagebutton:
            auto "gui/button.overworld.itemshop_%s.png"
            focus_mask True
            clicked [ Hide("basic_overlay"), SetVariable('in_overworld01', False), Jump("item_shop") ]
            xpos 1030 ypos 360
            xanchor 0 yanchor 0

    imagebutton:
        auto "gui/button.overworld.forest_%s.png"
        focus_mask True
        clicked [ Hide("basic_overlay"), SetVariable('in_overworld02', False), Jump("overworld02") ]
        xpos 0 ypos 0
        xanchor 0 yanchor 0
