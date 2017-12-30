init python:

    class RecipeStore():

        def __init__(self):
            self.store = {}
            self.id_mapping = {}

            self.fail_recipe = None

        def add_recipe_data(self, **kwargs):
            recipe = Recipe(**kwargs)
            name = ",".join(sorted(recipe.ingredients))

            if recipe.fail_recipe:
                self.fail_recipe = recipe
            else:
                self.id_mapping[recipe.id] = name
                self.store[name] = recipe

        def get_from_id(self, id):
            name = self.id_mapping[id]

            return self.store[name]

        def can_craft(self, ingredients):
            item_ids = [i.id for i in ingredients]

            length = len(ingredients) if len(ingredients) else 1
            average_quality = sum( [i.quality for i in ingredients] ) / length
            custom_tags = filter_tags([i.tags for i in ingredients])

            name = ",".join(sorted(item_ids))

            item = self.store.get(name, self.fail_recipe)

            if current_loc != item.craftable_in and item.craftable_in != "all":
                return self.fail_recipe, 100, []

            for stat, value in item.required_skill:
                if getattr(store, stat) >= value:
                    continue
                else:
                    return self.fail_recipe, 100, []

            return item, average_quality, custom_tags

    class Recipe():

        def __init__(self, id, name, ingredients, produces, containers=None, craftable_in="all", required_skill=[], is_known=False, fail_recipe=False):
            self.id = id
            self.name = name
            self.ingredients = ingredients
            self.produces = produces
            self.containers = containers
            self.craftable_in = craftable_in
            self.required_skill = required_skill
            self.is_known = is_known
            self.fail_recipe = fail_recipe

        @property
        def item(self):
            return global_item_store.return_item(self.produces)

        @property
        def ing_items(self):
            _data = []
            for item_id in self.ingredients:
                _data.append(global_item_store.return_item(item_id))

            return _data

screen recipe_screen(recipe):
    tag inventory_group
    zorder 10
    modal True

    default item = recipe.item
    default recipe_ing = recipe.ing_items

    add Solid("#000000") alpha 0.5

    frame:
        xysize (1100, 675)
        xalign 0.5
        yalign 0.5

        background Solid("d3d3d3")

        frame:
            area (0, 0, 550, 675)
            background None

            text item.name size 40 color "#000000" xalign 0.5 ypos 40

            button:
                xysize (250, 250)
                background item.image

                xalign 0.10
                yalign 0.25

            vbox:
                xalign 0.95
                yalign 0.20
                spacing 15

                for tag, value in recipe.required_skill:
                    text "[tag]: [value]" size 25 bold True

                text "BASE PRICE" size 30 bold True xalign 0.5
                text "[item.cost]" size 25 bold True

            text item.description xpos 30 ypos 380

        frame:
            xysize (500, 670)
            xalign 1.0
            background Solid("d3d3d3")

            vbox:
                ypos 40
                spacing 15

                text "RECIPE" size 45 xalign 0.5

                vpgrid:
                    area (0, 0, 550, 250)
                    cols 4
                    spacing 32

                    for ing in recipe_ing:
                        button:
                            xysize (100, 100)
                            background ing.icon

                text "TAGS" size 45

                for tag_name in item.tags:
                    text tag_name.upper() size 30 bold True
                    
    textbutton _("Back") action Hide("recipe_screen") xalign 1.0

screen craft_screen():
    tag inventory_group
    zorder 10
    modal True

    add Solid("#000000") alpha 0.5

    textbutton _("Back") action Hide("craft_screen") xalign 1.0

    frame:
        xysize (1100, 675)
        xalign 0.5
        yalign 0.5

        background Solid("d3d3d3")        

        use inventory_base_screen(player_bag, case="crafting")

        frame:
            xysize (550, 670)
            xalign 1.0
            background Solid("d3d3d3")

            vbox:
                ypos 5
                spacing 15

                text "INGREDIENTS" size 45 xalign 0.5

                vpgrid:
                    area (0, 0, 550, 250)
                    cols 4
                    spacing 32

                    for item in player_bag.items_in_pot:
                        button:
                            xysize (100, 100)
                            background item.icon

                            action Function(player_bag.remove_item_from_put, item=item)

                    for i in range(0, 8-len(player_bag.items_in_pot)):
                        button:
                            xysize (100, 100)
                            background Solid("#c0c0c0")

                textbutton _("Craft Button") action Function(crafted_item, ingredients=player_bag.items_in_pot) xalign 0.5
