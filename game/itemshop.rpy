##############################################################################
# Item Shop
#
# Sell and buy.


label item_shop:
    show bg itemshop
    show screen itemshop
    
    "I can sell my wares and buy new supplies here."
    jump item_shop

screen itemshop:
    tag menu2
    
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
        $ timeofday = "sunrise"
        $ day_cnt += 1
        $ calendar.next()
        $ forest001_first_herb_col = True
        $ forest001_second_herb_col = True
        $ forest001_third_herb_col = True
        $ forest001_forth_herb_col = True
        $ forest001_fifth_herb_col = True
        
        $ forest002_first_herb_col = True
        $ forest002_second_herb_col = True
        $ forest002_third_herb_col = True
        $ forest002_forth_herb_col = True
        $ forest002_fifth_herb_col = True
        
        $ forest003_first_herb_col = True
        $ forest003_second_herb_col = True
        $ forest003_third_herb_col = True
        $ forest003_forth_herb_col = True
        $ forest003_fifth_herb_col = True
        
        $ forest004_first_herb_col = True
        $ forest004_second_herb_col = True
        $ forest004_third_herb_col = True
        $ forest004_forth_herb_col = True
        $ forest004_fifth_herb_col = True
        
        $ forest005_first_herb_col = True
        $ forest005_second_herb_col = True
        $ forest005_third_herb_col = True
        $ forest005_forth_herb_col = True
        $ forest005_fifth_herb_col = True
        
        $ forest006_first_herb_col = True
        $ forest006_second_herb_col = True
        $ forest006_third_herb_col = True
        $ forest006_forth_herb_col = True
        $ forest006_fifth_herb_col = True
        
        $ forest007_first_herb_col = True
        $ forest007_second_herb_col = True
        $ forest007_third_herb_col = True
        $ forest007_forth_herb_col = True
        $ forest007_fifth_herb_col = True
        
        $ forest008_first_herb_col = True
        $ forest008_second_herb_col = True
        $ forest008_third_herb_col = True
        $ forest008_forth_herb_col = True
        $ forest008_fifth_herb_col = True
        
        $ forest009_first_herb_col = True
        $ forest009_second_herb_col = True
        $ forest009_third_herb_col = True
        $ forest009_forth_herb_col = True
        $ forest009_fifth_herb_col = True
        
        hide screen itemshop
        
        jump return_home

                
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
        jump shop_closed
    else:
        $ timeofday = "night"
        "It is now night."
    jump overworld01