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