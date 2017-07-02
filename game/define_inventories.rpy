label define_inventories:
    
    ######### DEFINE INVENTORIES ##########    
    $ pc_inv = Inventory("Aeth")
    
    $ pc_inv.take(herb001,250)
    $ pc_inv.take(herb002,250)
    $ pc_inv.take(herb003,250)
    $ pc_inv.take(herb004,250)
    $ pc_inv.take(herb005,250)
    $ pc_inv.take(herb006,250)
    $ pc_inv.take(herb007,250)
    $ pc_inv.take(herb008,250)
    $ pc_inv.take(herb009,250)
    $ pc_inv.take(herb010,250)
    $ pc_inv.take(herb011,250)
    $ pc_inv.take(herb012,250)
    $ pc_inv.take(herb013,250)
    $ pc_inv.take(herb014,250)
    $ pc_inv.take(herb015,250)
    $ pc_inv.take(herb016,250)
    $ pc_inv.take(herb017,250)
    $ pc_inv.take(herb018,250)
    $ pc_inv.take(herb019,250)
    $ pc_inv.take(herb020,250)
    $ pc_inv.take(herb021,250)
    $ pc_inv.take(herb022,250)
    $ pc_inv.take(herb023,250)
    $ pc_inv.take(herb024,250)
    $ pc_inv.take(herb025,250)
    $ pc_inv.take(herb026,250)
    $ pc_inv.take(herb027,250)
    $ pc_inv.take(herb028,250)
    $ pc_inv.take(herb029,250)
    $ pc_inv.take(herb030,250)
    $ pc_inv.take(bandages,500)
    $ pc_inv.take(empty_bottle,500)
    $ pc_inv.take(oil,500)
    $ pc_inv.take(vodka,500)
    $ pc_inv.take(empty_tin,500)
    $ pc_inv.take(wax,500)
    $ pc_inv.take(empty_jar,500)
    $ pc_inv.take(water,500)
    
    $ pc_inv.money = 5000  
    
    $ chest = Inventory("Storage Chest")
    
    $ chest.take(herbID1)
    
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