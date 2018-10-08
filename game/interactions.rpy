init python:

    def no_op(denizen):
        pass

    def disappear(denizen): #Removes sprite from map
        pc_farm.unoccupy(denizen.x, denizen.y)

    def pickup(denizen):
        #Removes sprite from map, adds to pc inventory, popup window
        pc_farm.unoccupy(denizen.x, denizen.y)
        player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])

    def loot(denizen):
        #Changes sprite image, adds to pc inventory, popup window
        player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
        denizen.changeimg("weed2.png")
        denizen.interaction = no_op

    def change_map(denizen):
        #Transports player to new map
        renpy.call("forest_east")
        pc_farm.unoccupy(pc_sprite)


    def craft(denizen):
        #Opens crafting window
        renpy.show_screen("craft_screen")

#    def talk():
#        #Triggers dialogue
#

#   Add some kinda thing where certain denizens turn transparent if pc is within one tile
