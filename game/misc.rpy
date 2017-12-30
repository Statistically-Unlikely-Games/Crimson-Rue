init python:

    import json

    def quality_string(value):
        for name, max_v, min_v in QUALITY:
            if in_range(max_v, min_v, value):
                return name

    def in_range(max_v, min_v, value):
        if max_v >= value and min_v < value:
            return True
        return False

    def quality_badge(rank):
        if isinstance(rank, int):
            rank = quality_string(rank)
        return QUALITY_IMAGES[rank]

    def crafted_item(ingredients):
        recipe_item, average_quality, custom_tags = global_recipe_store.can_craft(ingredients)
        player_bag.items_in_pot = []

        player_bag.add_item(item_id=recipe_item.produces, quality=average_quality, custom_tags=custom_tags)
        if recipe_item.containers:
            for item in recipe_item.containers:
                player_bag.add_item(item_id=item)

    def filter_tags(tags):
        _data = []
        _tag_count = {}
        cancel_pairs = {"sweet": "bitter", "bitter": "sweet"}
        tag_upgrade = {"cool": 20, "sweet": 4, "bitter": 4, "slimy": 1}

        for pair in tags:
            for i in pair:
                if " " in i:
                    name, value = i.split(" ")
                    value = int(value)
                else:
                    name = i
                    value = 1

                if name in _data:
                    _tag_count[name] += value
                    continue

                if name in cancel_pairs and cancel_pairs[name] in _data:
                    if cancel_pairs[name] in _tag_count:
                        current_value = value
                        value -= _tag_count[cancel_pairs[name]]
                        _tag_count[cancel_pairs[name]] -= current_value

                    if _tag_count[cancel_pairs[name]] <= 0:
                        _data.remove(cancel_pairs[name])

                        value += 1
                        del _tag_count[cancel_pairs[name]]

                    if value <= 1:
                        continue
                    else:
                        value -= 1

                _data.append(name)
                _tag_count[name] = value

        for ind, i in enumerate(_data):
            if i in _tag_count:
                if _tag_count[i] > tag_upgrade[i]:
                    _data[ind] = i + " " + str(tag_upgrade[i])
                else:
                    _data[ind] = i + " " + str(_tag_count[i])

        return _data

    def item_added_event(item):
        #If the item is added to the player's inventory only!
        if item.kind != "useless":
            renpy.show_screen("inventory_popup", message="Received " + item.name,item=item.name)
        else: 
            renpy.show_screen("inventory_popup", message="Crafting Failed!",item=item.name)
        if item.kind == "book":
            #shelf.add_book(eval(item.id))
            pass # do something

    def item_sell_event(item):
        if renpy.get_screen("store_screen"):
            renpy.show_screen("inventory_popup", message="Sold " + item.name,item=item.name)
            #renpy.show_screen("inventory_popup", message="Received " item.sell_price + "!",item=item.name)
        if item.kind == "book":
            pass # do something

    def item_buy_event(item):
        if renpy.get_screen("store_screen"):
            renpy.show_screen("inventory_popup", message="Bought " + item.name,item=item.name)
        if item.kind == "book":
            shelf.add_book(eval(item.id))
            item.id_get = True
            pass # do something

    def item_fermentation_event(item):
        renpy.show_screen("inventory_popup", message="Crafted " + item.name,item=item.name)
        if item.kind == "book":
            pass # do something

    def item_fermentation_fail_event(item):
        renpy.show_screen("inventory_popup", message="Can't Process!",item=item.name)
        if item.kind == "book":
            pass # do something
            
    def item_drying_event(item):
        renpy.show_screen("inventory_popup", message="Crafted " + item.name,item=item.name)
        if item.kind == "book":
            pass # do something

    def item_drying_fail_event(item):
        renpy.show_screen("inventory_popup", message="Can't Dry!",item=item.name)
        if item.kind == "book":
            pass # do something

    def load_data(tag_list):
        all_files = renpy.list_files()

        for tag in tag_list:
            for filepath in all_files:
                if "data/{}".format(tag) in filepath:
                    data = json.load(renpy.file(filepath))
                    if tag == "items":
                        global_item_store.add_item_data(**data)
                    elif tag == "recipes":
                        global_recipe_store.add_recipe_data(**data)
                    elif tag == "processors":
                        global_processor_store.add_processor_data(**data)
                    elif tag == "dehydrators":
                        global_dehydrator_store.add_dehydrator_data(**data)
