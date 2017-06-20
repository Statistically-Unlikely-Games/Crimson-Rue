label define_items:
    #"Encyclopaedia Actions have been imported."
    
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
    
    # An item with a unique action (shows screen with custom message)
#    $ sword = Item("Awesome Sword", "An awesome sword.", "inv/sword.png", 500, Show("inventory_popup", message="You wave the sword around wildly but nothing happens."))

    # An item that can be crafted has a recipe, which is a nested list of [ingredient, qty]
#    $ necklace = Item("Penny Necklace", "Super magic.", "inv/necklace.png", 50, recipe=[[coin,6],[yarn,1]])    
#    $ doll = Item("Handmade Doll", "Guaranteed to bring luck. (Or not?) Very huggable, mind the needle.", "inv/doll.png", 100000, recipe=[[but,2],[fabric,3],[yarn,1]]) 


#Books
    #This is currently broken. It says UnlockEncEntry is not defined. 
    #Need to investigate when the action code for encyclopedia runs. 
    
    $ herbID1 = Item("Herb Identification vol. 1", "A book of herbs", "inv/book.png", 5000, act=[Book.unlock_range(book_2, "all"),Show("inventory_popup", message="New Herbs Unlocked"), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ herbID2 = Item("Herb Identification vol. 2", "A book of herbs", "inv/book.png", 5000, act=[Book.unlock_range(book_2, "all"),Show("inventory_popup", message="New Herbs Unlocked"), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ herbID3 = Item("Herb Identification vol. 3", "A book of herbs", "inv/book.png", 5000, act=[Book.unlock_range(book_2, "all"),Show("inventory_popup", message="New Herbs Unlocked"), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])

#Tier 1 Items
    
    $ herb001 = Item("Thistle", "A medicinal herb.", "inv/herb001_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb002 = Item("Dandelion", "A medicinal herb.", "inv/herb002_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb003 = Item("Blackberry", "A medicinal herb.", "inv/herb003_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb004 = Item("Oak", "A medicinal herb.", "inv/herb004_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb005 = Item("Garlic", "A medicinal herb.", "inv/herb005_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb006 = Item("Mint", "A medicinal herb.", "inv/herb006_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb007 = Item("Oregano", "A medicinal herb.", "inv/herb007_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb008 = Item("Parsley", "A medicinal herb.", "inv/herb008_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb009 = Item("Sage", "A medicinal herb.", "inv/herb009_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb010 = Item("Laurel", "A medicinal herb.", "inv/herb010_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb011 = Item("Hyssop", "A medicinal herb.", "inv/herb011_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb012 = Item("Borage", "A medicinal herb.", "inv/herb012_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb013 = Item("Crown Flower", "A medicinal herb.", "inv/herb013_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb014 = Item("Marsh Marigold", "A medicinal herb.", "inv/herb014_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb015 = Item("Plantain", "A medicinal herb.", "inv/herb015_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb016 = Item("Chamomile", "A medicinal herb.", "inv/herb016_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb017 = Item("Calendula", "A medicinal herb.", "inv/herb017_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb018 = Item("Violet", "A medicinal herb.", "inv/herb018_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))

    $ bandages = Item("Bandages", "For wrapping wounds.", "inv/bandages.png", 5, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ empty_bottle = Item("Empty Bottle", "Fill it with all kinds of things.", "inv/bottle.empty.png", 300, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ water = Item("Bottle of Water", "Medicine made with this spread easy but spoil faster.", "inv/bottle.water.png", 300, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ oil = Item("Bottle of Oil", "Medicine made with this lasts a long time.", "inv/bottle.oil.png", 500, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ wine = Item("Bottle of Wine", "Useful in makeing tinctures.", "inv/bottle.wine.png", 500, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ empty_tin = Item("Empty Tin", "An empty tin.", "inv/tin.empty.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ wax = Item("Beeswax", "Useful in combining water based extracts with oil.", "inv/tin.wax.png", 200, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ empty_jar = Item("Empty Jar", "An empty jar.", "inv/jar.empty.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    
#Tier 2 Items

    $ extract001 = Item("Thistle Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb001,1]], containers=[])
    $ extract002 = Item("Dandelion Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb002,1]], containers=[])
    $ extract003 = Item("Blackberry Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb003,1]], containers=[])
    $ extract004 = Item("Oak Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb004,1]], containers=[])
    $ extract005 = Item("Garlic Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb005,1]], containers=[])
    $ extract006 = Item("Mint Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb006,1]], containers=[])
    $ extract007 = Item("Oregano Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb007,1]], containers=[])
    $ extract008 = Item("Parsley Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb008,1]], containers=[])
    $ extract009 = Item("Sage Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb009,1]], containers=[])
    $ extract010 = Item("Laurel Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb010,1]], containers=[])
    $ extract011 = Item("Hyssop Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb011,1]], containers=[])
    $ extract012 = Item("Barage Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb012,1]], containers=[])
    $ extract013 = Item("Crown Flower Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb013,1]], containers=[])
    $ extract014 = Item("Marsh Marigold Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb014,1]], containers=[])
    $ extract015 = Item("Plantain Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb015,1]], containers=[])
    $ extract016 = Item("Chamomile Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb016,1]], containers=[])
    $ extract017 = Item("Calendula Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb017,1]], containers=[])
    $ extract018 = Item("Violet Extract", "Made by boiling herbs.", "inv/bottle.extract.png", 550, recipe=[[water,1],[herb018,1]], containers=[])
    
    $ herb_oil001 = Item("Thistle Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb001,1]], containers=[])
    $ herb_oil002 = Item("Dandelion Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb002,1]], containers=[])
    $ herb_oil003 = Item("Blackberry Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb003,1]], containers=[])
    $ herb_oil004 = Item("Oak Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb004,1]], containers=[])
    $ herb_oil005 = Item("Garlic Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb005,1]], containers=[])
    $ herb_oil006 = Item("Mint Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb006,1]], containers=[])
    $ herb_oil007 = Item("Oregano Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb007,1]], containers=[])
    $ herb_oil008 = Item("Parsley Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb008,1]], containers=[])
    $ herb_oil009 = Item("Sage Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb009,1]], containers=[])
    $ herb_oil010 = Item("Laurel Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb010,1]], containers=[])
    $ herb_oil011 = Item("Hyssop Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb011,1]], containers=[])
    $ herb_oil012 = Item("Barage Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb012,1]], containers=[])
    $ herb_oil013 = Item("Crown Flower Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb013,1]], containers=[])
    $ herb_oil014 = Item("Marsh Marigold Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb014,1]], containers=[])
    $ herb_oil015 = Item("Plantain Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb015,1]], containers=[])
    $ herb_oil016 = Item("Chamomile Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb016,1]], containers=[])
    $ herb_oil017 = Item("Calendula Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb017,1]], containers=[])
    $ herb_oil018 = Item("Violet Oil", "Made by soaking herbs in oil.", "inv/bottle.extract.png", 800, recipe=[[oil,1],[herb018,1]], containers=[])
 
 #Tier 3 Items

    $ balm001 = Item("Thistle Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil001,1]], containers=[[empty_bottle,1]])
    $ balm002 = Item("Dandelion Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil002,1]], containers=[[empty_bottle,1]])
    $ balm003 = Item("Blackberry Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil003,1]], containers=[[empty_bottle,1]])
    $ balm004 = Item("Oak Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil004,1]], containers=[[empty_bottle,1]])
    $ balm005 = Item("Garlic Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil005,1]], containers=[[empty_bottle,1]])
    $ balm006 = Item("Mint Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil006,1]], containers=[[empty_bottle,1]])
    $ balm007 = Item("Oregano Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil007,1]], containers=[[empty_bottle,1]])
    $ balm008 = Item("Parsley Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil008,1]], containers=[[empty_bottle,1]])
    $ balm009 = Item("Sage Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil009,1]], containers=[[empty_bottle,1]])
    $ balm010 = Item("Laurel Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil010,1]], containers=[[empty_bottle,1]])
    $ balm011 = Item("Hyssop Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil011,1]], containers=[[empty_bottle,1]])
    $ balm012 = Item("Barage Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil012,1]], containers=[[empty_bottle,1]])
    $ balm013 = Item("Crown Flower Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil013,1]], containers=[[empty_bottle,1]])
    $ balm014 = Item("Marsh Marigold Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil014,1]], containers=[[empty_bottle,1]])
    $ balm015 = Item("Plantain Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil015,1]], containers=[[empty_bottle,1]])
    $ balm016 = Item("Chamomile Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil016,1]], containers=[[empty_bottle,1]])
    $ balm017 = Item("Calendula Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil017,1]], containers=[[empty_bottle,1]])
    $ balm018 = Item("Violet Balm", "Medicine applied to the skin.", "inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil018,1]], containers=[[empty_bottle,1]])

    $ cream001 = Item("Thistle Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil001,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream002 = Item("Dandelion Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil002,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream003 = Item("Blackberry Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil003,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream004 = Item("Oak Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil004,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream005 = Item("Garlic Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil005,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream006 = Item("Mint Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil006,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream007 = Item("Oregano Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil007,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream008 = Item("Parsley Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil008,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream009 = Item("Sage Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil009,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream010 = Item("Laurel Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil010,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream011 = Item("Hyssop Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil011,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream012 = Item("Barage Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil012,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream013 = Item("Crown Flower Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil013,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream014 = Item("Marsh Marigold Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil014,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream014 = Item("Plantain Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil015,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream014 = Item("Chamomile Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil016,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream014 = Item("Calendula Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil017,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ cream014 = Item("Violet Cream", "Medicine applied to the skin.", "inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil018,1]], containers=[[empty_bottle,3], [empty_tin,1]])

    $ infusion001 = Item("Thistle Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract001,1]], containers=[[empty_bottle,1]])
    $ infusion002 = Item("Dandelion Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract002,1]], containers=[[empty_bottle,1]])
    $ infusion003 = Item("Blackberry Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract003,1]], containers=[[empty_bottle,1]])
    $ infusion004 = Item("Oak Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract004,1]], containers=[[empty_bottle,1]])
    $ infusion005 = Item("Garlic Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract005,1]], containers=[[empty_bottle,1]])
    $ infusion006 = Item("Mint Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract006,1]], containers=[[empty_bottle,1]])
    $ infusion007 = Item("Oregano Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract007,1]], containers=[[empty_bottle,1]])
    $ infusion008 = Item("Parsley Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract008,1]], containers=[[empty_bottle,1]])
    $ infusion009 = Item("Sage Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract009,1]], containers=[[empty_bottle,1]])
    $ infusion010 = Item("Laurel Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract010,1]], containers=[[empty_bottle,1]])
    $ infusion011 = Item("Hyssop Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract011,1]], containers=[[empty_bottle,1]])
    $ infusion012 = Item("Barage Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract012,1]], containers=[[empty_bottle,1]])
    $ infusion013 = Item("Crown Flower Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract013,1]], containers=[[empty_bottle,1]])
    $ infusion014 = Item("Marsh Marigold Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract014,1]], containers=[[empty_bottle,1]])
    $ infusion015 = Item("Plantain Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract015,1]], containers=[[empty_bottle,1]])
    $ infusion016 = Item("Chamomile Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract016,1]], containers=[[empty_bottle,1]])
    $ infusion017 = Item("Calendula Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract017,1]], containers=[[empty_bottle,1]])
    $ infusion018 = Item("Violet Infusion", "Medicine you can drink.", "inv/bottle.medicine01.png", 1200, recipe=[[water,1],[extract018,1]], containers=[[empty_bottle,1]])
    
    $ salve001 = Item("Thistle Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil001,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve002 = Item("Dandelion Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil002,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve003 = Item("Blackberry Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil003,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve004 = Item("Oak Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil004,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve005 = Item("Garlic Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil005,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve006 = Item("Mint Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil006,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve007 = Item("Oregano Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil007,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve008 = Item("Parsley Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil008,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve009 = Item("Sage Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil009,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve010 = Item("Laurel Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil010,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve011 = Item("Hyssop Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil011,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve012 = Item("Barage Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil012,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve013 = Item("Crown Flower Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil013,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve014 = Item("Marsh Marigold Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil014,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve015 = Item("Plantain Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil015,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve016 = Item("Chamomile Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil016,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve017 = Item("Calendula Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil017,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve018 = Item("Violet Salve", "Medicine applied to the skin.", "inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil018,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    
    $ tincture001 = Item("Thistle Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract001,1]], containers=[[empty_bottle,1]])
    $ tincture002 = Item("Dandelion Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract002,1]], containers=[[empty_bottle,1]])
    $ tincture003 = Item("Blackberry Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract003,1]], containers=[[empty_bottle,1]])
    $ tincture004 = Item("Oak Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract004,1]], containers=[[empty_bottle,1]])
    $ tincture005 = Item("Garlic Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract005,1]], containers=[[empty_bottle,1]])
    $ tincture006 = Item("Mint Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract006,1]], containers=[[empty_bottle,1]])
    $ tincture007 = Item("Oregano Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract007,1]], containers=[[empty_bottle,1]])
    $ tincture008 = Item("Parsley Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract008,1]], containers=[[empty_bottle,1]])
    $ tincture009 = Item("Sage Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract009,1]], containers=[[empty_bottle,1]])
    $ tincture010 = Item("Laurel Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract010,1]], containers=[[empty_bottle,1]])
    $ tincture011 = Item("Hyssop Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract011,1]], containers=[[empty_bottle,1]])
    $ tincture012 = Item("Barage Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract012,1]], containers=[[empty_bottle,1]])
    $ tincture013 = Item("Crown Flower Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract013,1]], containers=[[empty_bottle,1]])
    $ tincture014 = Item("Marsh Marigold Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract014,1]], containers=[[empty_bottle,1]])
    $ tincture015 = Item("Plantain Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract015,1]], containers=[[empty_bottle,1]])
    $ tincture016 = Item("Chamomile Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract016,1]], containers=[[empty_bottle,1]])
    $ tincture017 = Item("Calendula Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract017,1]], containers=[[empty_bottle,1]])
    $ tincture018 = Item("Violet Tincture", "Medicine you can drink.", "inv/bottle.medicine02.png", 1500, recipe=[[wine,1],[extract018,1]], containers=[[empty_bottle,1]])
    
    #"Items have been defined."
    
    $ cooklist = [balm001,cream002,extract003,herb_oil004,infusion005,salve006,tincture007]
    
    $ extractslist = [extract001,extract002,extract003,extract004,extract005,extract006,extract007,extract008,extract009,extract010,extract011,extract012,extract013,extract014]
    $ herboilslist = [herb_oil001,herb_oil002,herb_oil003,herb_oil004,herb_oil005,herb_oil006,herb_oil007,herb_oil008,herb_oil009,herb_oil010,herb_oil011,herb_oil012,herb_oil013,herb_oil014]

    $ balmslist = [balm001,balm002,balm003,balm004,balm005,balm006,balm007,balm008,balm009,balm010,balm011,balm012,balm013,balm014]
    $ creamslist = [cream001,cream002,cream003,cream004,cream005,cream006,cream007,cream008,cream009,cream010,cream011,cream012,cream013,cream014]
    $ infusionslist = [infusion001,infusion002,infusion003,infusion004,infusion005,infusion006,infusion007,infusion008,infusion009,infusion010,infusion011,infusion012,infusion013,infusion014]
    $ salveslist = [salve001,salve002,salve003,salve004,salve005,salve006,salve007,salve008,salve009,salve010,salve011,salve012,salve013,salve014]
    $ tinctureslist = [tincture001,tincture002,tincture003,tincture004,tincture005,tincture006,tincture007,tincture008,tincture009,tincture010,tincture011,tincture012,tincture013,tincture014]
    
    return 
    
    