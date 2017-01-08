label items:
    "You are now in the items label."

    ######### DEFINE INVENTORIES ##########    
    $ pc_inv = Inventory("Aeth")
    
    ######### DEFINE ITEM OBJECTS ##########
    ### The format is name, description, icon image (if applicable), value (if applicable, selling/buying value), action (screen language action to be performed when icon is clicked on inventory screen), and recipe (if craftable).
    
    ### Items without icons are created like this:      
    #$ quarter = Item("Quarter", "A new quarter)
    
    ### Items with icons are created like this:
#    $ eye = Item(name="Eyeball", desc="A human eyeball, how creepy!", icon="inv/eye.png", value=250)

    # Items that can be used in crafting
#    $ but = Item("Button", "A shiny button", "inv/button.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
#    $ yarn = Item("Yarn", "Yarny yarny yarn.", "inv/yarn.png", 30, act=Show("inventory_popup", message="This item is only used in crafting"))  
#    $ fabric = Item("Fabric", "You know, cloth.", "inv/fabric.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
#    $ coin = Item("Coin", "An old coin", "inv/coin.png", 1, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    $ herb001 = Item("Herb 1", "A medicinal herb.", "inv/herb001_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb002 = Item("Herb 2", "A medicinal herb.", "inv/herb002_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb003 = Item("Herb 3", "A medicinal herb.", "inv/herb003_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb004 = Item("Herb 4", "A medicinal herb.", "inv/herb004_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb005 = Item("Herb 5", "A medicinal herb.", "inv/herb005_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb006 = Item("Herb 6", "A medicinal herb.", "inv/herb006_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb007 = Item("Herb 7", "A medicinal herb.", "inv/herb007_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb008 = Item("Herb 8", "A medicinal herb.", "inv/herb008_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb009 = Item("Herb 9", "A medicinal herb.", "inv/herb009_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb010 = Item("Herb 10", "A medicinal herb.", "inv/herb010_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    $ bandages = Item("Bandages", "For wrapping wounds.", "inv/bandages.png", 5, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ empty_bottle = Item("Empty Bottle", "Fill it with all kinds of things.", "inv/bottle.empty.png", 300, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ water = Item("Bottle of Water", "Medicine made with this spread easy but spoil faster.", "inv/bottle.water.png", 300, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ oil = Item("Bottle of Oil", "Medicine made with this lasts a long time.", "inv/bottle.oil.png", 500, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ wine = Item("Bottle of Wine", "Useful in makeing tinctures.", "inv/bottle.wine.png", 500, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ empty_tin = Item("Empty Tin", "An empty tin.", "inv/tin.empty.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ wax = Item("Beeswax", "Useful in combining water based extracts with oil.", "inv/tin.wax.png", 200, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ empty_jar = Item("Empty Jar", "An empty jar.", "inv/jar.empty.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    # An item with a unique action (shows screen with custom message)
#    $ sword = Item("Awesome Sword", "An awesome sword.", "inv/sword.png", 500, Show("inventory_popup", message="You wave the sword around wildly but nothing happens."))

    # An item that can be crafted has a recipe, which is a nested list of [ingredient, qty]
#    $ necklace = Item("Penny Necklace", "Super magic.", "inv/necklace.png", 50, recipe=[[coin,6],[yarn,1]])    
#    $ doll = Item("Handmade Doll", "Guaranteed to bring luck. (Or not?) Very huggable, mind the needle.", "inv/doll.png", 100000, recipe=[[but,2],[fabric,3],[yarn,1]]) 
    
    $ extract001 = Item("Herbal Extract 01", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb001,1]]) 
    $ extract002 = Item("Herbal Extract 02", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb002,1]]) 
    $ extract003 = Item("Herbal Extract 03", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb003,1]]) 
    $ extract004 = Item("Herbal Extract 04", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb004,1]]) 
    $ extract005 = Item("Herbal Extract 05", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb005,1]]) 
    $ extract006 = Item("Herbal Extract 06", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb006,1]]) 
    $ extract007 = Item("Herbal Extract 07", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb007,1]]) 
    $ extract008 = Item("Herbal Extract 08", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb008,1]]) 
    $ extract009 = Item("Herbal Extract 09", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb009,1]]) 
    $ extract010 = Item("Herbal Extract 10", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb010,1]])
    
    $ herb_oil001 = Item("Herbal Oil 01", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb001,1]]) 
    $ herb_oil002 = Item("Herbal Oil 02", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb002,1]]) 
    $ herb_oil003 = Item("Herbal Oil 03", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb003,1]]) 
    $ herb_oil004 = Item("Herbal Oil 04", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb004,1]]) 
    $ herb_oil005 = Item("Herbal Oil 05", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb005,1]]) 
    $ herb_oil006 = Item("Herbal Oil 06", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb006,1]]) 
    $ herb_oil007 = Item("Herbal Oil 07", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb007,1]]) 
    $ herb_oil008 = Item("Herbal Oil 08", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb008,1]]) 
    $ herb_oil009 = Item("Herbal Oil 09", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb009,1]]) 
    $ herb_oil010 = Item("Herbal Oil 10", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb010,1]]) 
    
    $ infusion001 = Item("Infusion 01", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract001,1]])
    $ infusion002 = Item("Infusion 02", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract002,1]])
    $ infusion003 = Item("Infusion 03", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract003,1]])
    $ infusion004 = Item("Infusion 04", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract004,1]])
    $ infusion005 = Item("Infusion 05", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract005,1]])
    $ infusion006 = Item("Infusion 06", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract006,1]])
    $ infusion007 = Item("Infusion 07", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract007,1]])
    $ infusion008 = Item("Infusion 08", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract008,1]])
    $ infusion009 = Item("Infusion 09", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract009,1]])
    $ infusion010 = Item("Infusion 10", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract010,1]])
    
    $ tincture001 = Item("Tincture 01", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract001,1]]) 
    $ tincture002 = Item("Tincture 02", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract002,1]]) 
    $ tincture003 = Item("Tincture 03", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract003,1]]) 
    $ tincture004 = Item("Tincture 04", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract004,1]]) 
    $ tincture005 = Item("Tincture 05", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract005,1]]) 
    $ tincture006 = Item("Tincture 06", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract006,1]]) 
    $ tincture007 = Item("Tincture 07", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract007,1]]) 
    $ tincture008 = Item("Tincture 08", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract008,1]]) 
    $ tincture009 = Item("Tincture 09", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract009,1]]) 
    $ tincture010 = Item("Tincture 10", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract010,1]]) 
    
    $ salve001 = Item("Salve 01", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil001,1]])
    $ salve002 = Item("Salve 02", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil002,1]])
    $ salve003 = Item("Salve 03", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil003,1]])
    $ salve004 = Item("Salve 04", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil004,1]])
    $ salve005 = Item("Salve 05", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil005,1]])
    $ salve006 = Item("Salve 06", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil006,1]])
    $ salve007 = Item("Salve 07", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil007,1]])
    $ salve008 = Item("Salve 08", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil008,1]])
    $ salve009 = Item("Salve 09", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil009,1]])
    $ salve010 = Item("Salve 10", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil010,1]])
    
    $ cream001 = Item("Cream 01", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil001,1]])
    $ cream002 = Item("Cream 02", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil002,1]])
    $ cream003 = Item("Cream 03", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil003,1]])
    $ cream004 = Item("Cream 04", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil004,1]])
    $ cream005 = Item("Cream 05", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil005,1]])
    $ cream006 = Item("Cream 06", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil006,1]])
    $ cream007 = Item("Cream 07", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil007,1]])
    $ cream008 = Item("Cream 08", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil008,1]])
    $ cream009 = Item("Cream 09", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil009,1]])
    $ cream010 = Item("Cream 10", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil010,1]])
    
    $ balm001 = Item("Balm 01", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil001,1]])
    $ balm002 = Item("Balm 02", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil002,1]])
    $ balm003 = Item("Balm 03", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil003,1]])
    $ balm004 = Item("Balm 04", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil004,1]])
    $ balm005 = Item("Balm 05", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil005,1]])
    $ balm006 = Item("Balm 06", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil006,1]])
    $ balm007 = Item("Balm 07", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil007,1]])
    $ balm008 = Item("Balm 08", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil008,1]])
    $ balm009 = Item("Balm 09", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil009,1]])
    $ balm010 = Item("Balm 10", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil010,1]])
    
    "Let's return to script."
    
    return 