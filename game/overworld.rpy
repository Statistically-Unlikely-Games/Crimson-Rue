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
        call timecount
        hide screen overworld
        
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
        
        