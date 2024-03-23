import unittest
from unittest.mock import MagicMock
from market import Market, Listing, Currency, ListingSourceInterface, NoListingAvailableException, Quality, ListingType, URIListingSource
from datetime import datetime


class TestMarket(unittest.TestCase):
    def setUp(self):
        # Create an instance of your market class and initialize any necessary data
        self.listing_source = ListingSourceInterface()
        self.market = Market(self.listing_source)
    
    def test_no_listings(self):
        self.listing_source.get_listings = MagicMock(return_value=[])
        # Test when no listings are found
        with self.assertRaises(NoListingAvailableException):
            self.market.get_current_price(3, 'Medium', Currency.GOLD, ListingType.OFFER)

    def test_get_current_gold_price(self):
        # Test when one listing is found
        uid = "testItem"
        listing1 = Listing(uid=uid, tType=ListingType.REQUEST, goldPrice=15400, gemsPrice=7642, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        listing2 = Listing(uid=uid, tType=ListingType.OFFER, goldPrice=15401, gemsPrice=7641, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.listing_source.get_listings = MagicMock(return_value=[listing1, listing2])
        self.assertEqual(self.market.get_current_price(uid, Quality.COMMON, Currency.GOLD, ListingType.REQUEST), 15400)
        self.assertEqual(self.market.get_current_price(uid, Quality.COMMON, Currency.GOLD, ListingType.OFFER), 15401)

    def test_get_current_gem_price(self):
        # Test when one listing is found
        uid = "testItem"
        listing1 = Listing(uid=uid, tType=ListingType.REQUEST, goldPrice=15400, gemsPrice=7642, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        listing2 = Listing(uid=uid, tType=ListingType.OFFER, goldPrice=15401, gemsPrice=7641, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.listing_source.get_listings = MagicMock(return_value=[listing1, listing2])
        self.assertEqual(self.market.get_current_price(uid, Quality.COMMON, Currency.GEMS, ListingType.REQUEST), 7642)
        self.assertEqual(self.market.get_current_price(uid, Quality.COMMON, Currency.GEMS, ListingType.OFFER), 7641)

    def test_get_current_gold_price_when_multiple_listing_available_with_different_update_time(self):
        # Test when multiple listings are found
        uid = "testItem"
        listing1 = Listing(uid=uid, tType=ListingType.REQUEST, goldPrice=15400, gemsPrice=7642, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        listing2 = Listing(uid=uid, tType=ListingType.REQUEST, goldPrice=15401, gemsPrice=7641, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.listing_source.get_listings = MagicMock(return_value=[listing1, listing2])
        self.assertEqual(self.market.get_current_price(uid, Quality.COMMON, Currency.GOLD, ListingType.REQUEST), 15400)

    def test_get_current_gold_price_when_multiple_listing_available_with_same_update_time(self):
        # Test when multiple listings are found
        uid = "testItem"
        listing1 = Listing(uid=uid, tType=ListingType.REQUEST, goldPrice=15400, gemsPrice=7642, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        listing2 = Listing(uid=uid, tType=ListingType.REQUEST, goldPrice=15401, gemsPrice=7641, tag1=None, updatedAt=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        self.listing_source.get_listings = MagicMock(return_value=[listing1, listing2])
        self.assertEqual(self.market.get_current_price(uid, Quality.COMMON, Currency.GOLD, ListingType.REQUEST), 15400)
        
class TestUriListing(unittest.TestCase):
    def test_can_get_listings(self):
        # Test if the URIListingSource can get listings
        uri_listing = URIListingSource()
        listings = uri_listing.get_listings()
        self.assertTrue(len(listings) > 0)
        self.assertIsInstance(listings[0], Listing)

if __name__ == '__main__':
    unittest.main()