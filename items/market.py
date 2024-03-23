import requests
from listing import Quality,Listing, Currency, ListingType
from datetime import datetime
from enum import Enum

class ListingSourceInterface:
    def get_listings(self) -> list[Listing]:
        raise NotImplementedError("Subclasses must implement this method")
    
class URIListingSource(ListingSourceInterface):
    def __init__(self):
        self.uri = "https://smartytitans.com/api/item/last/all"
        
    def get_listings(self) -> list[Listing]:
        response = requests.get(self.uri)
        if response.status_code == 200:
            return [Listing.from_dict(i) for i in response.json()['data']]
        else:
            raise Exception("Failed to fetch items from server")
        

class Market:
    def __init__(self, listing_source: ListingSourceInterface):
        self.listing_source = listing_source
        self.listings = []
    
    def refresh_listings(self):
        self.listings = self.listing_source.get_listings()
    
    def get_current_price(self, uid: str, quality: Quality, currency: Currency, list_type:ListingType):
        listings = list(filter(lambda l:uid==l.uid and l.quality == quality and l.type == list_type , self.listings))
        if len(listings) <= 0:
            raise NoListingAvailableException(f"No listings found for {quality} {uid} with {currency} for {list_type}")
        most_recent_listing = max(listings, key=lambda l: self.convert_datetime(l.updatedAt))
        if currency == Currency.GOLD:
            if most_recent_listing.goldPrice == None:
                raise NoListingAvailableException(f"No listings found for {quality} {uid} with {currency} for {list_type}")
            return most_recent_listing.goldPrice
        elif currency == Currency.GEMS:
            if most_recent_listing.gemsPrice == None:
                raise NoListingAvailableException(f"No listings found for {quality} {uid} with {currency} for {list_type}")
            return most_recent_listing.gemsPrice
        else:
            raise Exception("Invalid currency")

    def convert_datetime(self, date):
        return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

class NoListingAvailableException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
    
    
    