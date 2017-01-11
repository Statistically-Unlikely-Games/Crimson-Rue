##############################################################################
# Item Shop
#
# Sell and buy.


label item_shop:
    show screen itemshop
    
    "I can sell my wares and buy new supplies here."
    jump item_shop

screen itemshop:
    tag menu2
    
    add "bg/itemshop.png"
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv)
            textbutton "Leave Shop" action Jump("leave_itemshop")
            textbutton "Exit" action Quit(confirm=False)
    
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
    
    imagebutton: 
        auto "gui/button.itemshop.desk_%s.png" 
        focus_mask True 
        action Show("inventory_screen", first_inventory=pc_inv, second_inventory=shop_inv)
        xpos 655 ypos 420 
        xanchor 0 yanchor 0
    
label leave_itemshop:
    show screen basic_overlay
    show screen overworld
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
                
    if time_cnt == 1:
        $ timeofday = "sunrise"
        "It is now sunrise."
    elif time_cnt == 2:
        $ timeofday = "morning"
        "It is now morning."
    elif time_cnt == 3:
        $ timeofday = "noon"
        "It is now noon."
    elif time_cnt == 4:
        $ timeofday = "sunset"
        "It is now sunset."
    else:
        $ timeofday = "night"
        "It is now night."
    jump overworld01