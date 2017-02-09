##############################################################################
# Apothecary Shop
#
# Where you live. 

label return_home:
    $ in_overworld01 = False
    $ in_overworld02 = False
    $ in_kitchen = False
    $ in_cellar = False
    $ in_itemshop = False
    $ in_forest001 = False
    $ in_forest002 = False
    $ in_forest003 = False
    $ in_forest004 = False
    $ in_forest005 = False
    $ in_forest006 = False
    $ in_forest007 = False
    $ in_forest008 = False
    $ in_forest009 = False

    hide screen basic_overlay
    show bg black
    "It's getting late. Better head home."
    call calendar_ani(1)
    "You have a peaceful night's rest."
    jump apothecary_shop

label aplooping:
    $ renpy.pause()
    call timecount2
    call time_img
    jump aplooping
    
label apothecary_shop:    
    
    $ in_overworld01 = False
    $ in_overworld02 = False
    $ in_apothecary = True
    $ in_kitchen = False
    $ in_cellar = False
    $ in_itemshop = False
    $ in_forest001 = False
    $ in_forest002 = False
    $ in_forest003 = False
    $ in_forest004 = False
    $ in_forest005 = False
    $ in_forest006 = False
    $ in_forest007 = False
    $ in_forest008 = False
    $ in_forest009 = False
    
    show bg apothecary
    show screen apothecary
    show screen basic_overlay
    
    "You are in your apothecary shop."
    
    jump aplooping

screen apothecary:
    tag menu2
    
    imagebutton auto "gui/button.shop.workbench_%s.png" xpos 570 ypos 450 focus_mask True action Show("inventory_craftbalm", first_inventory=pc_inv)
    imagebutton auto "gui/button.shop.storage_%s.png" xpos 1221 ypos 0 focus_mask True action Show("inventory_screen", first_inventory=pc_inv, second_inventory=chest, trade_mode=True, bank_mode=True)
    imagebutton auto "gui/button.shop.herblist_%s.png" xpos 1125 ypos 331 focus_mask True action ShowMenu("encyclopaedia_list", encyclopaedia)
    imagebutton auto "gui/button.shop.door_%s.png" xpos 405 ypos 80 focus_mask True action [Hide("basic_overlay"), SetVariable('in_apothecary', False), Jump("overworld01")]
    
    
##############################################################################
# Kitchen
#
# Where you cook. 
    
label kitchen:  
    
    $ in_overworld01 = False
    $ in_overworld02 = False
    $ in_apothecary = False
    $ in_kitchen = True
    $ in_cellar = False
    $ in_itemshop = False
    $ in_forest001 = False
    $ in_forest002 = False
    $ in_forest003 = False
    $ in_forest004 = False
    $ in_forest005 = False
    $ in_forest006 = False
    $ in_forest007 = False
    $ in_forest008 = False
    $ in_forest009 = False
    
    show bg kitchen
    show screen kitchen
    show screen basic_overlay
    
    "You are in the kitchen."
    
    jump aplooping
    
screen kitchen:
    tag menu2
    
    imagebutton auto "gui/button.kitchen.stove_%s.png" xpos 588 ypos 0 focus_mask True action [Show("inventory_kitchen", first_inventory=pc_inv)]
    imagebutton auto "gui/button.kitchen.door_%s.png" xpos 45 ypos 445 focus_mask True action [Hide("basic_overlay"), SetVariable('in_kitchen', False), Jump("cellar")]
    
    
##############################################################################
# Root Cellar
#
# Where you get water. 

    
label cellar:  
    
    $ in_overworld01 = False
    $ in_overworld02 = False
    $ in_apothecary = False
    $ in_kitchen = False
    $ in_cellar = True
    $ in_itemshop = False
    $ in_forest001 = False
    $ in_forest002 = False
    $ in_forest003 = False
    $ in_forest004 = False
    $ in_forest005 = False
    $ in_forest006 = False
    $ in_forest007 = False
    $ in_forest008 = False
    $ in_forest009 = False
    
    show bg cellar
    show screen cellar
    show screen basic_overlay
    
    "You are in the cellar."
    
    jump aplooping
    
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
        
    imagebutton auto "gui/button.cellar.fountain_%s.png" xpos 0 ypos 480 focus_mask True action Jump("fountain")
    