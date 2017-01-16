##############################################################################
# Forest Overworld
#
# Explore the forest.

label overworld02:
    show screen basic_overlay
    show screen overworld02
    
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
        
        hide screen overworld02
        
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
        
        
            