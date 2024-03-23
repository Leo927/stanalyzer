from items.item import Item
from items.item import Item
import urllib.parse
import pandas as pd
class ItemDB:
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item):
        self.items[item.uid] = item

    def get_item(self, uid: str):
        return self.items[uid]

    def get_items(self):
        return self.items
    
    def get_items_by_type(self, itemType: str):
        return {uid:item for uid,item in self.items.items() if item.itemType == itemType}
    
    def get_item_type(self, uid: str):
        return self.items[uid].itemType


class itemImageDb:
    def __init__(self, items: ItemDB):
        self.items = items

    def get_item_image(self, uid: str):
        type_name = self.items.get_item_type(uid)

        url = f'https://smartytitans.com/assets/image/Items/{urllib.parse.quote(type_name)}/{urllib.parse.quote(uid)}.png'