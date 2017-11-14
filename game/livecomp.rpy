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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right neu.png"),
        )
    
    image aeth alarmed = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right alarmed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left alarmed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right alarmed.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left alarmed.png"),
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right alarmed.png"),
        )
    
    image aeth alert = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right alert.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left alert.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right alert.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left alert.png"),
        
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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right deprecating.png"),
        )
    
    image aeth determined = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right determined.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left determined.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right determined.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left determined.png"),
        
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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right disdain.png"),
        )
    
    image aeth eager = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right eager.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left eager.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right eager.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left eager.png"),
        
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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right glare.png"),
        )
    
    image aeth interested = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right interested.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left interested.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right interested.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left interested.png"),
        
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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right sad_smile.png"),
        )
    
    image aeth shocked = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right shocked.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left shocked.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right shocked.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left shocked.png"),
        
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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right smirk.png"),
        )
    
    image aeth surprised = ConditionSwitch(
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_down right surprised.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_down' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_down left surprised.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'right' ", Image ("images/spr/aeth/aeth vest arms_crossed right surprised.png"),
        "aeth_outfit == 'vest' and aeth_pose == 'arms_crossed' and aeth_facing == 'left' ", Image ("images/spr/aeth/aeth vest arms_crossed left surprised.png"),
        
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
        
        "True", Image ("images/spr/aeth/aeth vest arms_down right unimpressed.png"),
        )
    
    image elaine neu = ConditionSwitch(
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hands_hips right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hands_hips' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hands_hips left neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hips_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hips_pipe right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hips_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hips_pipe left neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest hold_arm right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'hold_arm' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest hold_arm left neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'right' ", Image ("images/spr/elaine/elaine vest smoke_pipe right neu.png"),
        "elaine_outfit == 'vest' and elaine_pose == 'smoke_pipe' and elaine_facing == 'left' ", Image ("images/spr/elaine/elaine vest smoke_pipe left neu.png"),
        
        "True", Image ("images/spr/elaine/elaine vest hands_hips left neu.png"),
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
        
    image lufte neu = ConditionSwitch(
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_down right neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_down' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_down left neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt arms_up right neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'arms_up' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt arms_up left neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'right' ", Image ("images/spr/lufte/lufte shirt biting right neu.png"),
        "lufte_outfit == 'shirt' and lufte_pose == 'biting' and lufte_facing == 'left' ", Image ("images/spr/lufte/lufte shirt biting left neu.png"),
        
        "True", Image ("images/spr/lufte/lufte shirt arms_down left neu.png"),
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