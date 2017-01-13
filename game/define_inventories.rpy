label define_inventories:
    
    ######### DEFINE INVENTORIES ##########    
    $ pc_inv = Inventory("Aeth")
    
    $ pc_inv.take(water,50)
    $ pc_inv.take(herb001,4)
    $ pc_inv.take(herb002)
    $ pc_inv.take(herb003)
    $ pc_inv.take(herb004,2)
    $ pc_inv.take(herb005,3)
    $ pc_inv.take(herb006,2)   
    
    $ pc_inv.money = 5000  
    
    $ chest = Inventory("Storage Chest")
    
    $ shop_inv = Inventory("Item Shop", 5000, 75)
    
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
    
    "Inventories have been defined and populated."