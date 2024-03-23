from items.item import Item
from items.itemdb import ItemDB
from items.pickleItemDb import PickleItemDb
from items.market import Market, ListingType, URIListingSource, NoListingAvailableException
from items.listing import Quality, Listing, Currency
from dataclasses import dataclass
import logging

@dataclass
class ProfitSet:
    item: str
    fromQuality: Quality
    toQuality: Quality
    fromCurrency: Currency
    toCurrency: Currency

    def __init__(self, item: str, quality1: Quality, quality2: Quality, currency1: Currency, currency2: Currency):
        self.item = item
        self.fromQuality = quality1
        self.toQuality = quality2
        self.fromCurrency = currency1
        self.toCurrency = currency2
    
    def __hash__(self) -> int:
        return hash((self.item, self.fromQuality, self.toQuality, self.fromCurrency, self.toCurrency))

class FusionProfitAnalyzer:
    gold_per_gem = 1500000
    def __init__(self, itemdb: ItemDB, market: Market):
        self.itemdb = itemdb
        self.market = market
        self.profit = dict()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        
        self.fusion_need_items = {Quality.COMMON: 4, Quality.UNCOMMON: 5, Quality.FLAWLESS: 5, Quality.EPIC: 6}
    
    def get_profitable_fusions(self):
        # for each item in the itemdb. for each quality of the item. find the profit of fusing the item with the same quality item
        for uid in self.itemdb.get_items():
            for quality in [Quality.COMMON, Quality.UNCOMMON, Quality.FLAWLESS, Quality.EPIC]:
                self.get_profit_to_fuse(uid, quality, Quality.add_one(quality), Currency.GOLD, Currency.GOLD)
                self.get_profit_to_fuse(uid, quality, Quality.add_one(quality), Currency.GOLD, Currency.GEMS)
                self.get_profit_to_fuse(uid, quality, Quality.add_one(quality), Currency.GEMS, Currency.GEMS)
            
        return self.profit
    
    def get_profit_to_fuse(self, uid, quality1: Quality, quality2: Quality, currency1: Currency, currency2: Currency):
        try:
            # find the price of the item in the market
            buy_price = self.market.get_current_price(uid, quality1, currency1, ListingType.OFFER)
            # find the price of the fusion item in the market
            sell_price = self.market.get_current_price(uid, quality2, currency2, ListingType.REQUEST)
            # calculate the profit
            profit = self.calculate_profit(buy_price, currency1, sell_price, currency2)
            if profit > 0:
                self.profit[ProfitSet(uid, quality1, quality2, currency1, currency2)] = profit
        except NoListingAvailableException as e:
            self.logger.debug(e)
    
    def convert_to_gold_price(self, price, currency):
        return price if currency == Currency.GOLD else price * self.gold_per_gem

    def calculate_profit(self, cost, currency1, revenue, currency2):
        return self.convert_to_gold_price(revenue, currency2) - self.convert_to_gold_price(cost, currency1)
    
    def add_profit(self, uid: str, quality1: Quality, quality2: Quality, currency1: Currency, currency2: Currency, profit: int):
        self.profit[ProfitSet(uid, quality1, quality2, currency1, currency2)] = profit
        
    

if __name__ == "__main__":
    itemdb = PickleItemDb('./items.pickle')
    listing_source = URIListingSource()
    market = Market(listing_source)
    market.refresh_listings()
    analyzer = FusionProfitAnalyzer(itemdb, market)
    f = analyzer.get_profitable_fusions()
    print(f)


