##############################################################################
# Apothecary Shop
#
# Where you live. 

screen apothecary:
    tag menu2
    
    add "bg/apothecary.png"
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Exit" action Quit(confirm=False)
    
    imagebutton auto "gui/button.shop.workbench_%s.png" xpos 570 ypos 450 focus_mask True action Show("inventory_craftbalm", first_inventory=pc_inv)
    imagebutton auto "gui/button.shop.storage_%s.png" xpos 1221 ypos 0 focus_mask True action Show("inventory_screen", first_inventory=pc_inv, second_inventory=chest, trade_mode=True, bank_mode=True)
    imagebutton auto "gui/button.shop.herblist_%s.png" xpos 1125 ypos 331 focus_mask True action Jump("herblist")
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
    
label herblist:
    "Sorry, I haven't programmed that yet!"
    jump looping