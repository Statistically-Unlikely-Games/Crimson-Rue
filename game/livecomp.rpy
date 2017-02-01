init-1:
    
    image F1Hover = ConditionSwitch(
        "F1Harvest == True ", Image ("gui/button.forest001_hover2.png"),
        "F1Harvest == False ", Image ("gui/button.forest001_hover.png"),
        "True", Image ("gui/button.forest001_idle.png"),
        )