default pc_dir = "front"

image pc = "pc [pc_dir]"

define pc_offset = -90

init python:
    def getFacingTile():
        if pc_dir == "back":
            return (pc_sprite.x, pc_sprite.y -1)
        elif pc_dir == "dback_left":
            return (pc_sprite.x -1, pc_sprite.y -1)
        elif pc_dir == "dback_right":
            return (pc_sprite.x +1, pc_sprite.y -1)
        elif pc_dir == "dfront_left":
            return (pc_sprite.x -1, pc_sprite.y +1)
        elif pc_dir == "dfront_right":
            return (pc_sprite.x +1, pc_sprite.y +1)
        elif pc_dir == "front":
            return (pc_sprite.x, pc_sprite.y +1)
        elif pc_dir == "left":
            return (pc_sprite.x -1, pc_sprite.y)
        else:
            return (pc_sprite.x +1, pc_sprite.y)

    def pcInteracts():
        x, y = getFacingTile()
        pc_farm.triggerInteraction(x, y)

image pc back:
    "pc/pc_back_1.png"
    0.15
    "pc/pc_back_2.png"
    0.2
    "pc/pc_back_3.png"
    0.15
    "pc/pc_back_2.png"
    0.2
    repeat

image pc dback_left:
    "pc/pc_dback_left_1.png"
    0.15
    "pc/pc_dback_left_2.png"
    0.2
    "pc/pc_dback_left_3.png"
    0.15
    "pc/pc_dback_left_2.png"
    0.2
    repeat

image pc dback_right:
    "pc/pc_dback_right_1.png"
    0.15
    "pc/pc_dback_right_2.png"
    0.2
    "pc/pc_dback_right_3.png"
    0.15
    "pc/pc_dback_right_2.png"
    0.2
    repeat

image pc dfront_left:
    "pc/pc_dfront_left_1.png"
    0.15
    "pc/pc_dfront_left_2.png"
    0.2
    "pc/pc_dfront_left_3.png"
    0.15
    "pc/pc_dfront_left_2.png"
    0.2
    repeat

image pc dfront_right:
    "pc/pc_dfront_right_1.png"
    0.15
    "pc/pc_dfront_right_2.png"
    0.2
    "pc/pc_dfront_right_3.png"
    0.15
    "pc/pc_dfront_right_2.png"
    0.2
    repeat

image pc front:
    "pc/pc_front_1.png"
    0.15
    "pc/pc_front_2.png"
    0.2
    "pc/pc_front_3.png"
    0.15
    "pc/pc_front_2.png"
    0.2
    repeat

image pc left:
    "pc/pc_left_1.png"
    0.15
    "pc/pc_left_2.png"
    0.2
    "pc/pc_left_3.png"
    0.15
    "pc/pc_left_2.png"
    0.2
    repeat

image pc right:
    "pc/pc_right_1.png"
    0.15
    "pc/pc_right_2.png"
    0.2
    "pc/pc_right_3.png"
    0.15
    "pc/pc_right_2.png"
    0.2
    repeat
