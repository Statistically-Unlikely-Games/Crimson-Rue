##############################################################################
# Forest
#
# Collect herbs.


label forest001:
    show screen forest
    
    "Everything is so full of life."
    jump forest001

screen forest:
    tag menu2
    
    add "bg/forest001.png"
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest")
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
    
    if herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("herb001_col", False), Jump("herb001") ]
            xpos 300 ypos 500
            xanchor 0 yanchor 0
            
    if herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("herb002_col", False), Jump("herb002") ]
            xpos 1120 ypos 480
            xanchor 0 yanchor 0
    
    if herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("herb003_col", False), Jump("herb003") ]
            xpos 200 ypos 330
            xanchor 0 yanchor 0
            
            
    if herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("herb004_col", False), Jump("herb004") ]
            xpos 600 ypos 390
            xanchor 0 yanchor 0
            
    if herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("herb005_col", False), Jump("herb005") ]
            xpos 800 ypos 320
            xanchor 0 yanchor 0
            
    
label herb001:
    $ pc_inv.take(herb001)
    "You picked herb1."
    jump forest001
    
label herb002:
    $ pc_inv.take(herb002)
    "You picked herb2."
    jump forest001

label herb003:
    $ pc_inv.take(herb003)
    "You picked herb3."
    jump forest001

label herb004:
    $ pc_inv.take(herb004)
    "You picked herb4."
    jump forest001

label herb005:
    $ pc_inv.take(herb005)
    "You picked herb5."
    jump forest001
    
label leave_forest:
    "I think I'm done here for now."
    show screen overworld
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ herb001_col = True
        $ herb002_col = True
        $ herb003_col = True
        $ herb004_col = True
        $ herb005_col = True
                
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
    jump overworld02