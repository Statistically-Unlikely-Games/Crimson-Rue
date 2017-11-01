label define_items:
    #"Encyclopaedia Actions have been imported."
    
    ######### DEFINE ITEM OBJECTS ##########
    ### The format is name, description, icon image (if applicable), value (if applicable, selling/buying value), action (screen language action to be performed when icon is clicked on inventory screen), and recipe (if craftable).
    
    ### Items without icons are created like this:      
    #$ quarter = Item("Quarter", "A new quarter)
    
    ### Items with icons are created like this:
#    $ eye = Item(name="Eyeball", desc="A human eyeball, how creepy!", icon="gui/inv/eye.png", value=250)

    # Items that can be used in crafting
#    $ but = Item("Button", "A shiny button", "gui/inv/button.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
#    $ yarn = Item("Yarn", "Yarny yarny yarn.", "gui/inv/yarn.png", 30, act=Show("inventory_popup", message="This item is only used in crafting"))  
#    $ fabric = Item("Fabric", "You know, cloth.", "gui/inv/fabric.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
#    $ coin = Item("Coin", "An old coin", "gui/inv/coin.png", 1, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    # An item with a unique action (shows screen with custom message)
#    $ sword = Item("Awesome Sword", "An awesome sword.", "gui/inv/sword.png", 500, Show("inventory_popup", message="You wave the sword around wildly but nothing happens."))

    # An item that can be crafted has a recipe, which is a nested list of [ingredient, qty]
#    $ necklace = Item("Penny Necklace", "Super magic.", "gui/inv/necklace.png", 50, recipe=[[coin,6],[yarn,1]])    
#    $ doll = Item("Handmade Doll", "Guaranteed to bring luck. (Or not?) Very huggable, mind the needle.", "gui/inv/doll.png", 100000, recipe=[[but,2],[fabric,3],[yarn,1]]) 


#Books 
    
    #These books, for some reason, will only cause time to pass the *very first* book you click. After that, they do nothing...
    
    $ herbID1 = Item("Herb Identification vol. 1", "A book of herbs", "gui/inv/book.png", 5000, act=[AddBook(book_2), Show("inventory_popup", message="New Herbs Unlocked"), SetVariable('herb_book1',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ herbID2 = Item("Herb Identification vol. 2", "A book of herbs", "gui/inv/book.png", 5000, act=[AddBook(book_3), Show("inventory_popup", message="New Herbs Unlocked"), SetVariable('herb_book2',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ herbID3 = Item("Herb Identification vol. 3", "A book of herbs", "gui/inv/book.png", 5000, act=[AddBook(book_4), Show("inventory_popup", message="New Herbs Unlocked"), SetVariable('herb_book3',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    
    $ medJNL1 = Item("Medical Journal vol. 1", "A book of medical symptoms", "gui/inv/book.png", 5000, act=[AddBook(book_5), Show("inventory_popup", message="New Journal Unlocked"), SetVariable('med_book1',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ medJNL2 = Item("Medical Journal vol. 2", "A book of medical symptoms", "gui/inv/book.png", 5000, act=[AddBook(book_6), Show("inventory_popup", message="New Journal Unlocked"), SetVariable('med_book2',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ medJNL3 = Item("Medical Journal vol. 3", "A book of medical symptoms", "gui/inv/book.png", 5000, act=[AddBook(book_7), Show("inventory_popup", message="New Journal Unlocked"), SetVariable('med_book3',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ medJNL4 = Item("Medical Journal vol. 4", "A book of medical symptoms", "gui/inv/book.png", 5000, act=[AddBook(book_8), Show("inventory_popup", message="New Journal Unlocked"), SetVariable('med_book4',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ medJNL5 = Item("Medical Journal vol. 5", "A book of medical symptoms", "gui/inv/book.png", 5000, act=[AddBook(book_9), Show("inventory_popup", message="New Journal Unlocked"), SetVariable('med_book5',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])
    $ medJNL6 = Item("Medical Journal vol. 6", "A book of medical symptoms", "gui/inv/book.png", 5000, act=[AddBook(book_10), Show("inventory_popup", message="New Journal Unlocked"), SetVariable('med_book6',True), SetVariable('time_cnt',time_cnt+1), Function(renpy.call, "time_img")])

#Tier 1 Items
    
    $ herb001 = Item("Thistle", "A medicinal herb. Seeds are best collected when the flowers have dried out, generally starting in early fall.", "gui/inv/herb001_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb002 = Item("Dandelion", "A medicinal herb. Roots are best harvested in late fall to early spring. Collect from large, vigorous plants.", "gui/inv/herb002_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb003 = Item("Blackberry", "A medicinal herb.", "gui/inv/herb003_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb004 = Item("Oak", "A medicinal herb.", "gui/inv/herb004_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb005 = Item("Garlic", "A medicinal herb.", "gui/inv/herb005_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb006 = Item("Mint", "A medicinal herb.", "gui/inv/herb006_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb007 = Item("Oregano", "A medicinal herb.", "gui/inv/herb007_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb008 = Item("Parsley", "A medicinal herb.", "gui/inv/herb008_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb009 = Item("Sage", "A medicinal herb.", "gui/inv/herb009_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb010 = Item("Laurel", "A medicinal herb.", "gui/inv/herb010_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb011 = Item("Hyssop", "A medicinal herb.", "gui/inv/herb011_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb012 = Item("Borage", "A medicinal herb.", "gui/inv/herb012_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb013 = Item("Crown Flower", "A medicinal herb.", "gui/inv/herb013_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb014 = Item("Marsh Marigold", "A medicinal herb.", "gui/inv/herb014_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb015 = Item("Plantain", "A medicinal herb.", "gui/inv/herb015_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb016 = Item("Chamomile", "A medicinal herb.", "gui/inv/herb016_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb017 = Item("Calendula", "A medicinal herb.", "gui/inv/herb017_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb018 = Item("Violet", "A medicinal herb.", "gui/inv/herb018_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb019 = Item("Rosemary", "A medicinal herb.", "gui/inv/herb019_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb020 = Item("Basil", "A medicinal herb.", "gui/inv/herb020_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb021 = Item("Poppy", "A medicinal herb.", "gui/inv/herb021_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb022 = Item("Mullein", "A medicinal herb.", "gui/inv/herb022_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb023 = Item("Red Clover", "A medicinal herb.", "gui/inv/herb023_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb024 = Item("St. John's Wort", "A medicinal herb.", "gui/inv/herb024_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb025 = Item("Yellow Dock", "A medicinal herb.", "gui/inv/herb025_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb026 = Item("Burdock", "A plant whose seeds and roots have medicinal properties. Rarely, the leaves are also used. Can be processed to treat various skin conditions and to promote liver function.", "gui/inv/herb026_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb027 = Item("Comfrey", "A plant whose leaves and roots have medicinal properties. The roots are more potent, but the leaves are more palatable. Can be processed to treat inflammation and promote healing.", "gui/inv/herb027_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb028 = Item("Goldenseal", "A plant whose bright yellow roots have medicinal properties. Best harvested in the fall, choosing older plants whose leaves have started to die off. Act as a strong anti-bacterial and can be processed to treat indigestion.", "gui/inv/herb028_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb029 = Item("Lemon Balm", "A plant whose leaves and flowers have medicinal properties. Can be processed to treat stress and anxiety, irritated stomaches, and mild insomnia. Has a strong lemony aroma.", "gui/inv/herb029_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ herb030 = Item("Licorice", "A plant whose roots have medicinal properties. Can be processed to treat fatigue and respiratory inflammation.", "gui/inv/herb030_idle.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))

    $ bandages = Item("Bandages", "For wrapping wounds.", "gui/inv/bandages.png", 5, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ cheesecloth = Item("Cheesecloth", "Often used for straining.", "gui/inv/bandages.png", 5, act=Show("inventory_popup", message="This item is only used in crafting"))

    $ empty_bottle = Item("Empty Bottle", "Fill it with all kinds of things.", "gui/inv/bottle.empty.png", 300, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ water = Item("Bottle of Water", "Medicine made with this spread easy but spoil faster.", "gui/inv/bottle.water.png", 300, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ oil = Item("Bottle of Oil", "Medicine made with this lasts a long time.", "gui/inv/bottle.oil.png", 500, act=Show("inventory_popup", message="This item is only used in crafting"))
#    $ refined_oil
    $ vodka = Item("Bottle of Vodka", "Useful in makeing tinctures.", "gui/inv/bottle.vodka.png", 500, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    $ empty_tin = Item("Empty Tin", "An empty tin.", "gui/inv/tin.empty.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ wax = Item("Beeswax", "Useful in combining water based extracts with oil.", "gui/inv/tin.wax.png", 200, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    $ empty_jar = Item("Empty Jar", "An empty jar.", "gui/inv/jar.empty.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    $ honey = Item("Jar of Honey", "An empty jar.", "gui/inv/jar.honey.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    
#Tier 2 Items
    
    $ dried_herb001 = Item("Dried Thistle", "A dried medicinal herb.", "gui/inv/herb001_idle.png", 200, recipe=[[herb001,1]], containers=[])
    $ dried_herb002 = Item("Dried Dandelion", "A dried medicinal herb.", "gui/inv/herb002_idle.png", 200, recipe=[[herb002,1]], containers=[])
    $ dried_herb003 = Item("Dried Blackberry", "A dried medicinal herb.", "gui/inv/herb003_idle.png", 200, recipe=[[herb003,1]], containers=[])
    $ dried_herb004 = Item("Dried Oak", "A dried medicinal herb.", "gui/inv/herb004_idle.png", 200, recipe=[[herb004,1]], containers=[])
    $ dried_herb005 = Item("Dried Garlic", "A dried medicinal herb.", "gui/inv/herb005_idle.png", 200, recipe=[[herb005,1]], containers=[])
    $ dried_herb006 = Item("Dried Mint", "A dried medicinal herb.", "gui/inv/herb006_idle.png", 200, recipe=[[herb006,1]], containers=[])
    $ dried_herb007 = Item("Dried Oregano", "A dried medicinal herb.", "gui/inv/herb007_idle.png", 200, recipe=[[herb007,1]], containers=[])
    $ dried_herb008 = Item("Dried Parsley", "A dried medicinal herb.", "gui/inv/herb008_idle.png", 200, recipe=[[herb008,1]], containers=[])
    $ dried_herb009 = Item("Dried Sage", "A dried medicinal herb.", "gui/inv/herb009_idle.png", 200, recipe=[[herb009,1]], containers=[])
    $ dried_herb010 = Item("Dried Laurel", "A dried medicinal herb.", "gui/inv/herb010_idle.png", 200, recipe=[[herb010,1]], containers=[])
    $ dried_herb011 = Item("Dried Hyssop", "A dried medicinal herb.", "gui/inv/herb011_idle.png", 200, recipe=[[herb011,1]], containers=[])
    $ dried_herb012 = Item("Dried Borage", "A dried medicinal herb.", "gui/inv/herb012_idle.png", 200, recipe=[[herb012,1]], containers=[])
    $ dried_herb013 = Item("Dried Crown Flower", "A dried medicinal herb.", "gui/inv/herb013_idle.png", 200, recipe=[[herb013,1]], containers=[])
    $ dried_herb014 = Item("Dried Marsh Marigold", "A dried medicinal herb.", "gui/inv/herb014_idle.png", 200, recipe=[[herb014,1]], containers=[])
    $ dried_herb015 = Item("Dried Plantain", "A dried medicinal herb.", "gui/inv/herb015_idle.png", 200, recipe=[[herb015,1]], containers=[])  
    $ dried_herb016 = Item("Dried Chamomile", "A dried medicinal herb.", "gui/inv/herb016_idle.png", 200, recipe=[[herb016,1]], containers=[])
    $ dried_herb017 = Item("Dried Calendula", "A dried medicinal herb.", "gui/inv/herb017_idle.png", 200, recipe=[[herb017,1]], containers=[])
    $ dried_herb018 = Item("Dried Violet", "A dried medicinal herb.", "gui/inv/herb018_idle.png", 200, recipe=[[herb018,1]], containers=[])
    $ dried_herb019 = Item("Dried Rosemary", "A dried medicinal herb.", "gui/inv/herb019_idle.png", 200, recipe=[[herb019,1]], containers=[])
    $ dried_herb020 = Item("Dried Basil", "A dried medicinal herb.", "gui/inv/herb020_idle.png", 200, recipe=[[herb020,1]], containers=[])
    $ dried_herb021 = Item("Dried Poppy", "A dried medicinal herb.", "gui/inv/herb021_idle.png", 200, recipe=[[herb021,1]], containers=[])
    $ dried_herb022 = Item("Dried Mullein", "A dried medicinal herb.", "gui/inv/herb022_idle.png", 200, recipe=[[herb022,1]], containers=[])
    $ dried_herb023 = Item("Dried Red Clover", "A dried medicinal herb.", "gui/inv/herb023_idle.png", 200, recipe=[[herb023,1]], containers=[])
    $ dried_herb024 = Item("Dried St. John's Wort", "A dried medicinal herb.", "gui/inv/herb024_idle.png", 200, recipe=[[herb024,1]], containers=[])
    $ dried_herb025 = Item("Dried Yellow Dock", "A dried medicinal herb.", "gui/inv/herb025_idle.png", 200, recipe=[[herb025,1]], containers=[])
    $ dried_herb026 = Item("Dried Burdock", "A dried medicinal herb.", "gui/inv/herb026_idle.png", 200, recipe=[[herb026,1]], containers=[])
    $ dried_herb027 = Item("Dried Comfrey", "A dried medicinal herb. Can be infused to make tinctures or tea, as well as processed into a powder.", "gui/inv/herb027_idle.png", 200, recipe=[[herb027,1]], containers=[])
    $ dried_herb028 = Item("Dried Goldenseal", "Dried goldenseal root. Can be infused to make tinctures or tea, as well as processed into a powder.", "gui/inv/herb028_idle.png", 200, recipe=[[herb028,1]], containers=[])
#    $ dried_herb029 = Item("Dried Lemon Balm", "A dried medicinal herb.", "gui/inv/herb029_idle.png", 200, recipe=[[herb029,1]], containers=[])
    $ dried_herb030 = Item("Dried Licorice", "Dried licorice root. Can be infused to make tea or processed into a powder.", "gui/inv/herb030_idle.png", 200, recipe=[[herb030,1]], containers=[]) #Generally baked to dry
    
    $ herb_oil001 = Item("Thistle Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb001,1]], containers=[])
    $ herb_oil002 = Item("Dandelion Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb002,1]], containers=[])
    $ herb_oil003 = Item("Blackberry Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb003,1]], containers=[])
    $ herb_oil004 = Item("Oak Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb004,1]], containers=[])
    $ herb_oil005 = Item("Garlic Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb005,1]], containers=[])
    $ herb_oil006 = Item("Mint Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb006,1]], containers=[])
    $ herb_oil007 = Item("Oregano Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb007,1]], containers=[])
    $ herb_oil008 = Item("Parsley Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb008,1]], containers=[])
    $ herb_oil009 = Item("Sage Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb009,1]], containers=[])
    $ herb_oil010 = Item("Laurel Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb010,1]], containers=[])
    $ herb_oil011 = Item("Hyssop Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb011,1]], containers=[])
    $ herb_oil012 = Item("Borage Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb012,1]], containers=[])
    $ herb_oil013 = Item("Crown Flower Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb013,1]], containers=[])
    $ herb_oil014 = Item("Marsh Marigold Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb014,1]], containers=[])
    $ herb_oil015 = Item("Plantain Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb015,1]], containers=[])
    $ herb_oil016 = Item("Chamomile Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb016,1]], containers=[])
    $ herb_oil017 = Item("Calendula Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb017,1]], containers=[])
    $ herb_oil018 = Item("Violet Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb018,1]], containers=[])
    $ herb_oil019 = Item("Rosemary Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb019,1]], containers=[])
    $ herb_oil020 = Item("Basil Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb020,1]], containers=[])
    $ herb_oil021 = Item("Poppy Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb021,1]], containers=[])
    $ herb_oil022 = Item("Mullein Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb022,1]], containers=[])
    $ herb_oil023 = Item("Red Clover Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb023,1]], containers=[])
    $ herb_oil024 = Item("St. John's Wort Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb024,1]], containers=[])
    $ herb_oil025 = Item("Yellow Dock Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb025,1]], containers=[])
    $ herb_oil026 = Item("Burdock Oil", "Made by soaking burdock leaves or seeds in oil.Can be processed into medicine.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb026,1]], containers=[])
    $ herb_oil027 = Item("Comfrey Oil", "Made by soaking comfrey leaves in oil. Can be processed into medicine.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb027,1]], containers=[])
    $ herb_oil028 = Item("Goldenseal Oil", "Made by soaking goldenseal root in oil. Can be processed into medicine.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb028,1]], containers=[])
    $ herb_oil029 = Item("Lemon Balm Oil", "Made by soaking lemon balm leaves in oil. May be added to edible dishes for flavor or processed into medicine.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb029,1]], containers=[])
#    $ herb_oil030 = Item("Licorice Oil", "Made by soaking herbs in oil.", "gui/inv/bottle.extract.png", 800, recipe=[[oil,1],[herb030,1]], containers=[])
    
    $ paste015 = Item("Plantain Paste", "A paste made from mashing herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[herb015,1]], containers=[])
    
    $ tincture001 = Item("Thistle Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb001,1]], containers=[[empty_bottle,1]])
    $ tincture002 = Item("Dandelion Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb002,1]], containers=[[empty_bottle,1]])
    $ tincture003 = Item("Blackberry Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb003,1]], containers=[[empty_bottle,1]])
    $ tincture004 = Item("Oak Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb004,1]], containers=[[empty_bottle,1]])
    $ tincture005 = Item("Garlic Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb005,1]], containers=[[empty_bottle,1]])
    $ tincture006 = Item("Mint Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb006,1]], containers=[[empty_bottle,1]])
    $ tincture007 = Item("Oregano Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb007,1]], containers=[[empty_bottle,1]])
    $ tincture008 = Item("Parsley Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb008,1]], containers=[[empty_bottle,1]])
    $ tincture009 = Item("Sage Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb009,1]], containers=[[empty_bottle,1]])
    $ tincture010 = Item("Laurel Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb010,1]], containers=[[empty_bottle,1]])
    $ tincture011 = Item("Hyssop Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb011,1]], containers=[[empty_bottle,1]])
    $ tincture012 = Item("Borage Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb012,1]], containers=[[empty_bottle,1]])
    $ tincture013 = Item("Crown Flower Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb013,1]], containers=[[empty_bottle,1]])
    $ tincture014 = Item("Marsh Marigold Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb014,1]], containers=[[empty_bottle,1]])
    $ tincture015 = Item("Plantain Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb015,1]], containers=[[empty_bottle,1]])
    $ tincture016 = Item("Chamomile Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb016,1]], containers=[[empty_bottle,1]])
    $ tincture017 = Item("Calendula Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb017,1]], containers=[[empty_bottle,1]])
    $ tincture018 = Item("Violet Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb018,1]], containers=[[empty_bottle,1]])
    $ tincture019 = Item("Rosemary Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb019,1]], containers=[[empty_bottle,1]])
    $ tincture020 = Item("Basil Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb020,1]], containers=[[empty_bottle,1]])
    $ tincture021 = Item("Poppy Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb021,1]], containers=[[empty_bottle,1]])
    $ tincture022 = Item("Mullein Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb022,1]], containers=[[empty_bottle,1]])
    $ tincture023 = Item("Red Clover Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb023,1]], containers=[[empty_bottle,1]])
    $ tincture024 = Item("St. John's Wort Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb024,1]], containers=[[empty_bottle,1]])
    $ tincture025 = Item("Yellow Dock Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb025,1]], containers=[[empty_bottle,1]])
    $ tincture026 = Item("Burdock Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb026,1]], containers=[[empty_bottle,1]])
    $ tincture027 = Item("Comfrey Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb027,1]], containers=[[empty_bottle,1]])
    $ tincture028 = Item("Goldenseal Tincture", "A strong medicine made by soaking goldenseal root in alcohol. Often diluted and used as a mouth or eye wash to treat infections.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb028,1]], containers=[[empty_bottle,1]])
    $ tincture029 = Item("Lemon Balm Tincture", "A strong medicine made by soaking lemon balm in alcohol. Commonly used to treat irritated stomachs and mild insomnia.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb029,1]], containers=[[empty_bottle,1]])
#    $ tincture030 = Item("Licorice Tincture", "Medicine you can drink.", "gui/inv/bottle.medicine02.png", 1500, recipe=[[vodka,1],[herb030,1]], containers=[[empty_bottle,1]])
    
    
#Tier 3 Items
    
    $ balm001 = Item("Thistle Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil001,1]], containers=[[empty_bottle,1]])
    $ balm002 = Item("Dandelion Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil002,1]], containers=[[empty_bottle,1]])
    $ balm003 = Item("Blackberry Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil003,1]], containers=[[empty_bottle,1]])
    $ balm004 = Item("Oak Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil004,1]], containers=[[empty_bottle,1]])
    $ balm005 = Item("Garlic Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil005,1]], containers=[[empty_bottle,1]])
    $ balm006 = Item("Mint Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil006,1]], containers=[[empty_bottle,1]])
    $ balm007 = Item("Oregano Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil007,1]], containers=[[empty_bottle,1]])
    $ balm008 = Item("Parsley Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil008,1]], containers=[[empty_bottle,1]])
    $ balm009 = Item("Sage Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil009,1]], containers=[[empty_bottle,1]])
#    $ balm010 = Item("Laurel Balm", "Medicine applied to the skin.", "gui/inv/tin.medicine05.png", 1400, recipe=[[wax,1],[herb_oil010,1]], containers=[[empty_bottle,1]])
    
    $ cream029 = Item("Lemon Balm Cream", "Medicine made from lemon balm, it is applied externally. Often used to soothe herpes sores.", "gui/inv/jar.medicine04.png", 2400, recipe=[[empty_jar,1],[water,2],[wax,1],[herb_oil029,1]], containers=[[empty_bottle,3], [empty_tin,1]])

#    $ essential_oil001
    
    $ infusion001 = Item("Thistle Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb001,1]], containers=[])
    $ infusion002 = Item("Dandelion Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb002,1]], containers=[])
    $ infusion003 = Item("Blackberry Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb003,1]], containers=[])
    $ infusion004 = Item("Oak Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb004,1]], containers=[])
    $ infusion005 = Item("Garlic Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb005,1]], containers=[])
    $ infusion006 = Item("Mint Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb006,1]], containers=[])
    $ infusion007 = Item("Oregano Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb007,1]], containers=[])
    $ infusion008 = Item("Parsley Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb008,1]], containers=[])
    $ infusion009 = Item("Sage Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb009,1]], containers=[])
    $ infusion010 = Item("Laurel Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb010,1]], containers=[])
    $ infusion011 = Item("Hyssop Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb011,1]], containers=[])
    $ infusion012 = Item("Borage Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb012,1]], containers=[])
    $ infusion013 = Item("Crown Flower Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb013,1]], containers=[])
    $ infusion014 = Item("Marsh Marigold Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb014,1]], containers=[])
    $ infusion015 = Item("Plantain Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb015,1]], containers=[])
    $ infusion016 = Item("Chamomile Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb016,1]], containers=[])
    $ infusion017 = Item("Calendula Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb017,1]], containers=[])
    $ infusion018 = Item("Violet Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb018,1]], containers=[])
    $ infusion019 = Item("Rosemary Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb019,1]], containers=[])
    $ infusion020 = Item("Basil Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb020,1]], containers=[])
    $ infusion021 = Item("Poppy Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb021,1]], containers=[])
    $ infusion022 = Item("Mullein Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb022,1]], containers=[])
    $ infusion023 = Item("Red Clover Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb023,1]], containers=[])
    $ infusion024 = Item("St. John's Wort Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb024,1]], containers=[])
    $ infusion025 = Item("Yellow Dock Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb025,1]], containers=[])
    $ infusion026 = Item("Burdock Infusion", "A medicinal tea made by boiling herbs.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb026,1]], containers=[])
    $ infusion027 = Item("Comfrey Infusion", "A medicinal tea made by boiling comfrey leaves. Helps calm inflammation and promote healing.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb027,1]], containers=[])
    $ infusion028 = Item("Goldenseal Infusion", "A medicinal tea made by boiling goldenseal root. Used as a digestive aid. Has a strong, bitter flavor.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[herb028,1]], containers=[])
    $ infusion029 = Item("Lemon Balm Infusion", "A medicinal tea made by boiling the leaves, and sometimes flowers, of the lemon balm plant. Helps alleviate stress and anxiety. True to its name, has a distinct lemony flavor.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[herb029,1]], containers=[])
    $ infusion030 = Item("Licorice Infusion", "A medicinal tea made by boiling licorice root. Used to treat fatigue. Has a very sweet flavor.", "gui/inv/bottle.medicine01.png", 550, recipe=[[water,1],[dried_herb030,1]], containers=[])
    
    $ poultice015 = Item("Plantain Poultice", "Spread on wounds to promote healing.", "gui/inv/bandages.png", 550, recipe=[[bandages,1],[paste015,1]], containers=[])
    
    $ powdered_herb001 = Item("Powdered Thistle", "A powdered medicinal herb.", "gui/inv/herb001_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb001,1]], containers=[])
    $ powdered_herb002 = Item("Powdered Dandelion", "A powdered medicinal herb.", "gui/inv/herb002_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb002,1]], containers=[])
    $ powdered_herb003 = Item("Powdered Blackberry", "A powdered medicinal herb.", "gui/inv/herb003_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb003,1]], containers=[])
    $ powdered_herb004 = Item("Powdered Oak", "A powdered medicinal herb.", "gui/inv/herb004_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb004,1]], containers=[])
    $ powdered_herb005 = Item("Powdered Garlic", "A powdered medicinal herb.", "gui/inv/herb005_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb005,1]], containers=[])
    $ powdered_herb006 = Item("Powdered Mint", "A powdered medicinal herb.", "gui/inv/herb006_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb006,1]], containers=[])
    $ powdered_herb007 = Item("Powdered Oregano", "A powdered medicinal herb.", "gui/inv/herb007_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb007,1]], containers=[])
    $ powdered_herb008 = Item("Powdered Parsley", "A powdered medicinal herb.", "gui/inv/herb008_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb008,1]], containers=[])
    $ powdered_herb009 = Item("Powdered Sage", "A powdered medicinal herb.", "gui/inv/herb009_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb009,1]], containers=[])
    $ powdered_herb010 = Item("Powdered Laurel", "A powdered medicinal herb.", "gui/inv/herb010_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb010,1]], containers=[])
    $ powdered_herb011 = Item("Powdered Hyssop", "A powdered medicinal herb.", "gui/inv/herb011_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb011,1]], containers=[])
    $ powdered_herb012 = Item("Powdered Borage", "A powdered medicinal herb.", "gui/inv/herb012_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb012,1]], containers=[])
    $ powdered_herb013 = Item("Powdered Crown Flower", "A powdered medicinal herb.", "gui/inv/herb013_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb013,1]], containers=[])
    $ powdered_herb014 = Item("Powdered Marsh Marigold", "A powdered medicinal herb.", "gui/inv/herb014_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb014,1]], containers=[])
    $ powdered_herb015 = Item("Powdered Plantain", "A powdered medicinal herb.", "gui/inv/herb015_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb015,1]], containers=[])
    $ powdered_herb016 = Item("Powdered Chamomile", "A powdered medicinal herb.", "gui/inv/herb016_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb016,1]], containers=[])
    $ powdered_herb017 = Item("Powdered Calendula", "A powdered medicinal herb.", "gui/inv/herb017_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb017,1]], containers=[])
    $ powdered_herb018 = Item("Powdered Violet", "A powdered medicinal herb.", "gui/inv/herb018_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb018,1]], containers=[])
    $ powdered_herb019 = Item("Powdered Rosemary", "A powdered medicinal herb.", "gui/inv/herb019_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb019,1]], containers=[])
    $ powdered_herb020 = Item("Powdered Basil", "A powdered medicinal herb.", "gui/inv/herb020_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb020,1]], containers=[])
    $ powdered_herb021 = Item("Powdered Poppy", "A powdered medicinal herb.", "gui/inv/herb021_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb021,1]], containers=[])
    $ powdered_herb022 = Item("Powdered Mullein", "A powdered medicinal herb.", "gui/inv/herb022_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb022,1]], containers=[])
    $ powdered_herb023 = Item("Powdered Red Clover", "A powdered medicinal herb.", "gui/inv/herb023_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb023,1]], containers=[])
    $ powdered_herb024 = Item("Powdered St. John's Wort", "A powdered medicinal herb.", "gui/inv/herb024_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb024,1]], containers=[])
    $ powdered_herb025 = Item("Powdered Yellow Dock", "A powdered medicinal herb.", "gui/inv/herb025_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb025,1]], containers=[])
    $ powdered_herb026 = Item("Powdered Burdock", "A powdered medicinal herb.", "gui/inv/herb026_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb026,1]], containers=[])
    $ powdered_herb027 = Item("Powdered Comfrey", "A powdered medicinal herb.", "gui/inv/herb027_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb027,1]], containers=[])
    $ powdered_herb028 = Item("Powdered Goldenseal", "Powdered goldenseal root. Often used in conjunction with other herbs due to its strong antibiotic properties.", "gui/inv/powder.medium.png", 300, recipe=[[empty_bottle,1],[dried_herb028,1]], containers=[])
#    $ powdered_herb029 = Item("Powdered Lemon Balm", "A powdered medicinal herb.", "gui/inv/herb029_idle.png", 300, recipe=[[empty_bottle,1],[dried_herb029,1]], containers=[])
    $ powdered_herb030 = Item("Powdered Licorice", "Powdered licorice root. Often added to pills in order to offest bad-tasting herbs.", "gui/inv/powder.coarse.png", 300, recipe=[[empty_bottle,1],[dried_herb030,1]], containers=[])
    
    $ mixed_powder_liver = Item("Liver Powder Mix", "Powdered thistle seeds, dandelion root, and burdock root. Generally processed into pills.", "gui/inv/powder.coarse.png", 300, recipe=[[empty_bottle,1],[dried_herb001,1],[dried_herb002,1],[dried_herb026,1]], containers=[])
    
    $ salve001 = Item("Thistle Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil001,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve002 = Item("Dandelion Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil002,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve003 = Item("Blackberry Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil003,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve004 = Item("Oak Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil004,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve005 = Item("Garlic Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil005,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve006 = Item("Mint Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil006,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve007 = Item("Oregano Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil007,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve008 = Item("Parsley Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil008,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve009 = Item("Sage Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil009,1]], containers=[[empty_bottle,3], [empty_tin,1]])
    $ salve010 = Item("Laurel Salve", "Medicine applied to the skin.", "gui/inv/jar.medicine03.png", 3000, recipe=[[empty_jar,1],[oil,2],[wax,1],[herb_oil010,1]], containers=[[empty_bottle,3], [empty_tin,1]])

    
 #Tier 4 Items
    
#    $ bath_blend001
    
    $ decoction001 = Item("Thistle Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion001,1]], containers=[])
    $ decoction002 = Item("Dandelion Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion002,1]], containers=[])
    $ decoction003 = Item("Blackberry Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion003,1]], containers=[])
    $ decoction004 = Item("Oak Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion004,1]], containers=[])
    $ decoction005 = Item("Garlic Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion005,1]], containers=[])
    $ decoction006 = Item("Mint Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion006,1]], containers=[])
    $ decoction007 = Item("Oregano Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion007,1]], containers=[])
    $ decoction008 = Item("Parsley Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion008,1]], containers=[])
    $ decoction009 = Item("Sage Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion009,1]], containers=[])
    $ decoction010 = Item("Laurel Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion010,1]], containers=[])
    $ decoction011 = Item("Hyssop Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion011,1]], containers=[])
    $ decoction012 = Item("Borage Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion012,1]], containers=[])
    $ decoction013 = Item("Crown Flower Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion013,1]], containers=[])
    $ decoction014 = Item("Marsh Marigold Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion014,1]], containers=[])
    $ decoction015 = Item("Plantain Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion015,1]], containers=[])
    $ decoction016 = Item("Chamomile Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion016,1]], containers=[])
    $ decoction017 = Item("Calendula Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion017,1]], containers=[])
    $ decoction018 = Item("Violet Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion018,1]], containers=[])
    $ decoction019 = Item("Rosemary Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion019,1]], containers=[])
    $ decoction020 = Item("Basil Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion020,1]], containers=[])
    $ decoction021 = Item("Poppy Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion021,1]], containers=[])
    $ decoction022 = Item("Mullein Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion022,1]], containers=[])
    $ decoction023 = Item("Red Clover Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion023,1]], containers=[])
    $ decoction024 = Item("St. John's Wort Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion024,1]], containers=[])
    $ decoction025 = Item("Yellow Dock Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion025,1]], containers=[])
    $ decoction026 = Item("Burdock Decoction", "Very concentrated liquid medicine made from burdock root.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion026,1]], containers=[])
    $ decoction027 = Item("Comfrey Decoction", "Very concentrated liquid medicine made from comfrey root. It calms inflammation and promotes healing.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion027,1]], containers=[])
    $ decoction028 = Item("Goldenseal Decoction", "Very concentrated liquid medicine made from the root of the goldenseal plant. Used to treat indigestion. Very bitter.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion028,1]], containers=[])
#    $ decoction029 = Item("Lemon Balm Decoction", "Very concentrated liquid medicine.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion029,1]], containers=[])
    $ decoction030 = Item("Licorice Decoction", "Very concentrated liquid medicine made from the root of the licorice plant. Often processed into a syrup to soothe sore throats and treat respiratory inflammation. It is extremely sweet, and thus usually used with other herbs.", "gui/inv/bottle.extract.png", 2000, recipe=[[infusion030,1]], containers=[])
    
#    $ compress001
    
#    $ perfume001
    
    $ pill001 = Item("Liver Pills", "Oral medicine taken to promote liver function.", "gui/inv/jar.medicine03.png", 2000, recipe=[[water,1],[honey,1],[mixed_powder_liver,1]], containers=[[empty_bottle,1]])
    
 #Tier 5 Items
    
#    $ syrup001
    
    #"Items have been defined."
    
    $ cook_list = [balm001,herb_oil004,infusion005,salve006,tincture007]
    
    $ driedherbs_list = [dried_herb001,dried_herb002,dried_herb003,dried_herb004,dried_herb005,dried_herb006,dried_herb007,dried_herb008,dried_herb009,dried_herb010,dried_herb011,dried_herb012,dried_herb013,dried_herb014,dried_herb015,dried_herb016,dried_herb017,dried_herb018,dried_herb019,dried_herb020,dried_herb021,dried_herb022,dried_herb023,dried_herb024,dried_herb025,dried_herb026,dried_herb027,dried_herb028,dried_herb030]
    $ herboils_list = [herb_oil001,herb_oil002,herb_oil003,herb_oil004,herb_oil005,herb_oil006,herb_oil007,herb_oil008,herb_oil009,herb_oil010,herb_oil011,herb_oil012,herb_oil013,herb_oil014,herb_oil015,herb_oil016,herb_oil017,herb_oil018,herb_oil019,herb_oil020,herb_oil021,herb_oil022,herb_oil023,herb_oil024,herb_oil025,herb_oil026,herb_oil027,herb_oil028,herb_oil029]
    $ pastes_list = [paste015]
    $ tinctures_list = [tincture001,tincture002,tincture003,tincture004,tincture005,tincture006,tincture007,tincture008,tincture009,tincture010,tincture011,tincture012,tincture013,tincture014,tincture015,tincture016,tincture017,tincture018,tincture019,tincture020,tincture021,tincture022,tincture023,tincture024,tincture025,tincture026,tincture027,tincture028,tincture029]
    
    $ balms_list = [balm001,balm002,balm003,balm004,balm005,balm006,balm007,balm008,balm009]
    $ creams_list = [cream029]
#    $ essentialoils_list = []
    $ infusions_list = [infusion001,infusion002,infusion003,infusion004,infusion005,infusion006,infusion007,infusion008,infusion009,infusion010,infusion011,infusion012,infusion013,infusion014,infusion015,infusion016,infusion017,infusion018,infusion019,infusion020,infusion021,infusion022,infusion023,infusion024,infusion025,infusion026,infusion027,infusion028,infusion029,infusion030]
    $ poultices_list = [poultice015]
    $ powderedherbs_list = [powdered_herb001,powdered_herb002,powdered_herb003,powdered_herb004,powdered_herb005,powdered_herb006,powdered_herb007,powdered_herb008,powdered_herb009,powdered_herb010,powdered_herb011,powdered_herb012,powdered_herb013,powdered_herb014,powdered_herb015,powdered_herb016,powdered_herb017,powdered_herb018,powdered_herb019,powdered_herb020,powdered_herb021,powdered_herb022,powdered_herb023,powdered_herb024,powdered_herb025,powdered_herb026,powdered_herb027,powdered_herb028,powdered_herb030]
    $ salves_list = [salve001,salve002,salve003,salve004,salve005,salve006,salve007,salve008,salve009,salve010]
    
#    $ bathblends_list = []
    $ decoctions_list = [decoction001,decoction002,decoction003,decoction004,decoction005,decoction006,decoction007,decoction008,decoction009,decoction010,decoction011,decoction012,decoction013,decoction014,decoction015,decoction016,decoction017,decoction018,decoction019,decoction020,decoction021,decoction022,decoction023,decoction024,decoction025,decoction026,decoction027,decoction028,decoction030]
#    $ compresses_list = []
#    $ perfumes_list = []
#    $ pills_list = []
    
    return 
    
    