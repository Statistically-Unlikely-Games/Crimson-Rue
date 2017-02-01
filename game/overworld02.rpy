##############################################################################
# Forest Overworld
#
# Explore the forest.

label overworld02:
    show screen basic_overlay
    show screen overworld02
    
    if time_cnt > 5:
        call timecount
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
    
    if F1Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest001_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest001_layout") ]
            xpos 908 ypos 0
            xanchor 0 yanchor 0
    elif F1Harvest == False: 
        imagebutton: 
            auto "gui/button.forest001_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest001_layout") ]
            xpos 908 ypos 0
            xanchor 0 yanchor 0
            
    if F2Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest002_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest002_layout") ]
            xpos 853 ypos 206
            xanchor 0 yanchor 0
    elif F2Harvest == False: 
        imagebutton: 
            auto "gui/button.forest002_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest002_layout") ]
            xpos 853 ypos 206
            xanchor 0 yanchor 0
            
    if F3Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest003_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest003_layout") ]
            xpos 482 ypos 0
            xanchor 0 yanchor 0
    elif F3Harvest == False: 
        imagebutton: 
            auto "gui/button.forest003_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest003_layout") ]
            xpos 482 ypos 0
            xanchor 0 yanchor 0
    
    if F4Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest004_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest004_layout") ]
            xpos 575 ypos 0
            xanchor 0 yanchor 0
    elif F4Harvest == False: 
        imagebutton: 
            auto "gui/button.forest004_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest004_layout") ]
            xpos 575 ypos 0
            xanchor 0 yanchor 0
    
    if F5Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest005_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest005_layout") ]
            xpos 88 ypos 0
            xanchor 0 yanchor 0
    elif F5Harvest == False: 
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
        
    if F7Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest007_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest007_layout") ]
            xpos 0 ypos 240
            xanchor 0 yanchor 0
    elif F7Harvest == False: 
        imagebutton: 
            auto "gui/button.forest007_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest007_layout") ]
            xpos 0 ypos 240
            xanchor 0 yanchor 0
            
    if F8Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest008_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest008_layout") ]
            xpos 665 ypos 295
            xanchor 0 yanchor 0
    elif F8Harvest == False: 
        imagebutton: 
            auto "gui/button.forest008_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest008_layout") ]
            xpos 665 ypos 295
            xanchor 0 yanchor 0
            
    if F9Harvest == True: 
        imagebutton: 
            auto "gui/button.2forest009_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest009_layout") ]
            xpos 922 ypos 405
            xanchor 0 yanchor 0
    elif F9Harvest == False: 
        imagebutton: 
            auto "gui/button.forest009_%s.png"
            focus_mask True 
            clicked [ Hide("basic_overlay"), Jump("forest009_layout") ]
            xpos 922 ypos 405
            xanchor 0 yanchor 0
            
            
        
        
            