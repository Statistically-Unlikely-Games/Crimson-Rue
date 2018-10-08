# If PC is at tile 4,3 that tile should be centered on screen

# center_x (pixels) = 90 (tile width) * 4 (tile) + 45 (tile center) = 405
# center of screen = 1980(resolution)/2 = 990
# xpos = 990 (center of screen) - 405 (center_x) in pixels = 585

# center_y (pixels) = 90 (tile width) * 3 (tile) + 45 (tile center) = 315
# center of screen = 1080(resolution)/2 = 540
# xpos = 540 (center of screen) - 315 (center_x) in pixels = 225

screen map_screen(tMap):

    add "#000"

    $offset_x = 990 - (90 * tMap.center_x) + 45
    $offset_y = 540 - (90 * tMap.center_y) + 45

    add tMap.img:
        pos(offset_x, offset_y)

    for i in range(len(tMap.map)):
        $ row = tMap.map[i]
        for j in range(len(row)):
            $ tile = row[j]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $ offx, offy = tile.occupant.getOffset()
                $ tile_lc_x = 90 * j + offset_x #left corner x
                $ tile_lc_y = 90 * i + offset_y #left corner y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)

        key "K_UP" action [Function(tMap.moveDenizen, pc_sprite.x, pc_sprite.y, 0, -1), SetVariable("pc_dir", "back")]
        key "K_DOWN" action [Function(tMap.moveDenizen, pc_sprite.x, pc_sprite.y, 0, 1), SetVariable("pc_dir", "front")]
        key "K_LEFT" action [Function(tMap.moveDenizen, pc_sprite.x, pc_sprite.y, -1, 0), SetVariable("pc_dir", "left")]
        key "K_RIGHT" action [Function(tMap.moveDenizen, pc_sprite.x, pc_sprite.y, 1, 0), SetVariable("pc_dir", "right")]
        key "K_UP" action [Function(tMap.moveDenizen, pc_sprite.x, pc_sprite.y, 0, -1), SetVariable("pc_dir", "back")]
        key "K_RETURN" action Function(pcInteracts)
