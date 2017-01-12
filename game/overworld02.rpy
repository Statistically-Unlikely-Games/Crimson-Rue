##############################################################################
# Forest Overworld
#
# Explore the forest.

label overworld02:
    show screen basic_overlay
    show screen overworld02
    
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
    
    "The forest outside of town."
    
    jump overworld02

screen overworld02:
    tag menu2
    
    add "bg/overworld02.png"
    
    imagebutton:
        auto "gui/button.forest001_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest001_layout") ]
        xpos 908 ypos 0
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest002_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest002_layout") ]
        xpos 853 ypos 206
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest003_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest003_layout") ]
        xpos 482 ypos 0
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest004_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest004_layout") ]
        xpos 575 ypos 0
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest005_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest005_layout") ]
        xpos 88 ypos 0
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest006_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest006_layout") ]
        xpos 0 ypos 0
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest007_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest007_layout") ]
        xpos 0 ypos 240
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest008_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest008_layout") ]
        xpos 665 ypos 295
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest009_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest009_layout") ]
        xpos 922 ypos 405
        xanchor 0 yanchor 0
        
        
            