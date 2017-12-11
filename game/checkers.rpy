label check_events:
    
    if current_loc == "apothecary" and day_cnt == 3 and day_003_evt == False:
        jump day_003
    
#    if calendar.month == "September" and calendar.day == 30:
#        jump Harvest_Festival
    
#    if calendar.moonphase == "full moon":
#        $ insanity += 5
    
    return
    


label check_end:
   
    "This function will check to see what ending has been triggered."
   
    return