##############################################################################
# Forest One
#
# Collect herbs.

label forest001_layout:
    $ forest001_spawn = renpy.random.randint(1, 5)
    

label forest001:
    init python: 
        message = "message"
    
    show bg forest001
    show screen forest001
    
    "Your random number is [forest001_spawn]."
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
    
    if forest001_spawn == 1:
    
        if forest001_second_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_second_herb_col", False), Jump("forest001_second_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest001_fourth_herb_col:
            imagebutton:
                idle "inv/herb006_idle.png"
                hover "inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fourth_herb_col", False), Jump("forest001_fourth_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fifth_herb_col", False), Jump("forest001_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_first_herb_col", False), Jump("forest001_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest001_third_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_third_herb_col", False), Jump("forest001_third_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest001_spawn == 2:
        
        if forest001_third_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_third_herb_col", False), Jump("forest001_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest001_eighth_herb_col:
            imagebutton:
                idle "inv/herb012_idle.png"
                hover "inv/herb012_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_eighth_herb_col", False), Jump("forest001_eighth_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_fourth_herb_col:
            imagebutton:
                idle "inv/herb006_idle.png"
                hover "inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fourth_herb_col", False), Jump("forest001_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest001_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_first_herb_col", False), Jump("forest001_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fifth_herb_col", False), Jump("forest001_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest001_spawn == 3:
    
        if forest001_fourth_herb_col:
            imagebutton:
                idle "inv/herb006_idle.png"
                hover "inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fourth_herb_col", False), Jump("forest001_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_second_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_second_herb_col", False), Jump("forest001_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fifth_herb_col", False), Jump("forest001_fifth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest001_seventh_herb_col:
            imagebutton:
                idle "inv/herb011_idle.png"
                hover "inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_seventh_herb_col", False), Jump("forest001_seventh_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest001_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_first_herb_col", False), Jump("forest001_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest001_spawn == 4:
    
        if forest001_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fifth_herb_col", False), Jump("forest001_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest001_third_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_third_herb_col", False), Jump("forest001_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest001_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_first_herb_col", False), Jump("forest001_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest001_second_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_second_herb_col", False), Jump("forest001_second_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest001_sixth_herb_col:
            imagebutton:
                idle "inv/herb009_idle.png"
                hover "inv/herb009_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_sixth_herb_col", False), Jump("forest001_sixth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest001_spawn == 5:
    
        if forest001_third_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_third_herb_col", False), Jump("forest001_third_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest001_fourth_herb_col:
            imagebutton:
                idle "inv/herb006_idle.png"
                hover "inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fourth_herb_col", False), Jump("forest001_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest001_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_fifth_herb_col", False), Jump("forest001_fifth_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest001_second_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_second_herb_col", False), Jump("forest001_second_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest001_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_first_herb_col", False), Jump("forest001_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest001_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest001
    
label forest001_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest001
    
label forest001_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest001
    
label forest001_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest001
    
label forest001_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest001
    
label forest001_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest001
    
label forest001_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest001
    
label forest001_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest001
    
label leave_forest001:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    

##############################################################################
# Forest Two
#
# Collect herbs.

label forest002_layout:
    $ forest002_spawn = renpy.random.randint(1, 5)
    

label forest002:
    init python: 
        message = "message"
    
    show bg forest002
    show screen forest002
    
    "Your random number is [forest002_spawn]."
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
    
    if forest002_spawn == 1:
    
        if forest002_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_first_herb_col", False), Jump("forest002_first_herb") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
        if forest002_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_fourth_herb_col", False), Jump("forest002_fourth_herb") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
    
        if forest002_sixth_herb_col:
            imagebutton:
                idle "inv/herb008_idle.png"
                hover "inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_sixth_herb_col", False), Jump("forest002_sixth_herb") ]
                xpos 400 ypos 460
                xanchor 0 yanchor 0
            
            
        if forest002_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_third_herb_col", False), Jump("forest002_third_herb") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
            
        if forest002_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_second_herb_col", False), Jump("forest002_second_herb") ]
                xpos 655 ypos 350
                xanchor 0 yanchor 0
                
    if forest002_spawn == 2:
        
        if forest002_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_second_herb_col", False), Jump("forest002_second_herb") ]
                xpos 655 ypos 350
                xanchor 0 yanchor 0
            
        if forest002_seventh_herb_col:
            imagebutton:
                idle "inv/herb010_idle.png"
                hover "inv/herb010_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_seventh_herb_col", False), Jump("forest002_seventh_herb") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
    
        if forest002_eighth_herb_col:
            imagebutton:
                idle "inv/herb011_idle.png"
                hover "inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_eighth_herb_col", False), Jump("forest002_eighth_herb") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
            
            
        if forest002_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_fifth_herb_col", False), Jump("forest002_fifth_herb") ]
                xpos 400 ypos 460
                xanchor 0 yanchor 0
            
        if forest002_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_third_herb_col", False), Jump("forest002_third_herb") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
                
    if forest002_spawn == 3:
    
        if forest002_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_second_herb_col", False), Jump("forest002_second_herb") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
            
        if forest002_sixth_herb_col:
            imagebutton:
                idle "inv/herb008_idle.png"
                hover "inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_sixth_herb_col", False), Jump("forest002_sixth_herb") ]
                xpos 655 ypos 350
                xanchor 0 yanchor 0
    
        if forest002_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_fourth_herb_col", False), Jump("forest002_fourth_herb") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
        if forest002_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_fifth_herb_col", False), Jump("forest002_fifth_herb") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
            
        if forest002_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_first_herb_col", False), Jump("forest002_first_herb") ]
                xpos 400 ypos 460
                xanchor 0 yanchor 0
                
    if forest002_spawn == 4:
    
        if forest002_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_first_herb_col", False), Jump("forest002_first_herb") ]
                xpos 400 ypos 460
                xanchor 0 yanchor 0
            
        if forest002_eighth_herb_col:
            imagebutton:
                idle "inv/herb011_idle.png"
                hover "inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_eighth_herb_col", False), Jump("forest002_eighth_herb") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
    
        if forest002_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_third_herb_col", False), Jump("forest002_third_herb") ]
                xpos 655 ypos 350
                xanchor 0 yanchor 0
            
            
        if forest002_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_second_herb_col", False), Jump("forest002_second_herb") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
        if forest002_sixth_herb_col:
            imagebutton:
                idle "inv/herb008_idle.png"
                hover "inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_sixth_herb_col", False), Jump("forest002_sixth_herb") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
    
    if forest002_spawn == 5:
    
        if forest002_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_fourth_herb_col", False), Jump("forest002_fourth_herb") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
            
        if forest002_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_second_herb_col", False), Jump("forest002_second_herb") ]
                xpos 400 ypos 460
                xanchor 0 yanchor 0
    
        if forest002_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_first_herb_col", False), Jump("forest002_first_herb") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
            
            
        if forest002_fifth_herb_col:
            imagebutton:
                idle "inv/herb007_idle.png"
                hover "inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_fifth_herb_col", False), Jump("forest002_fifth_herb") ]
                xpos 655 ypos 350
                xanchor 0 yanchor 0
            
        if forest002_seventh_herb_col:
            imagebutton:
                idle "inv/herb010_idle.png"
                hover "inv/herb010_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_seventh_herb_col", False), Jump("forest002_seventh_herb") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
    
label forest002_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest002
    
label forest002_second_herb:
    $ pc_inv.take(herb002)
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest002
    
label forest002_third_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest002
    
label forest002_fourth_herb:
    $ pc_inv.take(herb004)
    show screen inventory_popup2(message="Received Oak Bark",item="Oak")
    
    jump forest002
    
label forest002_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest002
    
label forest002_sixth_herb:
    $ pc_inv.take(herb008)
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest002
    
label forest002_seventh_herb:
    $ pc_inv.take(herb010)
    show screen inventory_popup2(message="Received Laurel",item="Laurel")
    
    jump forest002
    
label forest002_eighth_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest002
    
label leave_forest002:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Three
#
# Collect herbs.


label forest003_layout:
    $ forest003_spawn = renpy.random.randint(1, 5)
    

label forest003:
    init python: 
        message = "message"
    
    show bg forest003
    show screen forest003
    
    "Your random number is [forest003_spawn]."
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
    
    if forest003_spawn == 1:
    
        if forest003_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_first_herb_col", False), Jump("forest003_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest003_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_second_herb_col", False), Jump("forest003_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest003_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_third_herb_col", False), Jump("forest003_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest003_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fourth_herb_col", False), Jump("forest003_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest003_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fifth_herb_col", False), Jump("forest003_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest003_spawn == 2:
        
        if forest003_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_first_herb_col", False), Jump("forest003_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest003_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_second_herb_col", False), Jump("forest003_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest003_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_third_herb_col", False), Jump("forest003_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest003_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fourth_herb_col", False), Jump("forest003_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest003_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fifth_herb_col", False), Jump("forest003_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest003_spawn == 3:
    
        if forest003_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_first_herb_col", False), Jump("forest003_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest003_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_second_herb_col", False), Jump("forest003_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest003_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_third_herb_col", False), Jump("forest003_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest003_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fourth_herb_col", False), Jump("forest003_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest003_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fifth_herb_col", False), Jump("forest003_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest003_spawn == 4:
    
        if forest003_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_first_herb_col", False), Jump("forest003_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest003_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_second_herb_col", False), Jump("forest003_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest003_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_third_herb_col", False), Jump("forest003_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest003_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fourth_herb_col", False), Jump("forest003_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest003_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fifth_herb_col", False), Jump("forest003_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest003_spawn == 5:
    
        if forest003_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_first_herb_col", False), Jump("forest003_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest003_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_second_herb_col", False), Jump("forest003_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest003_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_third_herb_col", False), Jump("forest003_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest003_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fourth_herb_col", False), Jump("forest003_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest003_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_fifth_herb_col", False), Jump("forest003_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest003_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest003
    
label forest003_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest003
    
label forest003_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest003
    
label forest003_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest003
    
label forest003_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest003
    
label forest003_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest003
    
label forest003_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest003
    
label forest003_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest003
    
label leave_forest003:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Four
#
# Collect herbs.


label forest004_layout:
    $ forest004_spawn = renpy.random.randint(1, 5)
    

label forest004:
    init python: 
        message = "message"
    
    show bg forest004
    show screen forest004
    
    "Your random number is [forest004_spawn]."
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
    
    if forest004_spawn == 1:
    
        if forest004_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_first_herb_col", False), Jump("forest004_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest004_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_second_herb_col", False), Jump("forest004_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest004_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_third_herb_col", False), Jump("forest004_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest004_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fourth_herb_col", False), Jump("forest004_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest004_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fifth_herb_col", False), Jump("forest004_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest004_spawn == 2:
        
        if forest004_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_first_herb_col", False), Jump("forest004_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest004_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_second_herb_col", False), Jump("forest004_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest004_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_third_herb_col", False), Jump("forest004_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest004_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fourth_herb_col", False), Jump("forest004_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest004_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fifth_herb_col", False), Jump("forest004_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest004_spawn == 3:
    
        if forest004_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_first_herb_col", False), Jump("forest004_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest004_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_second_herb_col", False), Jump("forest004_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest004_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_third_herb_col", False), Jump("forest004_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest004_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fourth_herb_col", False), Jump("forest004_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest004_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fifth_herb_col", False), Jump("forest004_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest004_spawn == 4:
    
        if forest004_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_first_herb_col", False), Jump("forest004_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest004_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_second_herb_col", False), Jump("forest004_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest004_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_third_herb_col", False), Jump("forest004_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest004_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fourth_herb_col", False), Jump("forest004_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest004_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fifth_herb_col", False), Jump("forest004_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest004_spawn == 5:
    
        if forest004_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_first_herb_col", False), Jump("forest004_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest004_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_second_herb_col", False), Jump("forest004_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest004_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_third_herb_col", False), Jump("forest004_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest004_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fourth_herb_col", False), Jump("forest004_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest004_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_fifth_herb_col", False), Jump("forest004_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest004_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest004
    
label forest004_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest004
    
label forest004_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest004
    
label forest004_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest004
    
label forest004_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest004
    
label forest004_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest004
    
label forest004_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest004
    
label forest004_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest004
    
label leave_forest004:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Five
#
# Collect herbs.


label forest005_layout:
    $ forest005_spawn = renpy.random.randint(1, 5)
    

label forest005:
    init python: 
        message = "message"
    
    show bg forest005
    show screen forest005
    
    "Your random number is [forest005_spawn]."
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
    
    if forest005_spawn == 1:
    
        if forest005_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_first_herb_col", False), Jump("forest005_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest005_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_second_herb_col", False), Jump("forest005_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest005_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_third_herb_col", False), Jump("forest005_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest005_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fourth_herb_col", False), Jump("forest005_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest005_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fifth_herb_col", False), Jump("forest005_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest005_spawn == 2:
        
        if forest005_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_first_herb_col", False), Jump("forest005_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest005_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_second_herb_col", False), Jump("forest005_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest005_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_third_herb_col", False), Jump("forest005_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest005_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fourth_herb_col", False), Jump("forest005_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest005_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fifth_herb_col", False), Jump("forest005_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest005_spawn == 3:
    
        if forest005_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_first_herb_col", False), Jump("forest005_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest005_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_second_herb_col", False), Jump("forest005_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest005_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_third_herb_col", False), Jump("forest005_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest005_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fourth_herb_col", False), Jump("forest005_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest005_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fifth_herb_col", False), Jump("forest005_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest005_spawn == 4:
    
        if forest005_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_first_herb_col", False), Jump("forest005_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest005_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_second_herb_col", False), Jump("forest005_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest005_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_third_herb_col", False), Jump("forest005_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest005_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fourth_herb_col", False), Jump("forest005_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest005_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fifth_herb_col", False), Jump("forest005_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest005_spawn == 5:
    
        if forest005_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_first_herb_col", False), Jump("forest005_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest005_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_second_herb_col", False), Jump("forest005_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest005_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_third_herb_col", False), Jump("forest005_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest005_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fourth_herb_col", False), Jump("forest005_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest005_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_fifth_herb_col", False), Jump("forest005_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest005_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest005
    
label forest005_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest005
    
label forest005_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest005
    
label forest005_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest005
    
label forest005_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest005
    
label forest005_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest005
    
label forest005_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest005
    
label forest005_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest005
    
label leave_forest005:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Six
#
# Collect herbs.


label forest006_layout:
    $ forest006_spawn = renpy.random.randint(1, 5)
    

label forest006:
    init python: 
        message = "message"
    
    show bg forest006
    show screen forest006
    
    "Your random number is [forest006_spawn]."
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
    
    if forest006_spawn == 1:
    
        if forest006_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_first_herb_col", False), Jump("forest006_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest006_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_second_herb_col", False), Jump("forest006_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest006_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_third_herb_col", False), Jump("forest006_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest006_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fourth_herb_col", False), Jump("forest006_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest006_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fifth_herb_col", False), Jump("forest006_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest006_spawn == 2:
        
        if forest006_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_first_herb_col", False), Jump("forest006_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest006_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_second_herb_col", False), Jump("forest006_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest006_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_third_herb_col", False), Jump("forest006_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest006_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fourth_herb_col", False), Jump("forest006_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest006_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fifth_herb_col", False), Jump("forest006_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest006_spawn == 3:
    
        if forest006_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_first_herb_col", False), Jump("forest006_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest006_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_second_herb_col", False), Jump("forest006_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest006_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_third_herb_col", False), Jump("forest006_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest006_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fourth_herb_col", False), Jump("forest006_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest006_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fifth_herb_col", False), Jump("forest006_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest006_spawn == 4:
    
        if forest006_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_first_herb_col", False), Jump("forest006_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest006_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_second_herb_col", False), Jump("forest006_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest006_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_third_herb_col", False), Jump("forest006_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest006_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fourth_herb_col", False), Jump("forest006_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest006_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fifth_herb_col", False), Jump("forest006_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest006_spawn == 5:
    
        if forest006_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_first_herb_col", False), Jump("forest006_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest006_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_second_herb_col", False), Jump("forest006_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest006_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_third_herb_col", False), Jump("forest006_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest006_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fourth_herb_col", False), Jump("forest006_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest006_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_fifth_herb_col", False), Jump("forest006_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest006_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest001
    
label forest006_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest001
    
label forest006_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest006
    
label forest006_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest006
    
label forest006_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest006
    
label forest006_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest006
    
label forest006_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest006
    
label forest006_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest006
    
label leave_forest006:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Seven
#
# Collect herbs.


label forest007_layout:
    $ forest007_spawn = renpy.random.randint(1, 5)
    

label forest007:
    init python: 
        message = "message"
    
    show bg forest007
    show screen forest007
    
    "Your random number is [forest007_spawn]."
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
    
    if forest007_spawn == 1:
    
        if forest007_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_first_herb_col", False), Jump("forest007_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest007_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_second_herb_col", False), Jump("forest007_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest007_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_third_herb_col", False), Jump("forest007_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest007_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fourth_herb_col", False), Jump("forest007_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest007_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fifth_herb_col", False), Jump("forest007_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest007_spawn == 2:
        
        if forest007_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_first_herb_col", False), Jump("forest007_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest007_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_second_herb_col", False), Jump("forest007_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest007_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_third_herb_col", False), Jump("forest007_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest007_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fourth_herb_col", False), Jump("forest007_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest007_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fifth_herb_col", False), Jump("forest007_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest007_spawn == 3:
    
        if forest007_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_first_herb_col", False), Jump("forest007_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest007_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_second_herb_col", False), Jump("forest007_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest007_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_third_herb_col", False), Jump("forest007_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest007_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fourth_herb_col", False), Jump("forest007_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest007_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fifth_herb_col", False), Jump("forest007_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest007_spawn == 4:
    
        if forest007_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_first_herb_col", False), Jump("forest007_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest007_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_second_herb_col", False), Jump("forest007_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest007_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_third_herb_col", False), Jump("forest007_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest007_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fourth_herb_col", False), Jump("forest007_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest007_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fifth_herb_col", False), Jump("forest007_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest007_spawn == 5:
    
        if forest007_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_first_herb_col", False), Jump("forest007_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest007_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_second_herb_col", False), Jump("forest007_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest007_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_third_herb_col", False), Jump("forest007_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest007_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fourth_herb_col", False), Jump("forest007_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest007_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_fifth_herb_col", False), Jump("forest007_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest007_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest007
    
label forest007_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest007
    
label forest007_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest007
    
label forest007_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest007
    
label forest007_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest007
    
label forest007_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest007
    
label forest007_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest007
    
label forest007_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest007
    
label leave_forest007:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Eight
#
# Collect herbs.


label forest008_layout:
    $ forest008_spawn = renpy.random.randint(1, 5)
    

label forest008:
    init python: 
        message = "message"
    
    show bg forest008
    show screen forest008
    
    "Your random number is [forest008_spawn]."
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
    
    if forest008_spawn == 1:
    
        if forest008_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_first_herb_col", False), Jump("forest008_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest008_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_second_herb_col", False), Jump("forest008_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest008_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_third_herb_col", False), Jump("forest008_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest008_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fourth_herb_col", False), Jump("forest008_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest008_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fifth_herb_col", False), Jump("forest008_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest008_spawn == 2:
        
        if forest008_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_first_herb_col", False), Jump("forest008_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest008_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_second_herb_col", False), Jump("forest008_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest008_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_third_herb_col", False), Jump("forest008_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest008_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fourth_herb_col", False), Jump("forest008_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest008_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fifth_herb_col", False), Jump("forest008_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest008_spawn == 3:
    
        if forest008_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_first_herb_col", False), Jump("forest008_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest008_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_second_herb_col", False), Jump("forest008_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest008_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_third_herb_col", False), Jump("forest008_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest008_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fourth_herb_col", False), Jump("forest008_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest008_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fifth_herb_col", False), Jump("forest008_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest008_spawn == 4:
    
        if forest008_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_first_herb_col", False), Jump("forest008_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest008_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_second_herb_col", False), Jump("forest008_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest008_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_third_herb_col", False), Jump("forest008_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest008_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fourth_herb_col", False), Jump("forest008_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest008_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fifth_herb_col", False), Jump("forest008_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest008_spawn == 5:
    
        if forest008_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_first_herb_col", False), Jump("forest008_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest008_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_second_herb_col", False), Jump("forest008_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest008_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_third_herb_col", False), Jump("forest008_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest008_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fourth_herb_col", False), Jump("forest008_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest008_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_fifth_herb_col", False), Jump("forest008_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest008_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest008
    
label forest008_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest008
    
label forest008_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest008
    
label forest008_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest008
    
label forest008_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest008
    
label forest008_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest008
    
label forest008_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest008
    
label forest008_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest008
    
label leave_forest008:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Nine
#
# Collect herbs.


label forest009_layout:
    $ forest009_spawn = renpy.random.randint(1, 5)
    

label forest009:
    init python: 
        message = "message"
    
    show bg forest009
    show screen forest009
    
    "Your random number is [forest009_spawn]."
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
    
    if forest009_spawn == 1:
    
        if forest009_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_first_herb_col", False), Jump("forest009_first_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest009_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_second_herb_col", False), Jump("forest009_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest009_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_third_herb_col", False), Jump("forest009_third_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
            
        if forest009_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fourth_herb_col", False), Jump("forest009_fourth_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest009_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fifth_herb_col", False), Jump("forest009_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest009_spawn == 2:
        
        if forest009_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_first_herb_col", False), Jump("forest009_first_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest009_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_second_herb_col", False), Jump("forest009_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest009_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_third_herb_col", False), Jump("forest009_third_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if forest009_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fourth_herb_col", False), Jump("forest009_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest009_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fifth_herb_col", False), Jump("forest009_fifth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest009_spawn == 3:
    
        if forest009_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_first_herb_col", False), Jump("forest009_first_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest009_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_second_herb_col", False), Jump("forest009_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest009_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_third_herb_col", False), Jump("forest009_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if forest009_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fourth_herb_col", False), Jump("forest009_fourth_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest009_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fifth_herb_col", False), Jump("forest009_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest009_spawn == 4:
    
        if forest009_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_first_herb_col", False), Jump("forest009_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest009_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_second_herb_col", False), Jump("forest009_second_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if forest009_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_third_herb_col", False), Jump("forest009_third_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if forest009_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fourth_herb_col", False), Jump("forest009_fourth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if forest009_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fifth_herb_col", False), Jump("forest009_fifth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest009_spawn == 5:
    
        if forest009_first_herb_col:
            imagebutton:
                idle "inv/herb001_idle.png"
                hover "inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_first_herb_col", False), Jump("forest009_first_herb") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if forest009_second_herb_col:
            imagebutton:
                idle "inv/herb002_idle.png"
                hover "inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_second_herb_col", False), Jump("forest009_second_herb") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if forest009_third_herb_col:
            imagebutton:
                idle "inv/herb003_idle.png"
                hover "inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_third_herb_col", False), Jump("forest009_third_herb") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if forest009_fourth_herb_col:
            imagebutton:
                idle "inv/herb004_idle.png"
                hover "inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fourth_herb_col", False), Jump("forest009_fourth_herb") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if forest009_fifth_herb_col:
            imagebutton:
                idle "inv/herb005_idle.png"
                hover "inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_fifth_herb_col", False), Jump("forest009_fifth_herb") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest009_first_herb:
    $ pc_inv.take(herb001)
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest001
    
label forest009_second_herb:
    $ pc_inv.take(herb003)
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest009
    
label forest009_third_herb:
    $ pc_inv.take(herb005)
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest009
    
label forest009_fourth_herb:
    $ pc_inv.take(herb006)
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest009
    
label forest009_fifth_herb:
    $ pc_inv.take(herb007)
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest009
    
label forest009_sixth_herb:
    $ pc_inv.take(herb009)
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest009
    
label forest009_seventh_herb:
    $ pc_inv.take(herb011)
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest009
    
label forest009_eighth_herb:
    $ pc_inv.take(herb012)
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest009
    
label leave_forest009:
    show screen basic_overlay
    show screen overworld02
    $ time_cnt += 1
    
    jump overworld02    
   