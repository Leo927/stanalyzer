import unittest
from listing import Quality

class TestQuality(unittest.TestCase):
    def test_ranking_to_rarity(self):
        self.assertEqual(Quality.ranking_to_rarity(0), Quality.COMMON)
        self.assertEqual(Quality.ranking_to_rarity(1), Quality.UNCOMMON)
        self.assertEqual(Quality.ranking_to_rarity(2), Quality.FLAWLESS)
        self.assertEqual(Quality.ranking_to_rarity(3), Quality.EPIC)
        self.assertEqual(Quality.ranking_to_rarity(4), Quality.LEGENDARY)

    def test_get_ranking(self):
        self.assertEqual(Quality.get_ranking(Quality.COMMON), 0)
        self.assertEqual(Quality.get_ranking(Quality.UNCOMMON), 1)
        self.assertEqual(Quality.get_ranking(Quality.FLAWLESS), 2)
        self.assertEqual(Quality.get_ranking(Quality.EPIC), 3)
        self.assertEqual(Quality.get_ranking(Quality.LEGENDARY), 4)

    def test_add_one(self):
        self.assertEqual(Quality.add_one(Quality.COMMON), Quality.UNCOMMON)
        self.assertEqual(Quality.add_one(Quality.UNCOMMON), Quality.FLAWLESS)
        self.assertEqual(Quality.add_one(Quality.FLAWLESS), Quality.EPIC)
        self.assertEqual(Quality.add_one(Quality.EPIC), Quality.LEGENDARY)
        with self.assertRaises(ValueError):
            Quality.add_one(Quality.LEGENDARY)
    
    def test_equal(self):
        self.assertEqual(Quality.COMMON, Quality.COMMON)
        self.assertEqual(Quality.UNCOMMON, Quality.UNCOMMON)

if __name__ == '__main__':
    unittest.main()