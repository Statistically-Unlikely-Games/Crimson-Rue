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
define kayen = Character('Kayen', color="#5D625B", who_font = "PoiretOne-Regular.ttf", who_bold = True, who_outlines = [(3, "#FFFFFF", 0, 0)])
define elaine = Character('Master Elaine', color="#5D625B", who_font = "PoiretOne-Regular.ttf", who_bold = True, who_outlines = [(3, "#FFFFFF", 0, 0)])
define orthrus = Character('Orthrus', color="#5D625B", who_font = "PoiretOne-Regular.ttf", who_bold = True, who_outlines = [(3, "#FFFFFF", 0, 0)])
define harte = Character('Harte', color="#5D625B", who_font = "PoiretOne-Regular.ttf", who_bold = True, who_outlines = [(3, "#FFFFFF", 0, 0)])
define mikael = Character('Mikael', color="#5D625B", who_font = "PoiretOne-Regular.ttf", who_bold = True, who_outlines = [(3, "#FFFFFF", 0, 0)])


# Declaring books

default shelf = Shelf("Library", 20)
default book_1 = Book("Tutorial", "Tutorial", "Author", "Year")
default book_2 = Book("Herb Identification Guide vol. 1", "Herb Identification", "author", "year")
default book_3 = Book("Herb Identification Guide vol. 2", "Herb Identification", "author", "year")
default book_4 = Book("Herb Identification Guide vol. 3", "Herb Identification", "author", "year")
default book_5 = Book("Medical Journal vol. 1", "Medical Journal", "author", "year")
default book_6 = Book("Medical Journal vol. 2", "Medical Journal", "author", "year")


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
        herb_book1 = False
        herb_book2 = False
        herb_book3 = False
        med_book1 = False
        med_book2 = False
        
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
    
    "Skip Intro?"
    
    menu:

        "Yes":
            jump apothecary_shop


        "No":
            "Get on with it, then."


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
    
    aeth "Mother, I'm home. Are you there?"
    
    "There was a brief shuffling sound from the back of the room. Aeth's eyes were still adjusting to the dim lighting when their mother appeared before them."
    
    show kayen neu at right
    
    kayen "Aeth-- What are you doing back this time of year?"
    
    "She looked disheveled, as if she'd just gotten out of bed. It was a bit too early for that, but seeing another figure move further in, Aeth realized they had interrupted."
    
    aeth "Sorry to surprise you. Some... things happened. I decided to come home early."
    
    "Aeth's body language was withdrawn, and their tone flat. Kayen's eyes narrowed as they inspected their child, then softened."
    
    kayen "You know you are always welcome home. You've been traveling a long time, it's good to have a break once in a while."
    
    kayen "Why don't you drop by Elaine's shop tomorrow? I'm sure you've gathered a lot more experience while you were out, and she's been flooded with customers recently."
    
    kayen "And of course, she'd be horribly offended if you take too long to visit now that you're in town."
    
    "She laughed heartily, and Aeth had to smile. Elaine, who was like a grandmother to them, could be exceedingly petty when she felt slighted."
    
    kayen "You should rest for today, though. Bring your stuff in, we'll get dinner ready. I'm sure you haven't been eating. XXX is over, we'll have a full table!"
    
    "Aeth noded, and carried their things into one of the spare rooms."
    
    hide kayen neu
    
    show bg cellar
    
    "Aeth put their bag on the floor and prepared for dinner."
    
    hide aeth neu
    
    show bg black
    
    "Aeth went to sleep."
    
    show bg forest002
    
    "The next day, they went into town."
    
    "As they approached their master's shop, they saw a small child hiding around the corner."
    
    show lufte neu at right
    
    "Child" "..."
    
    show aeth neu at center
    
    aeth "Do you need any help?"
    
    "The child seemed surprised to hear a voice behind them, and jumped slightly. Aeth stared blankly at them, waiting."
    
    "The child backed away slowly before turning and running around a corner."
    
    hide lufte neu
    
    "Aeth stared after them for a moment, then went about their business."
    
    show aeth neu at left
    
    show bg apothecary
    
    "When they entered the shop, Master Elaine was busily preparing the morning's medication."
    
    show elaine neu at right
    
    elaine "Aeth! My dear, you are certainly home early, aren't you? Well, I'm sure there's a long explanation for that, but we simply don't have the time."
    
    "She hurriedly shoved an assortment of bottles and tools on the counter, and pushed them in Aeth's direction."
    
    elaine "I'll need you to prepare some dried X, a Y tincture, and get the Z started."
    
    hide elaine neu
    
    show bg forest002
    
    "Faster than they could register, the morning was over. Elaine sent them out to pick up supplies and deliver medications in town."
    
    "They started with deliveries, so that they only had to carry supplies on the way back."
    
    "Aeth approached a small house on the outskirts of town."
    
    aeth "Hm, this seems to be the right place."
    
    "Supposedly a young man lived here named Orthrus, and they were delivering medication for his younger sister."
    
    "As they approached the door, a voice stopped them."
    
    show orthrus neuR at left behind aeth
    
    "Young Man" "You have business with me?"
    
    "He leaned over from behind Aeth, uncomfortably close, though they never heard him approach. Their body instinctively tensed."
    
    show orthrus neu  at left behind aeth
    
    aeth "Master Elaine sent me to deliver medicine to Orthrus."
    
    show orthrus neu at center
    
    "He stepped back, and their muscles eased back to their previous position."
    
    orthrus "Ah, that'll be for me. Thanks for dropping them by, we'd just about run out."
    
    "A wide grin spread across his face as he reached out and took the bag."
    
    orthrus "You're Aeth, yeah? Kayen's kid? We met a few times when we were younger, dunno if you remember me?"
    
    "Orthrus's family ran a merchant caravan, and he and his sister often traveled with them away from town."
    
    "By the time they disappeared, Aeth had already left on their journey, and because of this they hadn't had much interaction with either sibling."
    
    "It was possible they'd seen each other in passing, but Aeth would have a hard time picking his face out of a crowd."
    
    "They'd learned that being so direct was considered rude by most, and remained silent unsure of what to say in response."
    
    orthrus "Er, it was a long time ago in any case. If you're helping out at Elaine's shop I'm sure we'll see more of each other from now on."
    
    orthrus "We'll just call this our first meeting then-- thanks in advanced for your hard work! These meds make a life a lot easier."
    
    "Aeth inclined their head towards Orthrus in a greeting and replied"
    
    aeth "Thank you for your patronage."
    
    "As they turned to leave, Orthrus waved cheekily at them from behind."
    
    hide orthrus neu
    
    "That ended up being a bit more stressful than they'd anticipated, but Aeth figured it worked out okay."
    
    "The next stop on their agenda was the general store. They needed to pick up some more glass bottles, and a few other essentials."
    
    show bg itemshop
    
    "Aeth walked in and was greeted by the shopkeeper, Harte."
    
    show harte neu at right
    
    harte "Aeth! I heard you were back in town early. Elaine got you running errands already?"
    
    "Aeth gave a small smile as they replied."
    
    aeth "You know Master Elaine. She goes at her own pace, and anyone around will get dragged right along."
    
    harte "Haha, you got that right! So, she send you for the regular refills?"
    
    aeth "The regular, plus an extra case of containers and wax."
    
    harte "I'm on it!"
    
    "Harte disappeared into the back room for a moment, then came out with a large, heavy box. They placed it on the counter, then added a few extra items from the supply shelf."
    
    harte "This should get you set up. You okay to carry all that?"
    
    aeth "I'll be fine, thanks."
    
    harte "They put you to work on the caravan, eh? Haha, good to see you back again in any case. Feel free to drop by anytime you need something!"
    
    aeth "I will-- have a good day."
    
    hide harte neu
    show bg forest002
    
    "Aeth left the shop and made their way towards the last errand."
    
    "They took the main street in the center of town and ended up in front of a shop with a sign that wasn't there last time they were here."
    
    "It shown the Healer's crest, just like their master's shop. Aeth stepped in and took a look around."
    
    show bg apothecary
    
    "The front of the shop had a more clinical feel than Master Elaine's-- it was missing the racks of dried herbs and general clutter."
    
    "Instead, there were more seats, and a curtain near the back of the room. Not long after the door shut behind them a familiar figure stepped out from behind it."
    
    show mikael neu at center
    
    aeth "Mikael?"
    
    mikael "Aeth, it's good to see you. Sorry for the delay, I was just wiping down the examination table."
    
    aeth "No, it's fine. Is this your shop?"
    
    mikael "Ah, right-- you were gone quite a while this time. I opened shop near the beginning of last year, with Master Elaine's blessings of course."
    
    mikael "She had been looking to step back from Guild work, so I've been taking on more of the administrative tasks. I've not quite taken over as representative, but..."
    
    mikael "Master Elaine has been wanting to tell the Healer's in Harvest City to get off her back for a while, haha."
    
    "His face emanated warmth, and Aeth couldn't help but smile at the image of Master Elaine chasing the powerful guild members out of her shop."
    
    mikael "Ahem, in any case, I'm guessing Master Elaine has you running her errands?"
    
    aeth "Yes, I'm here to pick up some distilled alcohol, and a few other specialty items."
    
    "Mikael looks down and sees the fairly large and heavy box Aeth is carrying."
    
    mikael "Well, I was just planning on closing the shop for a lunch break, why don't I help you take these back? That box looks pretty heavy."
    
    aeth "I've got this covered. But I wouldn't mind the company on the way back. It's been a while, it would be good to catch up."
    
    mikael "Alright, just give me a moment to pack up those supplies."
    
    hide mikael neu
    
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