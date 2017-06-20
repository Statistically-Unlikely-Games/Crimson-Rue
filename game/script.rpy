## inventory 1.5 demo

# Declaring images

init python hide:
    for file in renpy.list_files():
        if file.startswith('bg/') and file.endswith('.png'):
            name = file.replace('/', ' ').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('cg/') and file.endswith('.jpg'):
            name = file.replace('cg/', '').replace('.jpg','')
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
            

# Declaring characters

define aeth = Character('Aeth', color="#5D625B", who_font = "PoiretOne-Regular.ttf", who_bold = True, who_outlines = [(3, "#FFFFFF", 0, 0)])


# Declaring books

default shelf = Shelf("Library", 20)
default book_1 = Book("Tutorial", "Tutorial", "Author", "Year")
default book_2 = Book("Herb Identification Guide vol. 1", "kind1", "author", "year")
#default book_3 = Book("Herb Identification Guide vol. 2", "kind2", "author", "year")
#default book_4 = Book("Herb Identification Guide vol. 3", "kind2", "author", "year")
#default book_5 = Book("Medical Journal vol. 1", "kind1", "author", "year")
#default book_6 = Book("Medical Journal vol. 2", "kind2", "author", "year")


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
    #"Game Start"
#    "Setting Variables" 
    #For some reason after this line, small text in the dialogue box stops being white?
    
    ## ------------ ESC MENU AND TIME TRACKING --------------------
    #First day of the game is set to Monday unless you change the calendar code on L32
    $ calendar = Calendar(3, 2, 6, 5, 2017, 2016, 2020) # Calendar(day, oldday, month, oldmonth, year, oldyear, first leap year (can be ignored))
    $ time_cnt = 1
    $ day_cnt = 1

    init -1 python:
        in_overworld01 = False
        in_overworld02 = False
        in_apothecary = False
        in_kitchen = False
        in_cellar = False
        in_itemshop = False
        in_forest001 = False
        in_forest002 = False
        in_forest003 = False
        in_forest004 = False
        in_forest005 = False
        in_forest006 = False
        in_forest007 = False
        in_forest008 = False
        in_forest009 = False
        
        timeofday = "sunrise"
        
        F1Harvest = False
        forest001_first_herb_col = True
        forest001_second_herb_col = True
        forest001_third_herb_col = True
        forest001_fourth_herb_col = True
        forest001_fifth_herb_col = True
        forest001_sixth_herb_col = True
        forest001_seventh_herb_col = True
        forest001_eighth_herb_col = True
        
        F2Harvest = False
        forest002_first_herb_col = True
        forest002_second_herb_col = True
        forest002_third_herb_col = True
        forest002_fourth_herb_col = True
        forest002_fifth_herb_col = True
        forest002_sixth_herb_col = True
        forest002_seventh_herb_col = True
        forest002_eighth_herb_col = True
        
        F3Harvest = False
        forest003_first_herb_col = True
        forest003_second_herb_col = True
        forest003_third_herb_col = True
        forest003_fourth_herb_col = True
        forest003_fifth_herb_col = True
        forest003_sixth_herb_col = True
        forest003_seventh_herb_col = True
        forest003_eighth_herb_col = True
        
        F4Harvest = False
        forest004_first_herb_col = True
        forest004_second_herb_col = True
        forest004_third_herb_col = True
        forest004_fourth_herb_col = True
        forest004_fifth_herb_col = True
        forest004_sixth_herb_col = True
        forest004_seventh_herb_col = True
        forest004_eighth_herb_col = True
        
        F5Harvest = False
        forest005_first_herb_col = True
        forest005_second_herb_col = True
        forest005_third_herb_col = True
        forest005_fourth_herb_col = True
        forest005_fifth_herb_col = True
        forest005_sixth_herb_col = True
        forest005_seventh_herb_col = True
        forest005_eighth_herb_col = True
        
        forest006_first_herb_col = True
        forest006_second_herb_col = True
        forest006_third_herb_col = True
        forest006_fourth_herb_col = True
        forest006_fifth_herb_col = True
        forest006_sixth_herb_col = True
        forest006_seventh_herb_col = True
        forest006_eighth_herb_col = True
        
        F7Harvest = False
        forest007_first_herb_col = True
        forest007_second_herb_col = True
        forest007_third_herb_col = True
        forest007_fourth_herb_col = True
        forest007_fifth_herb_col = True
        forest007_sixth_herb_col = True
        forest007_seventh_herb_col = True
        forest007_eighth_herb_col = True
        
        F8Harvest = False
        forest008_first_herb_col = True
        forest008_second_herb_col = True
        forest008_third_herb_col = True
        forest008_fourth_herb_col = True
        forest008_fifth_herb_col = True
        forest008_sixth_herb_col = True
        forest008_seventh_herb_col = True
        forest008_eighth_herb_col = True
        
        F9Harvest = False
        forest009_first_herb_col = True
        forest009_second_herb_col = True
        forest009_third_herb_col = True
        forest009_fourth_herb_col = True
        forest009_fifth_herb_col = True
        forest009_sixth_herb_col = True
        forest009_seventh_herb_col = True
        forest009_eighth_herb_col = True
    
#    "All variables set."
    
#    show screen calendar_testing
    
    ## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
    $ cookbook = list() 
    
#    "Defining Items, Cookbooks and Inventories."

    $ shelf.add_book(book_1)
    $ shelf.add_book(book_2)

    call define_books
    call define_items
    call define_inventories

#    hide screen calendar_testing
    
#    "Testing future calendar projections."
    
#    $ calendar.getfuture(3)
#    show screen future_testing
#    "Three days in the future."
#    hide screen future_testing
    
#    $ calendar.getfuture(30)
#    show screen future_testing
#    "Thirty days in the future."
#    hide screen future_testing
    
#    $ calendar.getfuture(300)
#    show screen future_testing
#    "Three hundred days in the future."
#    hide screen future_testing
    
#    $ calendar.getfuture(3000)
#    show screen future_testing
#    "Three thousand days in the future."
#    hide screen future_testing
    
#    "Testing past calendar projections."
    
#    $ calendar.getpast(3)
#    show screen past_testing
#    "Three days in the past."
#    hide screen past_testing
    
#    $ calendar.getpast(30)
#    show screen past_testing
#    "Thirty days in the past."
#    hide screen past_testing
    
#    $ calendar.getpast(300)
#    show screen past_testing
#    "Three hundred days in the past."
#    hide screen past_testing

#    $ calendar.getpast(3000)
#    show screen past_testing
#    "Three thousand days in the past."
#    hide screen past_testing

#    "Testing between dates function."
#    $ calendar.getpast(5)
#    $ calendar.between_dates(cnt1=calendar.daycount_from_gamestart, cnt2=calendar.past_daycount)
#    show screen between_testing
#    "The difference between daycount and past_daycount is five."
#    hide screen between_testing
    
#    $calendar.getfuture(5)
#    $ calendar.between_dates(cnt1=calendar.future_daycount, cnt2=calendar.past_daycount)
#    show screen between_testing
#    "The difference between future_daycount and past_daycount is ten."
#    hide screen between_testing
    
    
label intro: 
    
#    show aeth neu at left
#    show elaine neu at right
#    show child neu at center
    
#    "This is a dialogue test."

    show bg overworld01

    "The cold air felt sharp as Aeth breathed it in, carrying the familiar scent of pine."
    
    "It had been several years since their last visit home. And many more years than that since they'd seen it this time of year."
    
    "The snow fell heavy here, and usually one wouldn't want to risk getting stuck. This time, though, that wasn't a problem."
    
    show bg forest001
    show aeth neu at left
    
    "They separated from the caravan before entering town, avoiding the main street."
    
    "Given the circumstances, they didn't want to have to explain themselves to any friendly faces they might run into on the way."
    
    "In short time they arrived at their destination, pulled back their hood, and thought about what they would say."
    
    "Waiting wouldn't make it any easier. They pushed open the heavy oak door, and in a breath called out"
    
    show bg kitchen
    
    aeth "Mother, I'm home. Please cover up, I don't want to accidentally walk in on you again. You never lock the door and it's really problematic."
    
    hide aeth neu
    
# Opening video?

# Funny scene where Aeth walks in on Kayen about to get it on with her female lover
# Wasn't expecting Aeth to come this time of the year, something serious must have happened
# All three have dinner, Aeth avoids giving details about why they came home
# Aeth was dating Teal in secret bc their mom wouldn't approve of a noble, now mother was proved right
# Mother instructs Aeth to go speak with Master Elaine, it has been a long time and she'll be offended if they don't see her first
# Gunna go first thing tomorrow

# Next Day
# Walks through town to see Master Elaine, possibly runs into a few love interests on the way there?
# Possibly see Lufte, small child, hanging out around the front of the shop?
# Elaine is very outgoing and friendly, suggests Aeth start working in the shop again
# Gotta do something, and they were talented. Apprentice moved out and got their own shop, it would help to have another hand around
# Aeth should say they will think about it, they don't want to be a burden on their mother but have some things to sort out
# Elaine will mention that winter is just around the corner, they should use this time to catch up before things get busy

# Timeskip to spring? Should I have more than that here? More introductions?
# Worried putting gameplay off for too long will cause some players to get bored...
    
    jump apothecary_shop










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