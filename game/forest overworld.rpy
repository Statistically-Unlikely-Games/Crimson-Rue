##############################################################################
# Forest Overworld
#
# Explore the forest.


label overworld02:
    show screen forest_overworld
    
    "The forest outside of town."
    jump overworld02

screen forest_overworld:
    tag menu2
    
    add "bg/overworld02.png"
    
    imagebutton:
        auto "gui/button.forest001_%s.png" 
        focus_mask True 
        action Jump("forest001")
        xpos 908 ypos 0
        xanchor 0 yanchor 0
         
#    imagebutton:
#        auto "gui/button.overworld.itemshop_%s.png" 
#        focus_mask True 
#        action Jump("item_shop")
#        xpos 1030 ypos 360 
#        xanchor 0 yanchor 0
        
#    imagebutton:
#        auto "gui/button.overworld.forest_%s.png" 
#        focus_mask True
#        action Jump("forest001")
#        xpos 0 ypos 0 
#        xanchor 0 yanchor 0
            
    
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
            