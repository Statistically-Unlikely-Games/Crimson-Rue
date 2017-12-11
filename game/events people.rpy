##############################################################################
# World Events
#
# This file is used to store all the events triggered as you play through the
# game. Events can be triggered by a choice made by the player or by stats.

## ORTHRUS EVENTS

label Orthrus_evt:
    $ orth_pick = renpy.random.randint(1, 5)
    "Your random number is [orth_pick]."
    
    if orth_pick == 1:
        jump Orthrus_trust_evt
    elif orth_pick == 2:
        jump Orthrus_respect_evt
    elif orth_pick == 3:
        jump Orthrus_rivalry_evt
    elif orth_pick == 4:
        jump Orthrus_platonic_evt
    elif orth_pick == 5:
        jump Orthrus_romantic_evt
    else:
        "This is a random number generator error."
        return
    
#Trust
label Orthrus_trust_evt:

    if orth_tru_evt_1 == False:
        
        "Orthrus doesn't differentiate you from others."
        $ orth_tru_evt_1 = True
        
    elif orth_tru >= 5 and orth_tru_evt_2 == False:
        
        "Orthrus thinks you are reasonably competent."
        $ orth_tru_evt_2 = True
        
    elif orth_tru >= 20 and orth_tru_evt_3 == False:
    
        "Orthrus goes to you for advice."
        $ orth_tru_evt_3 = True
        
    elif orth_tru >= 50 and orth_tru_evt_4 == False:
    
        "Orthrus trusts you with his deepest thoughts."
        $ orth_tru_evt_4 = True
        
    elif orth_tru >= 100 and orth_tru_evt_5 == False:
    
        "Orthrus would trust his sister's life to you."
        $ orth_tru_evt_5 = True
        
    else: 
        "No new Orthrus trust events."
        return
return
    
    
#Respect
label Orthrus_respect_evt:
    
    if orth_res_evt_1 == False:
        
        "Orthrus doesn't think much of you."
        $ orth_res_evt_1 = True
        
    elif orth_res >= 5 and orth_res_evt_2 == False:
        
        "Orthrus feels you have potential."
        $ orth_res_evt_2 = True
        
    elif orth_res >= 20 and orth_res_evt_3 == False:
    
        "Orthrus sees you as an equal."
        $ orth_res_evt_3 = True
        
    elif orth_res >= 50 and orth_res_evt_4 == False:
    
        "Orthrus has deep respect in your abilities."
        $ orth_res_evt_4 = True
    
    elif orth_res >= 100 and orth_res_evt_5 == False:
    
        "Orthrus worships the ground you walk on."
        $ orth_res_evt_5 = True

    else: 
        "No new Orthrus respect events."
        return
return

    
#Rivalry
label Orthrus_rivalry_evt:
    
    if orth_riv_evt_1 == False:
        
        "Orthrus doesn't have much interest in you."
        $ orth_riv_evt_1 = True
    
    elif orth_riv >= 5 and orth_riv_evt_2 == False:
        
        "Orthrus is occasionally playful."
        $ orth_riv_evt_2 = True
        
    elif orth_riv >= 20 and orth_riv_evt_3 == False:
    
        "Orthrus enjoys casual competition with you."
        $ orth_riv_evt_3 = True
        
    elif orth_riv >= 50 and orth_riv_evt_4 == False:
    
        "Orthrus challenges you at every opportunity."
        $ orth_riv_evt_4 = True

    elif orth_riv >= 100 and orth_riv_evt_5 == False:
    
        "Orthrus regularly tries to murder you."
        $ orth_riv_evt_5 = True
        
    else: 
        "No new Orthrus rivalry events."
        return
return

    
#Combo
    
    
#Platonic
label Orthrus_platonic_evt:
    
    if orth_pla_evt_1 == False:
        "Orthrus and you don't really talk."
        $ orth_pla_evt_1 = True
    
    elif orth_pla >= 5 and orth_pla_evt_2 == False:
        "Orthrus occasionally greets you."
        $ orth_pla_evt_2 = True
    
    elif orth_pla >= 20 and orth_pla_evt_3 == False:
    
        "Orthrus enjoys spending time with you."
        $ orth_riv_pla_3 = True
    
    elif orth_pla >= 50 and orth_pla_evt_4 == False:
    
        "Orthrus will threaten anyone who messes with you."
        $ orth_riv_pla_4 = True
    
    elif orth_pla >= 100 and orth_pla_evt_5 == False:
    
        "Orthrus would kill someone for you, no questions asked."
        $ orth_pla_evt_5 = True
        
    else: 
        "No new platonic Orthrus events."
        return
return

    
#Romantic
label Orthrus_romantic_evt:
    
    if orth_pla_rom_1 == False:
        "Orthrus doesn't seem to notice you romantically."
        $ orth_rom_evt_1 = True
    
    elif orth_rom >= 5 and orth_pla_rom_2 == False:
        "Orthrus flirts with you."
        $ orth_rom_evt_2 = True
    
    elif orth_rom >= 20 and orth_pla_rom_3 == False:
    
        "Orthrus starts inviting you out occasionally."
        $ orth_rom_evt_3 = True
    
    elif orth_rom >= 50 and orth_pla_rom_4 == False:
    
        "Orthrus starts spending a lot of time at your house."
        $ orth_rom_evt_4 = True

    elif orth_rom >= 100 and orth_pla_rom_5 == False:
    
        "Orthrus demands you move in with him."
        $ orth_rom_evt_5 = True
    
    else: 
        "No new romantic Orthrus events."
        return
return

    
#Poly