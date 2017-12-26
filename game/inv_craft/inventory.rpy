init python:

    class BaseInventory():

        def __init__(self, name, money=0, is_player=False):
            self.name = name
            self.money = money
            self.is_player = is_player

            self.store = []
            self.categories = set()

            self.items_in_pot = []

            self.filtering = ""
            self.update = False

        def add_item(self, item_id=None, item=None, quality=0, custom_tags=[]):
            if not item:
                item = global_item_store.return_item(item_id)

            if quality:
                item.quality = quality

            if custom_tags:
                item.tags = custom_tags

            self.store.append(item)
            self.categories.add(item.kind)

            item_added_event(item)

        def add_multi_items(self, item_list):
            for item_id in item_list:
                self.add_item(item_id)

        def remove_item(self, item):
            self.store.remove(item)

        def add_item_to_put(self, item):
            if len(self.items_in_pot) == 8:
                return
                
            self.store.remove(item)
            self.items_in_pot.append(item)

        def remove_item_from_put(self, item):
            self.store.append(item)
            self.items_in_pot.remove(item)

        def buy_item(self, item):
            if self.is_player:
                self.money -= item.buy_price
            else:
                self.money -= item.sell_price
            self.add_item(item=item)

        def sell_item(self, item):
            if self.is_player:
                self.money += item.sell_price
            else:
                self.money += item.buy_price
            self.remove_item(item)

        def refresh_items(self):
            for item in self.store:
                item.change_quality()

        def list_items(self):
            return [ item for item in self.store if not self.filtering or item.kind == self.filtering ]

        def sort(self, method):
            if method == "cost":
                self.store.sort(key=lambda item: item.cost)
            elif method == "name":
                self.store.sort(key=lambda item: item.name)
            elif method == "quality":
                self.store.sort(key=lambda item: item.quality)

screen inventory_screen(bag):
    tag inventory_group
    zorder 10
    modal True

    default viewing_item = None
    add Solid("#000000") alpha 0.5

    frame:
        xysize (1100, 675)
        xalign 0.5
        yalign 0.5

        background Solid("d3d3d3")

        use inventory_base_screen(bag, case="inventory")

        if viewing_item:
            frame:
                xysize (500, 670)
                xalign 1.0
                background Solid("d3d3d3")

                text viewing_item.name.upper() size 40 color "#000000" xalign 0.5

                button:
                    xysize (250, 250)
                    background viewing_item.image

                    add viewing_item.get_quality_badge xalign 0.95 yalign 0.05

                    xalign 0.10
                    yalign 0.25

                vbox:
                    xalign 0.80
                    yalign 0.20
                    spacing 15

                    for tag_name in viewing_item.tags:
                        text tag_name.upper() size 30 bold True

                text viewing_item.description xpos 0 ypos 380
                
    textbutton _("Back") action Hide("inventory_screen") xalign 1.0

screen inventory_base_screen(bag, case, seller_bag=None):
    frame:
        area (0, 0, 570, 675)
        background None

        text "INVENTORY" size 40 color "#000000" xalign 0.50

        vpgrid:
            area (0, 55, 520, 500)
            cols 4
            spacing 25
            draggable True
            mousewheel True

            scrollbars "vertical"

            for item in bag.list_items():
                if item:
                    vbox:
                        spacing 5

                        button:
                            xysize (100, 100)
                            background item.icon

                            add item.get_quality_badge xalign 0.95 yalign 0.05 at zoom_out

                            if case == "inventory":
                                action SetScreenVariable("viewing_item", item)
                            elif case == "crafting":
                                action Function(bag.add_item_to_put, item=item)
                            elif case == "store":
                                action BuySell(item=item, buyer=bag, seller=seller_bag)
                            elif case == "fermenting":
                                action [Function(player_processor.add_to_box, item=item), SetScreenVariable("showing", "")]

                        if case == "store":
                            if bag.is_player:
                                text "[item.sell_price]" xalign 0.5
                            else:
                                text "[item.buy_price]" xalign 0.5

            if len(bag.list_items()) < 12:
                for i in range(0, 12-len(bag.list_items())):
                    button:
                        xysize (100, 100)
                        background Solid("#c0c0c0")

        vbox:
            yalign 1.0
            xmaximum 550
            spacing 5

            hbox:
                spacing 5

                textbutton _("Name") action Function(bag.sort, method="name")
                textbutton _("Cost") action Function(bag.sort, method="cost")
                textbutton _("Quality") action Function(bag.sort, method="quality")

            hbox:
                spacing 5
                for kind in bag.categories:
                    textbutton _(kind) action SetField(bag, "filtering", kind), SetScreenVariable("viewing_item", None)
                textbutton _("None") action SetField(bag, "filtering", ""), SetScreenVariable("viewing_item", None)

screen store_screen(player, seller):
    tag inventory_group
    zorder 10
    modal True

    add Solid("#000000") alpha 0.5

    frame:
        xysize (1100, 675)
        xalign 0.5
        yalign 0.5

        background Solid("d3d3d3")
        
        hbox:
            spacing 5

            use inventory_base_screen(player, case="store", seller_bag=seller)
            add Solid("#000000", xysize=(10, 600)) yalign 0.5 xoffset -30
            use inventory_base_screen(seller, case="store", seller_bag=player)

    textbutton _("Back") action Hide("store_screen") xalign 1.0
