##############################################################################
# Apothecary Shop
#
# Where you live. 

label return_home:
    
    $ current_loc = "apothecary"

    hide screen basic_overlay
    scene bg black
    "It's getting late. Better head home."
    call calendar_ani(1)
    "You have a peaceful night's rest. It has been [day_cnt] days since game start."
    jump apothecary_shop
    

label aplooping:
    $ renpy.pause()
    call timecount_nomsg
    call time_img
    jump aplooping
    
label apothecary_shop:    
    
    $ current_loc = "apothecary"
    
    scene bg apothecary
    show screen basic_overlay
    call screen apothecary
    
    
#    "You are in your apothecary shop."
# Before the latest update, I could include this line of dialogue
# and renpy.pause would hide the textbox. After the update, this 
# seems not to be the case. If I have any dialogue, the box stays.
    
    hide screen apothecary
    call check_events
    show screen apothecary
    
    jump aplooping

screen apothecary:
    tag menu2
    
    imagebutton auto "gui/button.shop.rack_%s.png" xpos 844 ypos 152 focus_mask True action Show("drying_screen")
    imagebutton auto "gui/button.shop.scale_%s.png" xpos 652 ypos 397 focus_mask True action Show("craft_screen")
    imagebutton auto "gui/button.shop.mortar_%s.png" xpos 810 ypos 446 focus_mask True action Show("craft_screen")
    imagebutton auto "gui/button.shop.storage_%s.png" xpos 1221 ypos 0 focus_mask True action Show("box_screen", player=player_bag, seller=seller_bag)
    imagebutton auto "gui/button.shop.books_%s.png" xpos 1125 ypos 331 focus_mask True action [Hide("basic_overlay"), Hide("apothecary"), ShowMenu("book_shelf")]
    imagebutton auto "gui/button.shop.door_%s.png" xpos 405 ypos 80 focus_mask True action [Hide("basic_overlay"), SetVariable('current_loc', "none"), Jump("overworld01")]
    
    
##############################################################################
# Kitchen
#
# Where you cook. 
    
label kitchen:  
    
    $ current_loc = "kitchen"
    
    scene bg kitchen
    show screen kitchen
    show screen basic_overlay
    
#    "You are in the kitchen."

    hide screen kitchen
    call check_events
    show screen kitchen
    
    jump aplooping
    
screen kitchen:
    tag menu2
    
    imagebutton auto "gui/button.kitchen.stove_%s.png" xpos 588 ypos 0 focus_mask True action Show("craft_screen")
    imagebutton auto "gui/button.kitchen.door_%s.png" xpos 45 ypos 445 focus_mask True action [Hide("basic_overlay"), SetVariable('current_loc', "none"), Jump("cellar")]
    
    
##############################################################################
# Root Cellar
#
# Where you get water. 

    
label cellar:  
    
    $ current_loc = "cellar"
    
    scene bg cellar
    show screen cellar
    show screen basic_overlay
    
#    "You are in the cellar."

    hide screen cellar
    call check_events
    show screen cellar
    
    jump aplooping
    
label fountain:
#    if pc_inv.qty(empty_bottle):
#        $ pc_inv.take(water)
#        $ pc_inv.drop(empty_bottle) 
#        show screen inventory_popup(message="Received Bottle of Water",item="Bottle of Water")
#        "You draw water from the fountain."
#    else: 
#        "You need a bottle to collect water."
    
    jump cellar
    
screen cellar:
    tag menu2
        
    imagebutton auto "gui/button.cellar.fountain_%s.png" xpos 0 ypos 480 focus_mask True action Jump("fountain")
    imagebutton auto "gui/button.cellar.shelves_%s.png" xpos 0 ypos 0 focus_mask True action Show("fermenting_screen")
    