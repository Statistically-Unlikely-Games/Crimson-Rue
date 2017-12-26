init python:

    class BuySell(Action):

        def __init__(self, item, buyer, seller):
            self.item = item
            self.buyer = buyer
            self.seller = seller

        def __call__(self):
            self.seller.buy_item(self.item)
            self.buyer.sell_item(self.item)

            if self.buyer.is_player:
                item_sell_event(self.item)
            else:
                item_buy_event(self.item)

            renpy.restart_interaction()

        def get_sensitive(self):
            if self.buyer.is_player:
                return self.buyer.money >= self.item.sell_price
            return self.buyer.money >= self.item.buy_price
