label check_events:
    
    if current_loc == "itemshop" and day_cnt == 2 and itemshop_day002_evt == False:
        jump itemshop_day002
    
    elif current_loc == "apothecary" and day_cnt == 3 and day_003_evt == False:
        jump day_003
        
    elif current_loc == "forest001" and forest001_evt == False:
        jump forest001_intro
    
#    if calendar.month == "September" and calendar.day == 30:
#        jump Harvest_Festival
    
#    if calendar.moonphase == "full moon":
#        $ insanity += 5
    
    else: 
        return
    


label check_end:
   
    "This function will check to see what ending has been triggered."
   
    return