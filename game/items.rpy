label items:
    "You are now in the items label."

    ######### DEFINE INVENTORIES ##########    
    $ pc_inv = Inventory("Aeth")
    
    ######### DEFINE ITEM OBJECTS ##########
    ### The format is name, description, icon image (if applicable), value (if applicable, selling/buying value), action (screen language action to be performed when icon is clicked on inventory screen), and recipe (if craftable).
    
    ### Items without icons are created like this:      
    #$ quarter = Item("Quarter", "A new quarter)
    
    ### Items with icons are created like this:
    $ eye = Item(name="Eyeball", desc="A human eyeball, how creepy!", icon="inv/eye.png", value=250)
    $ herb001 = Item(name="Herb One", desc="A medicinal herb.", icon="inv/herb001.png", value=100)
    $ herb002 = Item(name="Herb Two", desc="A medicinal herb.", icon="inv/herb002.png", value=100)
    $ herb003 = Item(name="Herb Three", desc="A medicinal herb.", icon="inv/herb003.png", value=100)
    $ herb004 = Item(name="Herb Four", desc="A medicinal herb.", icon="inv/herb004.png", value=100)
    $ herb005 = Item(name="Herb Five", desc="A medicinal herb.", icon="inv/herb005.png", value=100)
    $ herb006 = Item(name="Herb Six", desc="A medicinal herb.", icon="inv/herb006.png", value=100)
    $ herb007 = Item(name="Herb Seven", desc="A medicinal herb.", icon="inv/herb007.png", value=100)
    $ herb008 = Item(name="Herb Eight", desc="A medicinal herb.", icon="inv/herb008.png", value=100)
    $ herb009 = Item(name="Herb Nine", desc="A medicinal herb.", icon="inv/herb009.png", value=100)
    $ herb010 = Item(name="Herb Ten", desc="A medicinal herb.", icon="inv/herb010.png", value=100)

    # Items that can be used in crafting
    $ but = Item("Button", "A shiny button", "inv/button.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    $ yarn = Item("Yarn", "Yarny yarny yarn.", "inv/yarn.png", 30, act=Show("inventory_popup", message="This item is only used in crafting"))  
    
    $ fabric = Item("Fabric", "You know, cloth.", "inv/fabric.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    $ coin = Item("Coin", "An old coin", "inv/coin.png", 1, act=Show("inventory_popup", message="This item is only used in crafting"))
    
    # An item with a unique action (shows screen with custom message)
    $ sword = Item("Awesome Sword", "An awesome sword.", "inv/sword.png", 500, Show("inventory_popup", message="You wave the sword around wildly but nothing happens."))

    # An item that can be crafted has a recipe, which is a nested list of [ingredient, qty]
    $ necklace = Item("Penny Necklace", "Super magic.", "inv/necklace.png", 50, recipe=[[coin,6],[yarn,1]])    
    $ doll = Item("Handmade Doll", "Guaranteed to bring luck. (Or not?) Very huggable, mind the needle.", "inv/doll.png", 100000, recipe=[[but,2],[fabric,3],[yarn,1]])    
    
    "Let's return to script."
    
    return 