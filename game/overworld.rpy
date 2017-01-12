##############################################################################
# Overworld Map
#
# Explore the town.

label shop_closed:
    "The shop closes soon, I better leave."
    jump overworld01

label overworld01:
    show screen basic_overlay
    show screen overworld
    
    if time_cnt > 5:
        $ time_cnt = 1
        $ day_cnt += 1
        $ calendar.next()
        $ forest001_herb001_col = True
        $ forest001_herb002_col = True
        $ forest001_herb003_col = True
        $ forest001_herb004_col = True
        $ forest001_herb005_col = True
        
        $ forest002_herb001_col = True
        $ forest002_herb002_col = True
        $ forest002_herb003_col = True
        $ forest002_herb004_col = True
        $ forest002_herb005_col = True
        
        $ forest003_herb001_col = True
        $ forest003_herb002_col = True
        $ forest003_herb003_col = True
        $ forest003_herb004_col = True
        $ forest003_herb005_col = True
        
        $ forest004_herb001_col = True
        $ forest004_herb002_col = True
        $ forest004_herb003_col = True
        $ forest004_herb004_col = True
        $ forest004_herb005_col = True
        
        $ forest005_herb001_col = True
        $ forest005_herb002_col = True
        $ forest005_herb003_col = True
        $ forest005_herb004_col = True
        $ forest005_herb005_col = True
        
        $ forest006_herb001_col = True
        $ forest006_herb002_col = True
        $ forest006_herb003_col = True
        $ forest006_herb004_col = True
        $ forest006_herb005_col = True
        
        $ forest007_herb001_col = True
        $ forest007_herb002_col = True
        $ forest007_herb003_col = True
        $ forest007_herb004_col = True
        $ forest007_herb005_col = True
        
        $ forest008_herb001_col = True
        $ forest008_herb002_col = True
        $ forest008_herb003_col = True
        $ forest008_herb004_col = True
        $ forest008_herb005_col = True
        
        $ forest009_herb001_col = True
        $ forest009_herb002_col = True
        $ forest009_herb003_col = True
        $ forest009_herb004_col = True
        $ forest009_herb005_col = True
        
        "It's getting late. Better head home."
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
    else:
        $ timeofday = "night"
        "It is now night."
    
    "The town where I live."
    jump overworld01

screen overworld:
    tag menu2
    
    add "bg/overworld01.png"
    
    imagebutton:
         auto "gui/button.overworld.apothecary_%s.png" 
         focus_mask True 
         clicked [ Hide("basic_overlay"), Jump("apothecary_shop") ]
         action Jump("apothecary_shop")
         xpos 717 ypos 427 
         xanchor 0 yanchor 0
         
    if time_cnt < 5:
         
        imagebutton:
            auto "gui/button.overworld.itemshop_%s.png" 
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("item_shop") ]
            xpos 1030 ypos 360 
            xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.overworld.forest_%s.png" 
        focus_mask True
        clicked [ Hide("basic_overlay"), Jump("overworld02") ]
        xpos 0 ypos 0 
        xanchor 0 yanchor 0
            
    
#    imagebutton:
#        idle "inv/herb003_idle.png"
#        hover "inv/herb003_hover.png"
#        clicked [ SetVariable("herb003_col", False), Jump("herb003") ]
#        xpos 200 ypos 330
#        xanchor 0 yanchor 0
            
            
#    if herb004_col:
#        imagebutton:
#            idle "inv/herb004_idle.png"
#            hover "inv/herb004_hover.png"
#            clicked [ SetVariable("herb004_col", False), Jump("herb004") ]
#            xpos 600 ypos 390
#            xanchor 0 yanchor 0
            
#    if herb005_col:
#        imagebutton:
#            idle "inv/herb005_idle.png"
#            hover "inv/herb005_hover.png"
#            clicked [ SetVariable("herb005_col", False), Jump("herb005") ]
#            xpos 800 ypos 320
#            xanchor 0 yanchor 0
            