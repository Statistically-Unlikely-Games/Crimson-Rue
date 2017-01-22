##############################################################################
# Apothecary Shop
#
# Where you live. 

label return_home:
    hide screen basic_overlay
    show bg black
    "It's getting late. Better head home."
    "You have a peaceful night's rest."
    jump apothecary_shop

label looping:
    $ renpy.pause()
    jump looping
    
label apothecary_shop:    
    
    show bg apothecary
    hide screen basic_overlay
    show screen apothecary
    
    "You are in your apothecary shop."
    
    jump looping

screen apothecary:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Kitchen" action Jump("kitchen")
            textbutton "Exit" action Quit(confirm=False)
    
    imagebutton auto "gui/button.shop.workbench_%s.png" xpos 570 ypos 450 focus_mask True action Show("inventory_craftbalm", first_inventory=pc_inv)
    imagebutton auto "gui/button.shop.storage_%s.png" xpos 1221 ypos 0 focus_mask True action Show("inventory_screen", first_inventory=pc_inv, second_inventory=chest, trade_mode=True, bank_mode=True)
    imagebutton auto "gui/button.shop.herblist_%s.png" xpos 1125 ypos 331 focus_mask True action ShowMenu("encyclopaedia_list")
    imagebutton auto "gui/button.shop.door_%s.png" xpos 405 ypos 80 focus_mask True action Jump("overworld01")
    
    python:
        if calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])
        
    add month_img xpos 22 ypos 12
    add day_img xpos 22 ypos 12
    add dotw_img xpos 22 ypos 12
    add moon_img align(0.17, 0.02)
    add time_img align(0.02, 0.135)
    
##############################################################################
# Kitchen
#
# Where you cook. 
    
label kitchen:  
    
    show bg kitchen
    show screen kitchen
    
    "You are in the kitchen."
    
    jump looping
    
screen kitchen:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Shop Front" action Jump("apothecary_shop")
            textbutton "Exit" action Quit(confirm=False)
    
    imagebutton auto "gui/button.kitchen.stove_%s.png" xpos 588 ypos 0 focus_mask True action Show("inventory_kitchen", first_inventory=pc_inv)
    imagebutton auto "gui/button.kitchen.door_%s.png" xpos 45 ypos 445 focus_mask True action Jump("cellar")
    
    python:
        if calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])
        
    add month_img xpos 22 ypos 12
    add day_img xpos 22 ypos 12
    add dotw_img xpos 22 ypos 12
    add moon_img align(0.17, 0.02)
    add time_img align(0.02, 0.135)
    
    
##############################################################################
# Root Cellar
#
# Where you get water. 

    
label cellar:  
    
    show bg cellar
    show screen cellar
    
    "You are in the cellar."
    
    jump looping
    
label fountain:
    if pc_inv.qty(empty_bottle):
        $ pc_inv.take(water)
        $ pc_inv.drop(empty_bottle) 
        show screen inventory_popup2(message="Received Bottle of Water",item="Bottle of Water")
        "You draw water from the fountain."
    else: 
        "You need a bottle to collect water."
    
    jump cellar
    
screen cellar:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Kitchen" action Jump("kitchen")
            textbutton "Exit" action Quit(confirm=False)
    
    imagebutton auto "gui/button.cellar.fountain_%s.png" xpos 0 ypos 480 focus_mask True action Jump("fountain")
    
    python:
        if calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])
        
    add month_img xpos 22 ypos 12
    add day_img xpos 22 ypos 12
    add dotw_img xpos 22 ypos 12
    add moon_img align(0.17, 0.02)
    add time_img align(0.02, 0.135)