init python:
        farm_map = []

        for i in range(12):
            new_row = []
            for j in range(22):
                new_row.append(MapTile())
            farm_map.append(new_row)

        pc_farm = TestMap(farm_map, "farm.png", 7, 8)
        pc_sprite = MapDenizen(7, 8, "pc", 90, 180, no_op)
        pc_farm.occupy(7, 8, pc_sprite)

        farm_door = MapDenizen(7, 9, "door.png", 90, 90, change_map)
        pc_farm.occupy(7, 7, farm_door)

        weed01_sprite = MapDenizen(14, 7, "weed.png", 90, 90, pickup)
        pc_farm.occupy(14, 7, weed01_sprite)
        weed02_sprite = MapDenizen(12, 9, "weed.png", 90, 90, loot)
        pc_farm.occupy(12, 9, weed02_sprite)
        weed03_sprite = MapDenizen(17, 8, "weed.png", 90, 90, pickup)
        pc_farm.occupy(17, 8, weed03_sprite)

    # This should be made into a loop later
        house_lf01 = MapOccupant(6, 7)
        pc_farm.occupy(6, 7, house_lf01)
        house_lf02 = MapOccupant(5, 7)
        pc_farm.occupy(5, 7, house_lf02)
        house_lf03 = MapOccupant(4, 7)
        pc_farm.occupy(4, 7, house_lf03)
        house_lf04 = MapOccupant(3, 7)
        pc_farm.occupy(3, 7, house_lf04)

        house_rf01 = MapOccupant(8, 7)
        pc_farm.occupy(8, 7, house_rf01)
        house_rf02 = MapOccupant(9, 7)
        pc_farm.occupy(9, 7, house_rf02)
        house_rf03 = MapOccupant(10, 7)
        pc_farm.occupy(10, 7, house_rf03)

        trough_1 = MapOccupant(9, 8)
        pc_farm.occupy(9, 8, trough_1)
        trough_2 = MapOccupant(10, 8)
        pc_farm.occupy(10, 8, trough_2)

################################################################################

        east_map = []

        for i in range(55):
            new_row = []
            for j in range(55):
                new_row.append(MapTile())
            east_map.append(new_row)

        forest_east = TestMap(east_map, "forest_east.png", 0, 25)
        pc_sprite = MapDenizen(0, 25, "pc", 90, 180, no_op)
        forest_east.occupy(0, 25, pc_sprite)

################################################################################

        northeast_map = []

        for i in range(55):
            new_row = []
            for j in range(55):
                new_row.append(MapTile())
            northeast_map.append(new_row)

        forest_northeast = TestMap(northeast_map, "forest_northeast.png", 25, 0)
        pc_sprite3 = MapDenizen(25, 0, "pc", 90, 180, no_op)
        forest_northeast.occupy(25, 0, pc_sprite3)

################################################################################

label hide_map_screen:
    hide screen map_screen
    return

label forest_east:
    show screen map_screen(forest_east)
    return

label forest_northeast:
    show screen map_screen(forest_northeast)
    return
