# Specification
# Grid/Tile based
# Character stays centered, map moves
# Enter keypress next to and facing item interacts
# Items are obstacles

# 1980 = 90*22
# 1080 = 90*12

define tile_size = 90

# Farm Map = 22 tiles wide x 12 tiles tall
# Forest Map = 55 tiles wide x 55 tiles tall

init python:

    class TestMap:
        def __init__(self, map_grid, img, start_x, start_y):
            self.map = map_grid
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty(self, x, y):
            return self.map[y][x].occupant is None

        def occupy(self, x, y, denizen):
            if not self.isEmpty(x, y):
                return
            self.map[y][x].occupant = denizen

        def unoccupy(self, x, y):
            self.map[y][x].occupant = None

        def moveDenizen(self, x, y, offx, offy):
            if self.isEmpty(x, y):
                return
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                return
            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y + offy][x + offx].occupant = denizen
            denizen.x += offx
            denizen.y += offy
            if self.center_x == x and self.center_y == y:
                self.center_x += offx
                self.center_y += offy

        def triggerInteraction(self, x, y):
            if x < 0 or x >= len(self.map[0]):
                return
            if y < 0 or y >= len(self.map):
                return
            if self.isEmpty(x, y):
                return
            self.map[y][x].occupant.interact()

    class MapTile:
        def __init__(self, occupant=None):
            self.occupant = occupant

    class MapOccupant:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def interact(self):
            pass

    class MapDenizen(MapOccupant):
        def __init__(self, x, y, img, width, height, interaction):
            super(MapDenizen, self).__init__(x, y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction

        def getOffset(self):
            return (tile_size - self.width, tile_size - self.height)

        def interact(self):
            self.interaction(self)

        def changeimg(self, img):
            self.img = img
