init python:

    class ItemStore():

        def __init__(self):
            self.store = {}

        def add_item_data(self, **kwargs):
            self.store[kwargs["id"]] = kwargs

        def get_item_data(self, id):
            return self.store[id]

        def return_item(self, id):
            if id not in self.store:
                return

            return Item(**self.store[id])

    class Item():

        def __init__(self, id, name, icon, image, description, kind, cost, season, quality=100, tags=[], day_degrade=0):
            self.id = id
            self.name = name
            self.icon = icon
            self.image = image
            self.description = description
            self.kind = kind
            self.cost = cost
            self.season = season
            self.quality = quality
            self.tags = tags
            self.day_degrade = day_degrade

            self.add_date = calendar.day # Get date from calendar

        def add_tags(self, tag_list):
            self.tags.extend(tag_list)

        def remove_tags(self, tag):
            ind = self.tags.index(tag)
            del self.tags[ind]

        def change_quality(self, by=-999):
            if by == -999:
                by = self.day_degrade
            self.quality += by

        def quality_level_up(self):
            _last = self.quality
            for name, max_v, min_v in QUALITY:
                if in_range(max_v, min_v, self.quality):
                    break
                _last = max_v
            self.quality = _last

        def change_date(self, date):
            self.pick_date = date

        @property
        def get_quality(self):
            return quality_string(self.quality)

        @property
        def get_next_quality_badge(self):
            _next = self.quality

            for name, max_v, min_v in QUALITY:
                if in_range(max_v, min_v, self.quality):
                    break
                _next = min_v + 1
            return quality_badge(_next)

        @property
        def get_quality_badge(self):
            return quality_badge(self.quality)

        @property
        def sell_price(self):
            if self.quality < 25:
                return int(self.cost * 0.35)
            elif self.quality < 50:
                return int(self.cost * 0.5)
            elif self.quality < 75:
                return int(self.cost * 0.75)
            elif self.quality <= 100:
                return int(self.cost * 0.85)

        @property
        def buy_price(self):
            return int(self.cost * 1.25)
