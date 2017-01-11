##############################################################################
# Forest Overworld
#
# Explore the forest.


label overworld02:
    show screen basic_overlay
    show screen overworld02
    
    "The forest outside of town."
    jump overworld02

screen overworld02:
    tag menu2
    
    add "bg/overworld02.png"
    
    imagebutton:
        auto "gui/button.forest001_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest001") ]
        xpos 908 ypos 0
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest002_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest002") ]
        xpos 853 ypos 206
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest003_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest003") ]
        xpos 482 ypos 0
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest004_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest004") ]
        xpos 575 ypos 0
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest005_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest005") ]
        xpos 88 ypos 0
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest006_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest006") ]
        xpos 0 ypos 0
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest007_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest007") ]
        xpos 0 ypos 240
        xanchor 0 yanchor 0
    
    imagebutton:
        auto "gui/button.forest008_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest008") ]
        xpos 665 ypos 295
        xanchor 0 yanchor 0
        
    imagebutton:
        auto "gui/button.forest009_%s.png" 
        focus_mask True 
        clicked [ Hide("basic_overlay"), Jump("forest009") ]
        xpos 922 ypos 405
        xanchor 0 yanchor 0
        
        
            