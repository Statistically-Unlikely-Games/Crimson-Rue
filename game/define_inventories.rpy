label define_inventories:
    
    ######### DEFINE INVENTORIES ##########    
    $ pc_inv = Inventory("Aeth")
    
    $ pc_inv.take(empty_bottle,5)
  
    
    $ pc_inv.money = 15000
    $ pc_inv.take(herbID1)
    $ pc_inv.take(herbID2)
    $ pc_inv.take(herbID3)
    $ pc_inv.take(medJNL1)
    $ pc_inv.take(medJNL2)
    
    $ chest = Inventory("Storage Chest")
    
    $ chest.take(medJNL3)
    $ chest.take(medJNL4)
    $ chest.take(medJNL5)
    $ chest.take(medJNL6)

    
    $ shop_inv = Inventory("Item Shop", 5000, 75)
    
    $ shop_inv.take(herbID2)
    $ shop_inv.take(herbID3)
    $ shop_inv.take(bandages,50)
    $ shop_inv.take(empty_bottle,50)
    $ shop_inv.take(oil,50)
    $ shop_inv.take(vodka,50)
    $ shop_inv.take(empty_tin,50)
    $ shop_inv.take(wax,50)
    $ shop_inv.take(empty_jar,50)
    
    #"Inventories have been defined and populated."
    
    
    
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