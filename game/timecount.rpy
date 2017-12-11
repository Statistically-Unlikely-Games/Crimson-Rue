label timecount_msg:
    
    if time_cnt > 5:
        $ time_cnt = 1
        $ timeofday = "sunrise"
        $ day_cnt += 1
        $ calendar.next()
        
        $ F1Harvest = False
        $ forest001_thistle_col = True
        $ forest001_blackberry_col = True
        $ forest001_oak_col = True
        $ forest001_garlic_col = True
        $ forest001_mint_col = True
        $ forest001_oregano_col = True
        $ forest001_chamomile_col = True
        $ forest001_mullein_col = True
        $ forest001_redclover_col = True
        $ forest001_stjohns_col = True
        $ forest001_burdock_col = True
        $ forest001_sage_col = True
        $ forest001_hyssop_col = True
        $ forest001_borage_col = True
        $ forest001_rosemary_col = True
        $ forest001_licorice_col = True
        $ forest001_poppy_col = True
        
        $ F2Harvest = False
        $ forest002_thistle_col = True
        $ forest002_dandelion_col = True
        $ forest002_blackberry_col = True
        $ forest002_oak_col = True
        $ forest002_oregano_col = True
        $ forest002_parsley_col = True
        $ forest002_chamomile_col = True
        $ forest002_mullein_col = True
        $ forest002_redclover_col = True
        $ forest002_stjohns_col = True
        $ forest002_burdock_col = True
        $ forest002_laurel_col = True
        $ forest002_hyssop_col = True
        $ forest002_calendula_col = True
        $ forest002_rosemary_col = True
        $ forest002_licorice_col = True
        
        $ F3Harvest = False
        $ forest003_thistle_col = True
        $ forest003_blackberry_col = True
        $ forest003_oak_col = True
        $ forest003_garlic_col = True
        $ forest003_oregano_col = True
        $ forest003_parsley_col = True
        $ forest003_chamomile_col = True
        $ forest003_chamomile2_col = True
        $ forest003_mullein_col = True
        $ forest003_redclover_col = True
        $ forest003_stjohns_col = True
        $ forest003_burdock_col = True
        $ forest003_sage_col = True
        $ forest003_borage_col = True
        $ forest003_calendula_col = True
        $ forest003_rosemary_col = True
        $ forest003_licorice_col = True
        
        $ F4Harvest = False
        $ forest004_dandelion_col = True
        $ forest004_blackberry_col = True
        $ forest004_oak_col = True
        $ forest004_mint_col = True
        $ forest004_oregano_col = True
        $ forest004_parsley_col = True
        $ forest004_plantain_col = True
        $ forest004_chamomile_col = True
        $ forest004_violet_col = True
        $ forest004_mullein_col = True
        $ forest004_stjohns_col = True
        $ forest004_burdock_col = True
        $ forest004_sage_col = True
        $ forest004_hyssop_col = True
        $ forest004_calendula_col = True
        $ forest004_rosemary_col = True
        $ forest004_licorice_col = True
        
        $ F5Harvest = False
        $ forest005_thistle_col = True
        $ forest005_dandelion_col = True
        $ forest005_blackberry_col = True
        $ forest005_oak_col = True
        $ forest005_garlic_col = True
        $ forest005_mint_col = True
        $ forest005_plantain_col = True
        $ forest005_chamomile_col = True
        $ forest005_violet_col = True
        $ forest005_mullein_col = True
        $ forest005_stjohns_col = True
        $ forest005_burdock_col = True
        $ forest005_laurel_col = True
        $ forest005_calendula_col = True
        $ forest005_rosemary_col = True
        $ forest005_lemonbalm_col = True
        $ forest005_licorice_col = True
        $ forest005_crownflower_col = True
        
        $ forest006_thistle_col = True
        $ forest006_dandelion_col = True
        $ forest006_oak_col = True
        $ forest006_garlic_col = True
        $ forest006_mint_col = True
        $ forest006_oregano_col = True
        $ forest006_parsley_col = True
        $ forest006_redclover_col = True
        $ forest006_burdock_col = True
        $ forest006_calendula_col = True
        $ forest006_rosemary_col = True
        $ forest006_comfrey_col = True
        $ forest006_crownflower_col = True
        $ forest006_poppy_col = True
        $ forest006_goldenseal_col = True
        
        $ F7Harvest = False
        $ forest007_thistle_col = True
        $ forest007_dandelion_col = True
        $ forest007_blackberry_col = True
        $ forest007_mint_col = True
        $ forest007_oregano_col = True
        $ forest007_parsley_col = True
        $ forest007_violet_col = True
        $ forest007_basil_col = True
        $ forest007_stjohns_col = True
        $ forest007_yellowdock_col = True
        $ forest007_comfrey_col = True
        $ forest007_lemonbalm_col = True
        $ forest007_marshmarigold_col = True
        $ forest007_goldenseal_col = True
        
        $ F8Harvest = False
        $ forest008_thistle_col = True
        $ forest008_dandelion_col = True
        $ forest008_blackberry_col = True
        $ forest008_oak_col = True
        $ forest008_garlic_col = True
        $ forest008_oregano_col = True
        $ forest008_parsley_col = True
        $ forest008_plantain_col = True
        $ forest008_plantain2_col = True
        $ forest008_violet_col = True
        $ forest008_basil_col = True
        $ forest008_stjohns_col = True
        $ forest008_yellowdock_col = True
        $ forest008_borage_col = True
        $ forest008_lemonbalm_col = True
        $ forest008_marshmarigold_col = True
        
        $ F9Harvest = False
        $ forest009_thistle_col = True
        $ forest009_dandelion_col = True
        $ forest009_blackberry_col = True
        $ forest009_violet_col = True
        $ forest009_basil_col = True
        $ forest009_stjohns_col = True
        $ forest009_yellowdock_col = True
        $ forest009_sage_col = True
        $ forest009_laurel_col = True
        $ forest009_hyssop_col = True
        $ forest009_comfrey_col = True
        $ forest009_lemonbalm_col = True
        $ forest009_marshmarigold_col = True
        $ forest009_marshmarigold2_col = True
        $ forest009_goldenseal_col = True
        
    if time_cnt == 1:
        $ timeofday = "sunrise"
        "It is now sunrise."
    elif time_cnt == 2:
        $ timeofday = "morning"
        "It is now morning."
    elif time_cnt == 3:
        $ timeofday = "noon"
        "It is now noon."
    elif time_cnt == 4:
        $ timeofday = "sunset"
        "It is now sunset."
    else:
        $ timeofday = "night"
        "It is now night."
    return
    
    
label timecount_nomsg:
    
    if time_cnt > 5:
        $ time_cnt = 1
        $ timeofday = "sunrise"
        $ day_cnt += 1
        $ calendar.next()
        
        $ F1Harvest = False
        $ forest001_thistle_col = True
        $ forest001_blackberry_col = True
        $ forest001_oak_col = True
        $ forest001_garlic_col = True
        $ forest001_mint_col = True
        $ forest001_oregano_col = True
        $ forest001_chamomile_col = True
        $ forest001_mullein_col = True
        $ forest001_redclover_col = True
        $ forest001_stjohns_col = True
        $ forest001_burdock_col = True
        $ forest001_sage_col = True
        $ forest001_hyssop_col = True
        $ forest001_borage_col = True
        $ forest001_rosemary_col = True
        $ forest001_licorice_col = True
        $ forest001_poppy_col = True
        
        $ F2Harvest = False
        $ forest002_thistle_col = True
        $ forest002_dandelion_col = True
        $ forest002_blackberry_col = True
        $ forest002_oak_col = True
        $ forest002_oregano_col = True
        $ forest002_parsley_col = True
        $ forest002_chamomile_col = True
        $ forest002_mullein_col = True
        $ forest002_redclover_col = True
        $ forest002_stjohns_col = True
        $ forest002_burdock_col = True
        $ forest002_laurel_col = True
        $ forest002_hyssop_col = True
        $ forest002_calendula_col = True
        $ forest002_rosemary_col = True
        $ forest002_licorice_col = True
        
        $ F3Harvest = False
        $ forest003_thistle_col = True
        $ forest003_blackberry_col = True
        $ forest003_oak_col = True
        $ forest003_garlic_col = True
        $ forest003_oregano_col = True
        $ forest003_parsley_col = True
        $ forest003_chamomile_col = True
        $ forest003_chamomile2_col = True
        $ forest003_mullein_col = True
        $ forest003_redclover_col = True
        $ forest003_stjohns_col = True
        $ forest003_burdock_col = True
        $ forest003_sage_col = True
        $ forest003_borage_col = True
        $ forest003_calendula_col = True
        $ forest003_rosemary_col = True
        $ forest003_licorice_col = True
        
        $ F4Harvest = False
        $ forest004_dandelion_col = True
        $ forest004_blackberry_col = True
        $ forest004_oak_col = True
        $ forest004_mint_col = True
        $ forest004_oregano_col = True
        $ forest004_parsley_col = True
        $ forest004_plantain_col = True
        $ forest004_chamomile_col = True
        $ forest004_violet_col = True
        $ forest004_mullein_col = True
        $ forest004_stjohns_col = True
        $ forest004_burdock_col = True
        $ forest004_sage_col = True
        $ forest004_hyssop_col = True
        $ forest004_calendula_col = True
        $ forest004_rosemary_col = True
        $ forest004_licorice_col = True
        
        $ F5Harvest = False
        $ forest005_thistle_col = True
        $ forest005_dandelion_col = True
        $ forest005_blackberry_col = True
        $ forest005_oak_col = True
        $ forest005_garlic_col = True
        $ forest005_mint_col = True
        $ forest005_plantain_col = True
        $ forest005_chamomile_col = True
        $ forest005_violet_col = True
        $ forest005_mullein_col = True
        $ forest005_stjohns_col = True
        $ forest005_burdock_col = True
        $ forest005_laurel_col = True
        $ forest005_calendula_col = True
        $ forest005_rosemary_col = True
        $ forest005_lemonbalm_col = True
        $ forest005_licorice_col = True
        $ forest005_crownflower_col = True
        
        $ forest006_thistle_col = True
        $ forest006_dandelion_col = True
        $ forest006_oak_col = True
        $ forest006_garlic_col = True
        $ forest006_mint_col = True
        $ forest006_oregano_col = True
        $ forest006_parsley_col = True
        $ forest006_redclover_col = True
        $ forest006_burdock_col = True
        $ forest006_calendula_col = True
        $ forest006_rosemary_col = True
        $ forest006_comfrey_col = True
        $ forest006_crownflower_col = True
        $ forest006_poppy_col = True
        $ forest006_goldenseal_col = True
        
        $ F7Harvest = False
        $ forest007_thistle_col = True
        $ forest007_dandelion_col = True
        $ forest007_blackberry_col = True
        $ forest007_mint_col = True
        $ forest007_oregano_col = True
        $ forest007_parsley_col = True
        $ forest007_violet_col = True
        $ forest007_basil_col = True
        $ forest007_stjohns_col = True
        $ forest007_yellowdock_col = True
        $ forest007_comfrey_col = True
        $ forest007_lemonbalm_col = True
        $ forest007_marshmarigold_col = True
        $ forest007_goldenseal_col = True
        
        $ F8Harvest = False
        $ forest008_thistle_col = True
        $ forest008_dandelion_col = True
        $ forest008_blackberry_col = True
        $ forest008_oak_col = True
        $ forest008_garlic_col = True
        $ forest008_oregano_col = True
        $ forest008_parsley_col = True
        $ forest008_plantain_col = True
        $ forest008_plantain2_col = True
        $ forest008_violet_col = True
        $ forest008_basil_col = True
        $ forest008_stjohns_col = True
        $ forest008_yellowdock_col = True
        $ forest008_borage_col = True
        $ forest008_lemonbalm_col = True
        $ forest008_marshmarigold_col = True
        
        $ F9Harvest = False
        $ forest009_thistle_col = True
        $ forest009_dandelion_col = True
        $ forest009_blackberry_col = True
        $ forest009_violet_col = True
        $ forest009_basil_col = True
        $ forest009_stjohns_col = True
        $ forest009_yellowdock_col = True
        $ forest009_sage_col = True
        $ forest009_laurel_col = True
        $ forest009_hyssop_col = True
        $ forest009_comfrey_col = True
        $ forest009_lemonbalm_col = True
        $ forest009_marshmarigold_col = True
        $ forest009_marshmarigold2_col = True
        $ forest009_goldenseal_col = True
        
    if time_cnt == 1:
        $ timeofday = "sunrise"
    elif time_cnt == 2:
        $ timeofday = "morning"
    elif time_cnt == 3:
        $ timeofday = "noon"
    elif time_cnt == 4:
        $ timeofday = "sunset"
    else:
        $ timeofday = "night"
        
    #Having the event checker here causes problems bc renpy is still paused in some circumstances
    #Thus, commands like scene and show do not work
    
    return
    
        
label time_img:
    if time_cnt == 1:
        $ timeofday = "sunrise"
    elif time_cnt == 2:
        $ timeofday = "morning"
    elif time_cnt == 3:
        $ timeofday = "noon"
    elif time_cnt == 4:
        $ timeofday = "sunset"
    else:
        $ timeofday = "night"
    return