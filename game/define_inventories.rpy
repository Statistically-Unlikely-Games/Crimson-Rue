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