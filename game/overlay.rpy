screen basic_overlay:
    zorder 2
        
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv)
            
            if in_overworld01 == True: 
                textbutton "Return Home" action [Hide("basic_overlay"), SetVariable('in_overworld01',False), Jump("apothecary_shop")]
            if in_overworld02 == True: 
                textbutton "Back to Town" action [Hide("basic_overlay"), SetVariable('in_overworld02',False), Jump("overworld01")]
            if in_apothecary == True:
                textbutton "Kitchen" action [Hide("basic_overlay"), SetVariable('in_apothecary',False), Jump("kitchen")]
            if in_kitchen == True: 
                textbutton "Shop Front" action [Hide("basic_overlay"), SetVariable('in_kitchen',False), Jump("apothecary_shop")]
            if in_cellar == True: 
                textbutton "Kitchen" action [Hide("basic_overlay"), SetVariable('in_cellar',False), Jump("kitchen")]
            if in_itemshop == True: 
                textbutton "Leave Shop" action [Hide("basic_overlay"), SetVariable('in_itemshop',False), Jump("leave_itemshop")]
            if in_forest001 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest001',False), Jump("leave_forest001")]
            if in_forest002 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest002',False), Jump("leave_forest002")]
            if in_forest003 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest003',False), Jump("leave_forest003")]
            if in_forest004 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest004',False), Jump("leave_forest004")]
            if in_forest005 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest005',False), Jump("leave_forest005")]
            if in_forest006 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest006',False), Jump("leave_forest006")]
            if in_forest007 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest007',False), Jump("leave_forest007")]
            if in_forest008 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest008',False), Jump("leave_forest008")]
            if in_forest009 == True: 
                textbutton "Leave Forest" action [SetVariable('in_forest009',False), Jump("leave_forest009")]
            
            
            textbutton "Exit Game" action Quit(confirm=False)

    
    python:
        cal_base = "cal/cal base.png"
        if calendar.day < 10:
            day_img = "".join(["cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["cal/cal ", timeofday, ".png"])

    add cal_base xpos 0 ypos 0
    add month_img xpos 0 ypos 0
    add day_img xpos 0 ypos 0
    add dotw_img xpos 0 ypos 0
    add moon_img xpos 0 ypos 0
    add time_img xpos 0 ypos 0
    

label moon_check:
    python: 
        month_img = "".join(["cal/cal ", calendar.moonphase, ".png"])
    return