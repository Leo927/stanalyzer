import pickle
import json
import os
from items.itemdb import ItemDB
from items.item import Item
import requests
import logging
import pandas as pd

class TranslationDb:
    def __init__(self, filename="translate.pickle"):
        self.init_logging()
        self.filename = filename        
        self.items = dict()
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
        response = requests.get("https://smartytitans.com/assets/gameData/texts_en.json")
            
        if response.status_code == 200:
            items = response.json()
            for key,value in items['texts'].items():
                self.items[key] = value
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

    def translate(self, key):
        return self.items[key]
    
    