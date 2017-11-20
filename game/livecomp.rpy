##############################################################################
# Live Composite
#
# Controls all Dynamic Characters

init-1:
    image aeth = "images/spr/aeth/aeth vest arms_down right neu.png"
    #This is a preset to keep you from getting an error.

# ----------------------------------------------------
    image aeth neu = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right neu.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left neu.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right neu.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left neu.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right neu.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left neu.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right neu.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left neu.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right neu.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left neu.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right neu.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left neu.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right neu.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left neu.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right neu.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left neu.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right neu.png"),
        )
    
    image aeth alarmed = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right alarmed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left alarmed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right alarmed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left alarmed.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right alarmed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left alarmed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right alarmed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left alarmed.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right alarmed.png"),
        )
    
    image aeth alert = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right alert.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left alert.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right alert.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left alert.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right alert.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left alert.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right alert.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left alert.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right alert.png"),
        )
    
    image aeth awkward = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right awkward.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left awkward.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right awkward.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left awkward.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right awkward.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left awkward.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right awkward.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left awkward.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right awkward.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left awkward.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right awkward.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left awkward.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right awkward.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left awkward.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right awkward.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left awkward.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right awkward.png"),
        )
    
    image aeth concerned = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right concerned.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left concerned.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right concerned.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left concerned.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right concerned.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left concerned.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right concerned.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left concerned.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right concerned.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left concerned.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right concerned.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left concerned.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right concerned.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left concerned.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right concerned.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left concerned.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right concerned.png"),
        )
    
    image aeth deprecating = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right deprecating.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left deprecating.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right deprecating.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left deprecating.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right deprecating.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left deprecating.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right deprecating.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left deprecating.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right deprecating.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left deprecating.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right deprecating.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left deprecating.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right deprecating.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left deprecating.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right deprecating.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left deprecating.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right deprecating.png"),
        )
    
    image aeth determined = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right determined.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left determined.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right determined.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left determined.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right determined.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left determined.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right determined.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left determined.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right determined.png"),
        )
    
    image aeth disdain = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right disdain.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left disdain.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right disdain.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left disdain.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right disdain.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left disdain.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right disdain.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left disdain.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right disdain.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left disdain.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right disdain.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left disdain.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right disdain.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left disdain.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right disdain.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left disdain.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right disdain.png"),
        )
    
    image aeth eager = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right eager.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left eager.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right eager.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left eager.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right eager.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left eager.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right eager.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left eager.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right eager.png"),
        )
    
    image aeth glare = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right glare.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left glare.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right glare.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left glare.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right glare.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left glare.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right glare.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left glare.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right glare.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left glare.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right glare.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left glare.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right glare.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left glare.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right glare.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left glare.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right glare.png"),
        )
    
    image aeth interested = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right interested.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left interested.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right interested.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left interested.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right interested.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left interested.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right interested.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left interested.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right interested.png"),
        )
    
    image aeth sad = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right sad.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left sad.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right sad.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left sad.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right sad.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left sad.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right sad.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left sad.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right sad.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left sad.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right sad.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left sad.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right sad.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left sad.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right sad.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left sad.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right sad.png"),
        )
    
    image aeth sad_smile = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right sad_smile.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left sad_smile.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right sad_smile.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left sad_smile.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right sad_smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left sad_smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right sad_smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left sad_smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right sad_smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left sad_smile.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right sad_smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left sad_smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right sad_smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left sad_smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right sad_smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left sad_smile.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right sad_smile.png"),
        )
    
    image aeth shocked = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right shocked.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left shocked.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right shocked.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left shocked.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right shocked.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left shocked.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right shocked.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left shocked.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right shocked.png"),
        )
    
    image aeth smile = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right smile.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left smile.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right smile.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left smile.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right smile.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left smile.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right smile.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left smile.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right smile.png"),
        )
    
    image aeth smirk = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right smirk.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left smirk.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right smirk.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left smirk.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right smirk.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left smirk.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right smirk.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left smirk.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right smirk.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left smirk.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right smirk.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left smirk.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right smirk.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left smirk.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right smirk.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left smirk.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right smirk.png"),
        )
    
    image aeth surprised = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right surprised.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left surprised.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right surprised.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left surprised.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right surprised.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left surprised.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right surprised.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left surprised.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right surprised.png"),
        )
    
    image aeth thinking = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right thinking.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left thinking.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right thinking.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left thinking.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right thinking.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left thinking.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right thinking.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left thinking.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right thinking.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left thinking.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right thinking.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left thinking.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right thinking.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left thinking.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right thinking.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left thinking.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right thinking.png"),
        )
    
    image aeth unimpressed = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right unimpressed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left unimpressed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right unimpressed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left unimpressed.png"),
        
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_down right unimpressed.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_down left unimpressed.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_up right unimpressed.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_up left unimpressed.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed right unimpressed.png"),
        "aeth_outfit == 'cloak_up' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_up arms_crossed left unimpressed.png"),
        
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_down right unimpressed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_down left unimpressed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_up right unimpressed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_up' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_up left unimpressed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed right unimpressed.png"),
        "aeth_outfit == 'cloak_down' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth cloak_down arms_crossed left unimpressed.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right unimpressed.png"),
        )
    
    image elaine neu = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left neu.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left neu.png"),
        )
    
    image elaine angry = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right angry.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left angry.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right angry.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left angry.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right angry.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left angry.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left angry.png"),
        )
    
    image elaine disappointed = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right disappointed.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left disappointed.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right disappointed.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left disappointed.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right disappointed.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left disappointed.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left disappointed.png"),
        )
    
    image elaine evaluating = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right evaluating.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left evaluating.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right evaluating.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left evaluating.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right evaluating.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left evaluating.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left evaluating.png"),
        )
    
    image elaine laugh = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right laugh.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left laugh.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right laugh.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left laugh.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right laugh.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left laugh.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left laugh.png"),
        )
    
    image elaine sad = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right sad.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left sad.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right sad.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left sad.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right sad.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left sad.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left sad.png"),
        )
    
    image elaine sad_smile = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right sad_smile.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left sad_smile.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right sad_smile.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left sad_smile.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right sad_smile.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left sad_smile.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left sad_smile.png"),
        )
    
    image elaine shocked = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right shocked.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left shocked.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right shocked.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left shocked.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right shocked.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left shocked.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left shocked.png"),
        )
    
    image elaine shout = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right shout.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left shout.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right shout.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left shout.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right shout.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left shout.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left shout.png"),
        )
    
    image elaine surprised = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right surprised.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left surprised.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right surprised.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left surprised.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right surprised.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left surprised.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left surprised.png"),
        )
    
    image elaine thinking = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right thinking.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left thinking.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right thinking.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left thinking.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right thinking.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left thinking.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left thinking.png"),
        )
    
    image harte neu = ConditionSwitch(
        "harte_outfit == 'apron' and harte_pose == 'book' ", Image ("images/spr/harte/harte apron book neu.png"),
        "harte_outfit == 'apron' and harte_pose == 'pages' ", Image ("images/spr/harte/harte apron pages neu.png"),

        "harte_outfit == 'desk' and harte_pose == 'book' ", Image ("images/spr/harte/harte desk book neu.png"),
        "harte_outfit == 'desk' and harte_pose == 'pages' ", Image ("images/spr/harte/harte desk pages neu.png"),
        "harte_outfit == 'desk' and harte_pose == 'leaning' ", Image ("images/spr/harte/harte desk leaning neu.png"),

        "True", Image ("images/spr/harte/harte apron book neu.png"),
        )
    
    image kayen neu = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down neu.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up neu.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair neu.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles neu.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down neu.png"),
        )
    
    image kayen angry = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down angry.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up angry.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair angry.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles angry.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down angry.png"),
        )
    
    image kayen annoyed = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down annoyed.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up annoyed.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair annoyed.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles annoyed.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down annoyed.png"),
        )
    
    image kayen cruel = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down cruel.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up cruel.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair cruel.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles cruel.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down cruel.png"),
        )
    
    image kayen desperate = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down desperate.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up desperate.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair desperate.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles desperate.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down desperate.png"),
        )
    
    image kayen determined = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down determined.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up determined.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair determined.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles determined.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down determined.png"),
        )
    
    image kayen disgust = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down disgust.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up disgust.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair disgust.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles disgust.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down disgust.png"),
        )
    
    image kayen displeased = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down displeased.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up displeased.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair displeased.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles displeased.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down displeased.png"),
        )
    
    image kayen eager = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down eager.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up eager.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair eager.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles eager.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down eager.png"),
        )
    
    image kayen evaluating = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down evaluating.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up evaluating.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair evaluating.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles evaluating.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down evaluating.png"),
        )
    
    image kayen furious = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down furious.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up furious.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair furious.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles furious.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down furious.png"),
        )
    
    image kayen glare = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down glare.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up glare.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair glare.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles glare.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down glare.png"),
        )
    
    image kayen grin = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down grin.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up grin.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair grin.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles grin.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down grin.png"),
        )
    
    image kayen laugh = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down laugh.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up laugh.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair laugh.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles laugh.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down laugh.png"),
        )
    
    image kayen sad = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down sad.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up sad.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair sad.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles sad.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down sad.png"),
        )
    
    image kayen sad_smile = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down sad_smile.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up sad_smile.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair sad_smile.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles sad_smile.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down sad_smile.png"),
        )
    
    image kayen sheepish = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down sheepish.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up sheepish.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair sheepish.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles sheepish.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down sheepish.png"),
        )
    
    image kayen smile = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down smile.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up smile.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair smile.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles smile.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down smile.png"),
        )
    
    image kayen smirk = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down smirk.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up smirk.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair smirk.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles smirk.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down smirk.png"),
        )
    
    image kayen speechless = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down speechless.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up speechless.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair speechless.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles speechless.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down speechless.png"),
        )
    
    image kayen surprised = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down surprised.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up surprised.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair surprised.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles surprised.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down surprised.png"),
        )
    
    image kayen sympathetic = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down sympathetic.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up sympathetic.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair sympathetic.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles sympathetic.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down sympathetic.png"),
        )
    
    image kayen teasing = ConditionSwitch(
        "kayen_outfit == 'dress' and kayen_pose == 'arm_down' ", Image ("images/spr/kayen/kayen dress arm_down teasing.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'arm_up' ", Image ("images/spr/kayen/kayen dress arm_up teasing.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'hand_hair' ", Image ("images/spr/kayen/kayen dress hand_hair teasing.png"),
        "kayen_outfit == 'dress' and kayen_pose == 'knuckles' ", Image ("images/spr/kayen/kayen dress knuckles teasing.png"),

        "True", Image ("images/spr/kayen/kayen dress arm_down teasing.png"),
        )
        
    image lufte neu = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left neu.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left neu.png"),
        )
    
    image lufte angry = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right angry.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left angry.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right angry.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left angry.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right angry.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left angry.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left angry.png"),
        )
    
    image lufte depressed = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right depressed.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left depressed.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right depressed.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left depressed.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right depressed.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left depressed.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left depressed.png"),
        )
    
    image lufte glare = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right glare.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left glare.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right glare.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left glare.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right glare.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left glare.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left glare.png"),
        )
    
    image lufte laugh = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right laugh.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left laugh.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right laugh.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left laugh.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right laugh.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left laugh.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left laugh.png"),
        )
    
    image lufte pleading = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right pleading.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left pleading.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right pleading.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left pleading.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right pleading.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left pleading.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left pleading.png"),
        )
    
    image lufte pout = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right pout.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left pout.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right pout.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left pout.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right pout.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left pout.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left pout.png"),
        )
    
    image lufte sad = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left sad.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left sad.png"),
        )
    
    image lufte sad = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right sad.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left sad.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left sad.png"),
        )
    
    image lufte shocked = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right shocked.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left shocked.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right shocked.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left shocked.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right shocked.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left shocked.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left shocked.png"),
        )
    
    image lufte smile = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right smile.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left smile.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right smile.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left smile.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right smile.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left smile.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left smile.png"),
        )
    
    image lufte surprised = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right surprised.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left surprised.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right surprised.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left surprised.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right surprised.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left surprised.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left surprised.png"),
        )
    
    image mikael neu = ConditionSwitch(
        "mikael_outfit == 'shirt' and mikael_pose == 'arms_crossed' and mikael_facing == 'right' ", Image ("images/spr/mikael/mikael shirt arms_crossed right neu.png"),
        "mikael_outfit == 'shirt' and mikael_pose == 'arms_crossed' and mikael_facing == 'left' ", Image ("images/spr/mikael/mikael shirt arms_crossed left neu.png"),
        "mikael_outfit == 'shirt' and mikael_pose == 'arms_down' and mikael_facing == 'right' ", Image ("images/spr/mikael/mikael shirt arms_down right neu.png"),
        "mikael_outfit == 'shirt' and mikael_pose == 'arms_down' and mikael_facing == 'left' ", Image ("images/spr/mikael/mikael shirt arms_down left neu.png"),
        "mikael_outfit == 'shirt' and mikael_pose == 'hand_ear' and mikael_facing == 'right' ", Image ("images/spr/mikael/mikael shirt hand_ear right neu.png"),
        "mikael_outfit == 'shirt' and mikael_pose == 'hand_ear' and mikael_facing == 'left' ", Image ("images/spr/mikael/mikael shirt hand_ear left neu.png"),
        
        "True", Image ("images/spr/mikael/mikael shirt arms_crossed left neu.png"),
        )
    
    image orthrus neu = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right neu.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left neu.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right neu.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left neu.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right neu.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left neu.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left neu.png"),
        )
    
    image orthrus angry = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right angry.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left angry.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right angry.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left angry.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right angry.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left angry.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left angry.png"),
        )
    
    image orthrus awkward = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right awkward.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left awkward.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right awkward.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left awkward.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right awkward.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left awkward.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left awkward.png"),
        )
    
    image orthrus competitive = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right competitive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left competitive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right competitive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left competitive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right competitive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left competitive.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left competitive.png"),
        )
    
    image orthrus complaining = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right complaining.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left complaining.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right complaining.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left complaining.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right complaining.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left complaining.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left complaining.png"),
        )
    
    image orthrus disgust = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right disgust.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left disgust.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right disgust.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left disgust.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right disgust.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left disgust.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left disgust.png"),
        )
    
    image orthrus furious = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right furious.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left furious.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right furious.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left furious.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right furious.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left furious.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left furious.png"),
        )
    
    image orthrus glare = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right glare.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left glare.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right glare.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left glare.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right glare.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left glare.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left glare.png"),
        )
    
    image orthrus interested = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right interested.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left interested.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right interested.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left interested.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right interested.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left interested.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left interested.png"),
        )
    
    image orthrus laugh = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right laugh.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left laugh.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right laugh.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left laugh.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right laugh.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left laugh.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left laugh.png"),
        )
    
    image orthrus sad = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right sad.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left sad.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right sad.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left sad.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right sad.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left sad.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left sad.png"),
        )
    
    image orthrus seductive = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right seductive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left seductive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right seductive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left seductive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right seductive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left seductive.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left seductive.png"),
        )
    
    image orthrus shocked = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right shocked.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left shocked.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right shocked.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left shocked.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right shocked.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left shocked.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left shocked.png"),
        )
    
    image orthrus smirk = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right smirk.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left smirk.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right smirk.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left smirk.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right smirk.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left smirk.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left smirk.png"),
        )
    
    image orthrus sneer = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right sneer.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left sneer.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right sneer.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left sneer.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right sneer.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left sneer.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left sneer.png"),
        )
    
    image orthrus snicker = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right snicker.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left snicker.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right snicker.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left snicker.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right snicker.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left snicker.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left snicker.png"),
        )
    
    image orthrus suggestive = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right suggestive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left suggestive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right suggestive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left suggestive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right suggestive.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left suggestive.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left suggestive.png"),
        )
    
    image orthrus surprised = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right surprised.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left surprised.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right surprised.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left surprised.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right surprised.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left surprised.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left surprised.png"),
        )
    
    image orthrus thinking = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right thinking.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left thinking.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right thinking.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left thinking.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right thinking.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left thinking.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left thinking.png"),
        )
    
    image orthrus unhappy = ConditionSwitch(
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed right unhappy.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_crossed' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_crossed left unhappy.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt arms_up right unhappy.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'arms_up' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt arms_up left unhappy.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'right' ", Image ("images/spr/orthrus/orthrus shirt hands_hips right unhappy.png"),
        "orthrus_outfit == 'shirt' and orthrus_pose == 'hands_hips' and orthrus_facing == 'left' ", Image ("images/spr/orthrus/orthrus shirt hands_hips left unhappy.png"),
        
        "True", Image ("images/spr/orthrus/orthrus shirt hands_hips left unhappy.png"),
        )
    
    image teal neu = ConditionSwitch(
        "teal_outfit == 'vest' and teal_pose == 'arm_up' and teal_facing == 'right' ", Image ("images/spr/teal/teal vest arm_up right neu.png"),
        "teal_outfit == 'vest' and teal_pose == 'arm_up' and teal_facing == 'left' ", Image ("images/spr/teal/teal vest arm_up left neu.png"),
        "teal_outfit == 'vest' and teal_pose == 'arms_down' and teal_facing == 'right' ", Image ("images/spr/teal/teal vest arms_down right neu.png"),
        "teal_outfit == 'vest' and teal_pose == 'arms_down' and teal_facing == 'left' ", Image ("images/spr/teal/teal vest arms_down left neu.png"),
        "teal_outfit == 'vest' and teal_pose == 'hand_hair' and teal_facing == 'right' ", Image ("images/spr/teal/teal vest hand_hair right neu.png"),
        "teal_outfit == 'vest' and teal_pose == 'hand_hair' and teal_facing == 'left' ", Image ("images/spr/teal/teal vest hand_hair left neu.png"),
        
        "True", Image ("images/spr/teal/teal vest hand_hair left neu.png"),
        )