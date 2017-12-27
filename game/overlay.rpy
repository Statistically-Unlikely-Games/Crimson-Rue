screen basic_overlay:
    zorder 2
        
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", bag=player_bag)
            
            if current_loc == "overworld01": 
                textbutton "Return Home" action [Hide("basic_overlay"), SetVariable('current_loc',"none"), Jump("apothecary_shop")]
            elif current_loc == "overworld02": 
                textbutton "Back to Town" action [Hide("basic_overlay"), SetVariable('current_loc',"none"), Jump("overworld01")]
            elif current_loc == "apothecary":
                textbutton "Kitchen" action [Hide("basic_overlay"), SetVariable('current_loc',"none"), Jump("kitchen")]
            elif current_loc == "kitchen": 
                textbutton "Shop Front" action [Hide("basic_overlay"), SetVariable('current_loc',"none"), Jump("apothecary_shop")]
            elif current_loc == "cellar": 
                textbutton "Kitchen" action [Hide("basic_overlay"), SetVariable('current_loc',"none"), Jump("kitchen")]
            elif current_loc == "itemshop": 
                textbutton "Leave Shop" action [Hide("basic_overlay"), SetVariable('current_loc',"none"), Jump("leave_itemshop")]
            elif current_loc == "forest001": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest001")]
            elif current_loc == "forest002": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest002")]
            elif current_loc == "forest003": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest003")]
            elif current_loc == "forest004": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest004")]
            elif current_loc == "forest005": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest005")]
            elif current_loc == "forest006": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest006")]
            elif current_loc == "forest007": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest007")]
            elif current_loc == "forest008": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest008")]
            elif current_loc == "forest009": 
                textbutton "Leave Forest" action [SetVariable('current_loc',"none"), Jump("leave_forest009")]
            elif current_loc == "none":
                textbutton "No Location"
            else: 
                textbutton "Error"
            
            textbutton "Exit Game" action Quit(confirm=False)

    
    python:
        cal_base = "gui/cal/cal base.png"
        if calendar.day < 10:
            day_img = "".join(["gui/cal/cal 0", str(calendar.day), ".png"])
        else:
            day_img = "".join(["gui/cal/cal ", str(calendar.day), ".png"])
        dotw_img = "".join(["gui/cal/cal ", calendar.weekday, ".png"])
        month_img = "".join(["gui/cal/cal ", calendar.month, ".png"])
        moon_img = "".join(["gui/cal/cal ", calendar.moonphase, ".png"])
        time_img = "".join(["gui/cal/cal ", timeofday, ".png"])

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