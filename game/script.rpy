## inventory 1.5 demo

# Declaring images

init python hide:
    for file in renpy.list_files():
        if file.startswith('images/bg/') and file.endswith('.png'):
            name = file.replace('images/bg/', ' ').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('images/cg/') and file.endswith('.jpg'):
            name = file.replace('images/cg/', '').replace('.jpg','')
            renpy.image(name, Image(file))
            

# Declaring characters

define dialogue = Character(
    None,

    window_background = "gui/dialoguebox.png",

    who_font = "PoiretOne-Regular.ttf",
    who_outlines = [(3, "#FF6C03", 0, 0)],
    who_color="#FFD200",
    who_bold = True,
    who_xalign=0.5,
    who_textalign=0.5,

    what_color = "#000000",
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

define thoughts = Character(
    None,

    window_background = "gui/thoughtbox.png",

    who_font = "PoiretOne-Regular.ttf",
    who_outlines = [(3, "#FF6C03", 0, 0)],
    who_color="#FFD200",
    who_bold = True,
    who_xalign=0.5,
    who_textalign=0.5,

    what_color = "#FFFFFF",
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

define narrator = Character(None, what_outlines=[( 0, "#A3A3A3", 2, 2 )])

define name_only = Character(None, kind = dialogue)

define aeth = Character('Aeth', kind = dialogue)
define aeth_int = Character('Aeth', kind = thoughts)

define kayen = Character('Kayen', kind = dialogue)
define elaine = Character('Master Elaine', kind = dialogue)
define orthrus = Character('Orthrus', kind = dialogue)
define harte = Character('Harte', kind = dialogue)
define mikael = Character('Mikael', kind = dialogue)
define lufte = Character('Lufte', kind = dialogue)


#Defining Transformations
define slow_dissolve = Dissolve(1.0)
define fast_dissolve = Dissolve(0.25)

transform easein_right:
    subpixel True
    offscreenright #starting position
    easein 2.0 right #transition, speed, ending position
    
transform easein_rightctr:
    subpixel True
    offscreenright #starting position
    easein 2.0 center #transition, speed, ending position
    
transform easeout_right:
    subpixel True
    right #starting position
    easein 2.0 offscreenright #transition, speed, ending position
    
transform easeout_rightctr:
    subpixel True
    center #starting position
    easein 2.0 offscreenright #transition, speed, ending position
    
transform easein_left:
    subpixel True
    offscreenleft #starting position
    easein 2.0 left #transition, speed, ending position
    
transform easein_leftctr:
    subpixel True
    offscreenleft #starting position
    easein 2.0 center #transition, speed, ending position
    
transform easeout_left:
    subpixel True
    left #starting position
    easein 2.0 offscreenleft #transition, speed, ending position
    
transform easeout_leftctr:
    subpixel True
    center #starting position
    easein 2.0 offscreenleft #transition, speed, ending position
    
transform surprised_left:
    yalign 1.0 xalign 1.0
    linear 0.05 yalign 0.9
    linear 0.1 yalign 1.0

transform surprised_ctr:
    yalign 1.0 xalign 0.5
    linear 0.05 yalign 0.9
    linear 0.1 yalign 1.0

transform surprised_right:
    yalign 1.0 xalign 0.0
    linear 0.05 yalign 0.9
    linear 0.1 yalign 1.0


# Declaring books

default shelf = Shelf("Library", 20)
default book_1 = Book("Tutorial", "Tutorial", "Author", "Year")
default book_2 = Book("Herb Identification Guide vol. 1", "Herb Identification", "Master Elaine", "year")
default book_3 = Book("Herb Identification Guide vol. 2", "Herb Identification", "Master Elaine", "year")
default book_4 = Book("Herb Identification Guide vol. 3", "Herb Identification", "Master Elaine", "year")
default book_5 = Book("Medical Journal vol. 1", "Medical Journal", "Master Elaine", "year")
default book_6 = Book("Medical Journal vol. 2", "Medical Journal", "Master Elaine", "year")
default book_7 = Book("Medical Journal vol. 3", "Medical Journal", "Master Elaine", "year")
default book_8 = Book("Medical Journal vol. 4", "Medical Journal", "Master Elaine", "year")
default book_9 = Book("Medical Journal vol. 5", "Medical Journal", "Master Elaine", "year")
default book_10 = Book("Medical Journal vol. 6", "Medical Journal", "Master Elaine", "year")


# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
    scene bg black
    $ renpy.pause(0)
    scene bg logo
    with dissolve
    with Pause (1.5)
    
    scene bg main_menu
    with fade
    with Pause(1.5)
    
    return 
    
      
label start:  
    #"Game Start"
#    "Setting Variables" 
    #For some reason after this line, small text in the dialogue box stops being white?
    
    ## ------------ ESC MENU AND TIME TRACKING --------------------
    #First day of the game is set to Monday unless you change the calendar code on L32
    $ calendar = Calendar(3, 2, 11, 10, 2017, 2016, 2020) # Calendar(day, oldday, month, oldmonth, year, oldyear, first leap year (can be ignored))
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
        forest001_thistle_col = True
        forest001_blackberry_col = True
        forest001_oak_col = True
        forest001_garlic_col = True
        forest001_mint_col = True
        forest001_oregano_col = True
        forest001_chamomile_col = True
        forest001_mullein_col = True
        forest001_redclover_col = True
        forest001_stjohns_col = True
        forest001_burdock_col = True
        forest001_sage_col = True
        forest001_hyssop_col = True
        forest001_borage_col = True
        forest001_rosemary_col = True
        forest001_licorice_col = True
        forest001_poppy_col = True
        
        F2Harvest = False
        forest002_thistle_col = True
        forest002_dandelion_col = True
        forest002_blackberry_col = True
        forest002_oak_col = True
        forest002_oregano_col = True
        forest002_parsley_col = True
        forest002_chamomile_col = True
        forest002_mullein_col = True
        forest002_redclover_col = True
        forest002_stjohns_col = True
        forest002_burdock_col = True
        forest002_laurel_col = True
        forest002_hyssop_col = True
        forest002_calendula_col = True
        forest002_rosemary_col = True
        forest002_licorice_col = True
        
        F3Harvest = False
        forest003_thistle_col = True
        forest003_blackberry_col = True
        forest003_oak_col = True
        forest003_garlic_col = True
        forest003_oregano_col = True
        forest003_parsley_col = True
        forest003_chamomile_col = True
        forest003_chamomile2_col = True
        forest003_mullein_col = True
        forest003_redclover_col = True
        forest003_stjohns_col = True
        forest003_burdock_col = True
        forest003_sage_col = True
        forest003_borage_col = True
        forest003_calendula_col = True
        forest003_rosemary_col = True
        forest003_licorice_col = True
        
        F4Harvest = False
        forest004_dandelion_col = True
        forest004_blackberry_col = True
        forest004_oak_col = True
        forest004_mint_col = True
        forest004_oregano_col = True
        forest004_parsley_col = True
        forest004_plantain_col = True
        forest004_chamomile_col = True
        forest004_violet_col = True
        forest004_mullein_col = True
        forest004_stjohns_col = True
        forest004_burdock_col = True
        forest004_sage_col = True
        forest004_hyssop_col = True
        forest004_calendula_col = True
        forest004_rosemary_col = True
        forest004_licorice_col = True
        
        F5Harvest = False
        forest005_thistle_col = True
        forest005_dandelion_col = True
        forest005_blackberry_col = True
        forest005_oak_col = True
        forest005_garlic_col = True
        forest005_mint_col = True
        forest005_plantain_col = True
        forest005_chamomile_col = True
        forest005_violet_col = True
        forest005_mullein_col = True
        forest005_stjohns_col = True
        forest005_burdock_col = True
        forest005_laurel_col = True
        forest005_calendula_col = True
        forest005_rosemary_col = True
        forest005_lemonbalm_col = True
        forest005_licorice_col = True
        forest005_crownflower_col = True
        
        forest006_thistle_col = True
        forest006_dandelion_col = True
        forest006_oak_col = True
        forest006_garlic_col = True
        forest006_mint_col = True
        forest006_oregano_col = True
        forest006_parsley_col = True
        forest006_redclover_col = True
        forest006_burdock_col = True
        forest006_calendula_col = True
        forest006_rosemary_col = True
        forest006_comfrey_col = True
        forest006_crownflower_col = True
        forest006_poppy_col = True
        forest006_goldenseal_col = True
        
        F7Harvest = False
        forest007_thistle_col = True
        forest007_dandelion_col = True
        forest007_blackberry_col = True
        forest007_mint_col = True
        forest007_oregano_col = True
        forest007_parsley_col = True
        forest007_violet_col = True
        forest007_basil_col = True
        forest007_stjohns_col = True
        forest007_yellowdock_col = True
        forest007_comfrey_col = True
        forest007_lemonbalm_col = True
        forest007_marshmarigold_col = True
        forest007_goldenseal_col = True
        
        F8Harvest = False
        forest008_thistle_col = True
        forest008_dandelion_col = True
        forest008_blackberry_col = True
        forest008_oak_col = True
        forest008_garlic_col = True
        forest008_oregano_col = True
        forest008_parsley_col = True
        forest008_plantain_col = True
        forest008_plantain2_col = True
        forest008_violet_col = True
        forest008_basil_col = True
        forest008_stjohns_col = True
        forest008_yellowdock_col = True
        forest008_borage_col = True
        forest008_lemonbalm_col = True
        forest008_marshmarigold_col = True
        
        F9Harvest = False
        forest009_thistle_col = True
        forest009_dandelion_col = True
        forest009_blackberry_col = True
        forest009_violet_col = True
        forest009_basil_col = True
        forest009_stjohns_col = True
        forest009_yellowdock_col = True
        forest009_sage_col = True
        forest009_laurel_col = True
        forest009_hyssop_col = True
        forest009_comfrey_col = True
        forest009_lemonbalm_col = True
        forest009_marshmarigold_col = True
        forest009_marshmarigold2_col = True
        forest009_goldenseal_col = True
        
        orth_tru = 10
        orth_res = 0
        orth_riv = 0
        orth_pla = 0
        orth_rom = 0
        orth_sex = 0
        
        orth_tru_evt_1 = False
        orth_tru_evt_2 = False
        orth_tru_evt_3 = False
        orth_tru_evt_4 = False
        orth_tru_evt_5 = False
        
        orth_res_evt_1 = False
        orth_res_evt_2 = False
        orth_res_evt_3 = False
        orth_res_evt_4 = False
        orth_res_evt_5 = False
        
        orth_riv_evt_1 = False
        orth_riv_evt_2 = False
        orth_riv_evt_3 = False
        orth_riv_evt_4 = False
        orth_riv_evt_5 = False
        
        orth_pla_evt_1 = False
        orth_pla_evt_2 = False
        orth_pla_evt_3 = False
        orth_pla_evt_4 = False
        orth_pla_evt_5 = False
        
        orth_rom_evt_1 = False
        orth_rom_evt_2 = False
        orth_rom_evt_3 = False
        orth_rom_evt_4 = False
        orth_rom_evt_5 = False
        
        orth_sex_evt_1 = False
        orth_sex_evt_2 = False
        orth_sex_evt_3 = False
        orth_sex_evt_4 = False
        orth_sex_evt_5 = False
    
#    "All variables set."
    
    ## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
    $ cookbook = list() 
    
#    "Defining Items, Cookbooks and Inventories."

    $ shelf.add_book(book_1)

    call define_books
    call define_items
    call define_inventories
    
    
    
    jump intro
    
    
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

