screen basic_overlay:
    zorder 50
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Return Home" action Jump("apothecary_shop")
            textbutton "Exit" action Quit(confirm=False)
    
    python:
        if _calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(_calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(_calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", _calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", _calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", _calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])
        
    add month_img xpos 22 ypos 12
    add day_img xpos 22 ypos 12
    add dotw_img xpos 22 ypos 12
    add moon_img align(0.17, 0.02)
    add time_img align(0.02, 0.135)