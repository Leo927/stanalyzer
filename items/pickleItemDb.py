import pickle
import json
import os
from items.itemdb import ItemDB
from items.item import Item
import requests
import logging
import pandas as pd
from items.translation import TranslationDb

class PickleItemDb(ItemDB):
    def __init__(self, filename="items.pickle"):
        self.init_logging()
        self.filename = filename        
        self.translationDb = TranslationDb()
        self.items = {}
        self.load()

    def init_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def load(self):
        if os.path.exists(self.filename):
            self.load_from_cache()
        else:
            self.load_from_server()

    def load_from_server(self):
        response = requests.get("https://smartytitans.com/assets/gameData/items.json")
            
        if response.status_code == 200:
            items = response.json()
            for name in items:
                item = items[name]
                uid = item['uid']
                item['name'] = self.translationDb.translate(f'{uid}_name')
                self.items[uid] = Item(item)
            self.logger.info(f"Loaded {len(self.items)} items from server")
            self.save()
        else:
                    # Handle the error case
            raise Exception("Failed to fetch items from server")
    

    def load_from_cache(self):
        with open(self.filename, 'rb') as f:
            self.items = pickle.load(f)
        self.logger.info(f"Loaded {len(self.items)} items from pickle file")

    def save(self):
        pickle.dump(self.items, open(self.filename, "wb"))
        self.logger.info("Saved items to pickle file")

    def add_item(self, item: Item):
        super().add_item(item)
        self.save()
    

if __name__ == "__main__":
    db = PickleItemDb()
    print(db.get_item('shortsword').name)