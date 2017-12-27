# The script of the game goes in this file.

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
    what_xmaximum = 950,
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
    what_xmaximum = 950,
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

define narrator = Character(None, what_color = "#000000", what_outlines=[( 0, "#A3A3A3", 2, 2 )])
define black_screen = Character(None, what_color = "#FFFFFF", what_outlines=[( 0, "#808080", 2, 2 )])

define name_only = Character(None, kind = dialogue)

define aeth = Character("Aeth", kind = dialogue)
define aeth_int = Character("Aeth", kind = thoughts)

define kayen = Character("Kayen", kind = dialogue)
define elaine = Character("Master Elaine", kind = dialogue)
define orthrus = Character("Orthrus", kind = dialogue)
define harte = Character("Harte", kind = dialogue)
define mikael = Character("Mikael", kind = dialogue)
define lufte = Character("Lufte", kind = dialogue)
define vemri = Character("Vemri", kind = dialogue)


#Defining Transformations
define slow_dissolve = Dissolve(1.0)
define fast_dissolve = Dissolve(0.25)

transform ease(start, end, time):
    subpixel True
    start
    easein time end
    
transform linear(start, end, time):
    subpixel True
    start
    linear time end
    
transform surprised(start):
    subpixel True
    start
    linear 0.05 yalign 0.9
    start
    
transform zoom_out:
    subpixel True
    zoom 0.4
    

# Declaring books

default shelf = Shelf("Library", 20)
default book_1 = Book("Tutorial", "Tutorial", "Author", "Year")
default herbID1 = Book("Herb Identification Guide vol. 1", "Herb Identification", "Master Elaine", "year")
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
    
# The game starts here.

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
        
        timeofday = "sunrise"
        
        current_loc = "none"
        
        #ITEM VARIABLES
        
        herbID1_get = False
        
        herb_book1 = False
        herb_book2 = False
        herb_book3 = False
        med_book1 = False
        med_book2 = False
        
        
        #HERB GATHER VARIABLES
        
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
        
        
        #LIVECOMP VARIABLES
        
        aeth_outfit = 'vest'
        aeth_pose = 'arms_down'
        aeth_facing = 'right'
        
        elaine_outfit = 'vest'
        elaine_pose = 'hands_hips'
        elaine_facing = 'left'
        
        harte_outfit = 'desk'
        harte_pose = 'book'
        
        kayen_outfit = 'dress'
        kayen_pose = 'arm_down'
        
        lufte_outfit = 'shirt'
        lufte_pose = 'arms_down'
        lufte_facing = 'left'
        
        mikael_outfit = 'shirt'
        mikael_pose = 'arms_down'
        mikael_facing = 'left'
        
        orthrus_outfit = 'shirt'
        orthrus_pose = 'hands_hips'
        orthrus_facing = 'left'
        
        
        #COMMON EVENT VARIABLES
        
        day001_evt = False
        day002_evt = False
        day002_itemshop_evt = False
        day003_evt = False
        
        
        #WORLD EVENT VARIABLES
        
        forest001_evt = False
        forest002_evt = False
        forest003_evt = False
        forest004_evt = False
        forest005_evt = False
        forest006_evt = False
        forest007_evt = False
        forest008_evt = False
        forest009_evt = False
        
        
        #RELATIONSHIP EVENT VARIABLES
        
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

    $ global_item_store = ItemStore()
    $ global_recipe_store = RecipeStore()
    $ global_processor_store = ProcessorStore()
    $ global_dehydrator_store = DehydratorStore()

    $ load_data(["items", "recipes", "processors", "dehydrators"])

    $ player_bag = BaseInventory("Player", 800000, is_player=True)
    $ player_processor = ProcessorBox()
    $ player_dehydrator = DehydratorBox()
    $ seller_bag = BaseInventory("Seller", 800000)

    $ player_recipes = []

    $ player_bag.add_multi_items(["herb001", "herb001", "oil", "oil", "water", "honey"])
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ player_bag.add_item("oil", quality=50, custom_tags=["slimy"])
    $ seller_bag.add_multi_items(["herbID1", "herb001", "herb_oil001", "vodka", "empty_bottle", "wax"])
    
#    "Defining Items, Cookbooks and Inventories."

    $ shelf.add_book(book_1)

    call define_books
    
    
    jump day001

#    menu options_check_menu:
#        "Fermenting":
#            call screen fermenting_screen

#        "Inventory":
#            call screen inventory_screen(player_bag)

#        "Recipe":
#            call screen recipe_screen(global_recipe_store.get_from_id("herb_oil001_recipe"))

#        "Craft":
#            call screen craft_screen

#        "Store":
#            call screen store_screen(player_bag, seller_bag)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
