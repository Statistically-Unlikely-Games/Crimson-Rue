## inventory 1.5 demo

init python hide:
    for file in renpy.list_files():
        if file.startswith('bg/') and file.endswith('.png'):
            name = file.replace('/', ' ').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('spr/') and file.endswith('.png'):
            name = file.replace('spr/', '').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('cg/') and file.endswith('.png'):
            name = file.replace('cg/', '').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('gui/') and file.endswith('notification.png'):
            name = file.replace('gui/', '').replace('.png','')
            renpy.image(name, Image(file))
            
            
# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
    show bg black
    $ renpy.pause(0)
    show bg logo
    with dissolve
    with Pause (1.5)
    
    show bg main_menu
    with fade
    with Pause(1.5)
    
    return 
    
      
label start:  
    
    "Game start" 
        
    ## ------------ ESC MENU AND TIME TRACKING --------------------
    
    $ _game_menu_screen = "game_menu" # This code activates the "pause menu" in screens.rpy
    $ calendar = Calendar(6, 1, 2017, 2020) # Calendar(day, month, year, first leap year (can be ignored))
    $ time_cnt = 1
    $ day_cnt = 1
    init python:
        timeofday = "sunrise"
        herb001_col = True
        herb002_col = True
        herb003_col = True
        herb004_col = True
        herb005_col = True
    
    
    ## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
    $ cookbook = list() 
    call items
    $ balmslist = [balm001,balm002,balm003,balm004,balm005,balm006,balm007,balm008,balm009,balm010]
    $ creamslist = [cream001,cream002,cream003,cream004,cream005,cream006,cream007,cream008,cream009,cream010]
    $ extractslist = [extract001,extract002,extract003,extract004,extract005,extract006,extract007,extract008,extract009,extract010]
    $ herboilslist = [herb_oil001,herb_oil002,herb_oil003,herb_oil004,herb_oil005,herb_oil006,herb_oil007,herb_oil008,herb_oil009,herb_oil010]
    $ infusionslist = [infusion001,infusion002,infusion003,infusion004,infusion005,infusion006,infusion007,infusion008,infusion009,infusion010]
    $ salveslist = [salve001,salve002,salve003,salve004,salve005,salve006,salve007,salve008,salve009,salve010]
    $ tinctureslist = [tincture001,tincture002,tincture003,tincture004,tincture005,tincture006,tincture007,tincture008,tincture009,tincture010]
    
    
    $ pc_inv.take(water,50)
    $ pc_inv.take(herb001,4)
    $ pc_inv.take(herb002)
    $ pc_inv.take(herb003)
    $ pc_inv.take(herb004,2)
    $ pc_inv.take(herb005,3)
    $ pc_inv.take(herb006,2)   
    
    $ pc_inv.money = 5000  
    $ shop_inv = Inventory("Shop", 5000, 75)
    $ shop_inv.take(herb007,4)
    $ shop_inv.take(herb008,3)
    $ shop_inv.take(herb009,2)
    $ shop_inv.take(herb010)
    $ shop_inv.take(bandages,50)
    $ shop_inv.take(empty_bottle,50)
    $ shop_inv.take(oil,50)
    $ shop_inv.take(wine,50)
    $ shop_inv.take(empty_tin,50)
    $ shop_inv.take(wax,50)
    $ shop_inv.take(empty_jar,50)
    
    $ chest = Inventory("Storage Chest")   
    
    "All inventory items have been generated."
    
    jump apothecary_shop

    
label looping:
    $ renpy.pause()
    jump looping
    
label apothecary_shop:    
    
    show screen apothecary
    
    "You are in your apothecary shop."
    
    jump looping


#    menu:
#        "Feature demo":
#            pass
#        "Skip demo":
#            jump skip_demo
    
#label demo:    
    # Display an inventory by using the inventory object name as the parameter  
#    "For this demo the inventory_screen modal has been set to False (line 150 of inventory.rpy)."
#    show screen inventory_screen(first_inventory=pc_inv)         
    
#    "Let's add some items to Jane's inventory. The format is item, quantity."
#    $ pc_inv.take(coin,4)
#    $ pc_inv.take(sword)
#    $ pc_inv.take(eye)
#    $ pc_inv.take(but,2)
#    $ pc_inv.take(fabric,3)
#    $ pc_inv.take(yarn,2)        
      
#    "You can hover over the items to see a description. If you click on the sword you will perform the action associated with that item (show a screen with a message).  You can sort inventory several ways and can switch between a grid and list view. If you're using text items you'll only want to enable the list view."  
    
#    "Now, let's remove a coin."
#    $ pc_inv.drop(coin)   
    
#    "We can also check to see if Jane has a certain item.  The check function returns the quantity, if any."    
#    if pc_inv.qty(coin): 
#        $ qty = pc_inv.qty(coin)
#        "Jane still has [qty] coins. Good job, Jane."
#    else:
#        "Jane doesn't have any coins. You must have changed this script!"   

#    if pc_inv.qty(but):
#        $ qty = pc_inv.qty(but)
#        "Jane has [qty] buttons."
#    else:
#        "Jane doesn't have any buttons."
        
#    "You can also change an item and modify the name, description, and icon if you need to."
#    $ sword.change("Broken sword", "This sword is old and busted.", "inv/broke_sword.png", 50, act=Show("inventory_popup", message="It's broken, be careful!"))
    
#    "Now the sword is broken and you can't even wave it around anymore.  Let's sell it and buy something else."
    
#    "We'll create a vendor named Mindy and give her money and inventory.  Mindy really likes eyes and buttons. Her barter percentage is 75, so she will only buy items from Jane at 75 percent of their value."
#    $ mindy_inv = Inventory("Mindy", 500, 75)
#    $ mindy_inv.take(eye,4)
#    $ mindy_inv.take(but,3)
#    $ mindy_inv.take(coin,2)    
    
    # vendor screen parameters are left-side inventory, right-side inventory
#    show screen inventory_screen(first_inventory=pc_inv, second_inventory=mindy_inv)
    
#    "Now we'll give Jane some walking-around money."
#    $ pc_inv.money = 500    
    
#    "The inventory screen can take two inventory parameters and display the inventories side-by-side. You can click an item to buy/sell between the two.  Neither character can buy items if they don't have enough money.  Trade mode allows you to exchange items without money and bank mode allows withdrawing and depositing money."    
    
#    $ chest = Inventory("Storage Chest")

#    "Using trade and bank modes together, you can create a storage chest."
#    show screen inventory_screen(first_inventory=pc_inv, second_inventory=chest, trade_mode=True, bank_mode=True)    
#    "That's it! Exit to end the demo when you are finished."    
    
#    show screen overlay