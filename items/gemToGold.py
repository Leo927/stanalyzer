from items.pickleItemDb import ItemDB, Item, TranslationDb, PickleItemDb
from items.market import Market, Quality, Currency, ListingType, URIListingSource, NoListingAvailableException
from itertools import product
import pandas as pd

class GemToGoldConversion:
    itemDb: ItemDB
    market: Market
    def __init__(self, itemDb: ItemDB, market: Market):
        self.itemDb = itemDb
        self.market = market
    
    def find_best_conversion_rate(self):
        self.market.refresh_listings()
        # find the best item and ratio at each item tier
        best_rates = dict()
        for item,quality in product(self.itemDb.items.values(), list(Quality)):
            best_rate = 0 if item.tier not in best_rates else best_rates[item.tier][0]
            try:
                rate= self.calculate_conversion_rate(item, quality)
                if rate > best_rate:
                    best_rates[item.tier] = (rate, item, quality)
            except NoListingAvailableException as e:
                pass        
        return best_rates
    
    def calculate_conversion_rate(self, item: Item, quality: Quality):
        buy_gem_value = self.market.get_current_price(item.uid, quality, Currency.GEMS, ListingType.OFFER)
        sell_gold_value = self.market.get_current_price(item.uid, quality, Currency.GOLD, ListingType.REQUEST)
        return sell_gold_value / buy_gem_value

if __name__ == '__main__':
    itemDb = PickleItemDb()
    market = Market(URIListingSource())
    gemToGoldConversion = GemToGoldConversion(itemDb, market)
    best_rates = gemToGoldConversion.find_best_conversion_rate()
    for tier, (best_rate, best_item, quality) in best_rates.items():
        print(f"Best item: {best_item.short_description()} {quality} {best_rate:,.0f} gold per gem at tier {tier}")