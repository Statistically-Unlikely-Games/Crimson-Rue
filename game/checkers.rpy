label check_events:
    
    if calendar.month == "September" and calendar.day == 30:
        jump Harvest_Festival
    
    #if calendar.moonphase == "full moon":
        #$ insanity += 5
    
    return
    


label check_end:
   
    "This function will check to see what ending has been triggered."
   
    return