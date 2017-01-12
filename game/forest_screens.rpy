##############################################################################
# Forest One
#
# Collect herbs.

label f1_layout:
    $ f1 = renpy.random.randint(1, 5)
    

label forest001:
    init python: 
        message = "message"
    
    show bg forest001
    show screen forest001
    
    "Your random number is [f1]."
    "Everything is so full of life."
    jump forest001

screen forest001:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest001")
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
    
    if f1 == 1:
    
        if forest001_herb001_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb001_col", False), Jump("forest001_herb001") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest001_herb002_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb002_col", False), Jump("forest001_herb002") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_herb003_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb003_col", False), Jump("forest001_herb003") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest001_herb004_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb004_col", False), Jump("forest001_herb004") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest001_herb005_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb005_col", False), Jump("forest001_herb005") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if f1 == 2:
        
        if forest001_herb001_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb001_col", False), Jump("forest001_herb001") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest001_herb002_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb002_col", False), Jump("forest001_herb002") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_herb003_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb003_col", False), Jump("forest001_herb003") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest001_herb004_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb004_col", False), Jump("forest001_herb004") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_herb005_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb005_col", False), Jump("forest001_herb005") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if f1 == 3:
    
        if forest001_herb001_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb001_col", False), Jump("forest001_herb001") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_herb002_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb002_col", False), Jump("forest001_herb002") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_herb003_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb003_col", False), Jump("forest001_herb003") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest001_herb004_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb004_col", False), Jump("forest001_herb004") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest001_herb005_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb005_col", False), Jump("forest001_herb005") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if f1 == 4:
    
        if forest001_herb001_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb001_col", False), Jump("forest001_herb001") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest001_herb002_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb002_col", False), Jump("forest001_herb002") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_herb003_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb003_col", False), Jump("forest001_herb003") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest001_herb004_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb004_col", False), Jump("forest001_herb004") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest001_herb005_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb005_col", False), Jump("forest001_herb005") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if f1 == 5:
    
        if forest001_herb001_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb001_col", False), Jump("forest001_herb001") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest001_herb002_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb002_col", False), Jump("forest001_herb002") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest001_herb003_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb003_col", False), Jump("forest001_herb003") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest001_herb004_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb004_col", False), Jump("forest001_herb004") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_herb005_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_herb005_col", False), Jump("forest001_herb005") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
    
    else: 
        text "There was an error in the random number generator."
            
    
label forest001_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest001
    
label forest001_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest001
    
label forest001_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest001
    
label forest001_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest001
    
label forest001_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest001
    
label leave_forest001:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest001_herb001_col = True
        $ forest001_herb002_col = True
        $ forest001_herb003_col = True
        $ forest001_herb004_col = True
        $ forest001_herb005_col = True
                
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
    

##############################################################################
# Forest Two
#
# Collect herbs.


label forest002:
    init python: 
        message = "message"
    
    show bg forest002
    show screen forest002
    
    "Everything is so full of life."
    jump forest002

screen forest002:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest002")
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
    
    if forest002_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest002_herb001_col", False), Jump("forest002_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest002_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest002_herb002_col", False), Jump("forest002_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest002_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest002_herb003_col", False), Jump("forest002_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest002_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest002_herb004_col", False), Jump("forest002_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest002_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest002_herb005_col", False), Jump("forest002_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest002_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest002
    
label forest002_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest002
    
label forest002_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest002
    
label forest002_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest002
    
label forest002_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest002
    
label leave_forest002:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest002_herb001_col = True
        $ forest002_herb002_col = True
        $ forest002_herb003_col = True
        $ forest002_herb004_col = True
        $ forest002_herb005_col = True
                
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
    
    
##############################################################################
# Forest Three
#
# Collect herbs.


label forest003:
    init python: 
        message = "message"
    
    show bg forest003
    show screen forest003
    
    "Everything is so full of life."
    jump forest003

screen forest003:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest003")
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
    
    if forest003_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest003_herb001_col", False), Jump("forest003_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest003_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest003_herb002_col", False), Jump("forest003_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest003_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest003_herb003_col", False), Jump("forest003_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest003_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest003_herb004_col", False), Jump("forest003_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest003_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest003_herb005_col", False), Jump("forest003_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest003_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest003
    
label forest003_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest003
    
label forest003_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest003
    
label forest003_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest003
    
label forest003_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest003
    
label leave_forest003:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest003_herb001_col = True
        $ forest003_herb002_col = True
        $ forest003_herb003_col = True
        $ forest003_herb004_col = True
        $ forest003_herb005_col = True
                
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
    
    
##############################################################################
# Forest Four
#
# Collect herbs.


label forest004:
    init python: 
        message = "message"
    
    show bg forest004
    show screen forest004
    
    "Everything is so full of life."
    jump forest004

screen forest004:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest004")
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
    
    if forest004_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest004_herb001_col", False), Jump("forest004_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest002_herb004_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest004_herb002_col", False), Jump("forest004_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest004_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest004_herb003_col", False), Jump("forest004_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest004_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest004_herb004_col", False), Jump("forest004_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest004_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest004_herb005_col", False), Jump("forest004_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest004_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest004
    
label forest004_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest004
    
label forest004_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest004
    
label forest004_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest004
    
label forest004_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest004
    
label leave_forest004:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest004_herb001_col = True
        $ forest004_herb002_col = True
        $ forest004_herb003_col = True
        $ forest004_herb004_col = True
        $ forest004_herb005_col = True
                
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
    
    
##############################################################################
# Forest Five
#
# Collect herbs.


label forest005:
    init python: 
        message = "message"
    
    show bg forest005
    show screen forest005
    
    "Everything is so full of life."
    jump forest005

screen forest005:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest005")
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
    
    if forest005_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest005_herb001_col", False), Jump("forest005_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest005_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest00_herb002_col", False), Jump("forest005_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest005_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest005_herb003_col", False), Jump("forest005_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest005_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest005_herb004_col", False), Jump("forest005_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest005_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest005_herb005_col", False), Jump("forest005_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest005_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest005
    
label forest005_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest005
    
label forest005_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest005
    
label forest005_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest005
    
label forest005_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest005
    
label leave_forest005:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest005_herb001_col = True
        $ forest005_herb002_col = True
        $ forest005_herb003_col = True
        $ forest005_herb004_col = True
        $ forest005_herb005_col = True
                
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
    
    
##############################################################################
# Forest Six
#
# Collect herbs.


label forest006:
    init python: 
        message = "message"
    
    show bg forest006
    show screen forest006
    
    "Everything is so full of life."
    jump forest006

screen forest006:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest006")
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
    
    if forest006_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest006_herb001_col", False), Jump("forest006_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest006_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest006_herb002_col", False), Jump("forest006_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest006_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest006_herb003_col", False), Jump("forest006_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest006_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest006_herb004_col", False), Jump("forest006_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest006_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest006_herb005_col", False), Jump("forest006_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest006_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest006
    
label forest006_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest006
    
label forest006_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest006
    
label forest006_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest006
    
label forest006_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest006
    
label leave_forest006:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest006_herb001_col = True
        $ forest006_herb002_col = True
        $ forest006_herb003_col = True
        $ forest006_herb004_col = True
        $ forest006_herb005_col = True
                
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
    
    
##############################################################################
# Forest Seven
#
# Collect herbs.


label forest007:
    init python: 
        message = "message"
    
    show bg forest007
    show screen forest007
    
    "Everything is so full of life."
    jump forest007

screen forest007:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest007")
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
    
    if forest007_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest007_herb001_col", False), Jump("forest007_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest007_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest007_herb002_col", False), Jump("forest007_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest007_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest007_herb003_col", False), Jump("forest007_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest007_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest007_herb004_col", False), Jump("forest007_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest007_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest007_herb005_col", False), Jump("forest007_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest007_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest007
    
label forest007_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest007
    
label forest007_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest007
    
label forest007_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest007
    
label forest007_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest007
    
label leave_forest007:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest007_herb001_col = True
        $ forest007_herb002_col = True
        $ forest007_herb003_col = True
        $ forest007_herb004_col = True
        $ forest007_herb005_col = True
                
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
    
    
##############################################################################
# Forest Eight
#
# Collect herbs.


label forest008:
    init python: 
        message = "message"
    
    show bg forest008
    show screen forest008
    
    "Everything is so full of life."
    jump forest008

screen forest008:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest008")
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
    
    if forest008_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest008_herb001_col", False), Jump("forest008_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest008_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest008_herb002_col", False), Jump("forest008_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest008_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest008_herb003_col", False), Jump("forest008_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest008_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest008_herb004_col", False), Jump("forest008_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest008_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest008_herb005_col", False), Jump("forest008_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest008_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest008
    
label forest008_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest008
    
label forest008_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest008
    
label forest008_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest008
    
label forest008_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest008
    
label leave_forest008:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest008_herb001_col = True
        $ forest008_herb002_col = True
        $ forest008_herb003_col = True
        $ forest008_herb004_col = True
        $ forest008_herb005_col = True
                
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
    
    
##############################################################################
# Forest Nine
#
# Collect herbs.


label forest009:
    init python: 
        message = "message"
    
    show bg forest009
    show screen forest009
    
    "Everything is so full of life."
    jump forest009

screen forest009:
    tag menu2
    
    frame:
        yalign 0.0 xalign 0.95
        vbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv) 
            textbutton "Leave Forest" action Jump("leave_forest009")
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
    
    if forest009_herb001_col:
        imagebutton:
            idle "inv/herb001_idle.png"
            hover "inv/herb001_hover.png"
            focus_mask True
            clicked [ SetVariable("forest009_herb001_col", False), Jump("forest009_herb001") ]
            xpos 800 ypos 400
            xanchor 0 yanchor 0
            
    if forest009_herb002_col:
        imagebutton:
            idle "inv/herb002_idle.png"
            hover "inv/herb002_hover.png"
            focus_mask True
            clicked [ SetVariable("forest009_herb002_col", False), Jump("forest009_herb002") ]
            xpos 1000 ypos 550
            xanchor 0 yanchor 0
    
    if forest009_herb003_col:
        imagebutton:
            idle "inv/herb003_idle.png"
            hover "inv/herb003_hover.png"
            focus_mask True
            clicked [ SetVariable("forest009_herb003_col", False), Jump("forest009_herb003") ]
            xpos 400 ypos 460
            xanchor 0 yanchor 0
            
            
    if forest009_herb004_col:
        imagebutton:
            idle "inv/herb004_idle.png"
            hover "inv/herb004_hover.png"
            focus_mask True
            clicked [ SetVariable("forest009_herb004_col", False), Jump("forest009_herb004") ]
            xpos 50 ypos 490
            xanchor 0 yanchor 0
            
    if forest009_herb005_col:
        imagebutton:
            idle "inv/herb005_idle.png"
            hover "inv/herb005_hover.png"
            focus_mask True
            clicked [ SetVariable("forest009_herb005_col", False), Jump("forest009_herb005") ]
            xpos 655 ypos 350
            xanchor 0 yanchor 0
            
    
label forest009_herb001:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Herb1",item="Herb 1")
    
    jump forest009
    
label forest009_herb002:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Herb2",item="Herb 2")
    
    jump forest009
    
label forest009_herb003:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Herb3",item="Herb 3")
    
    jump forest009
    
label forest009_herb004:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Herb4",item="Herb 4")
    
    jump forest009
    
label forest009_herb005:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Herb5",item="Herb 5")
    
    jump forest009
    
label leave_forest009:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest009_herb001_col = True
        $ forest009_herb002_col = True
        $ forest009_herb003_col = True
        $ forest009_herb004_col = True
        $ forest009_herb005_col = True
                
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
    
   