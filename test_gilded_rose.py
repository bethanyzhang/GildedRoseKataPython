# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    # Test case 1 - logical error
    def test_aged_brie_should_not_decrease_quality(self):
        items = [Item("Aged Brie", 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        brie_item = items[0]
        self.assertEqual(40, brie_item.quality)
        self.assertEqual(5, brie_item.sell_in)
        self.assertEqual("Aged Brie", brie_item.name)

    # Test case 2 - logical error
    def test_sulfuras_hand_of_ragnaros_should_not_decrease_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(2, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)
    
    # Test case 3 - logical error
    def test_sulfuras_should_not_mismatch_name(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(79, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfurassssss", sulfuras_item.name)

    # Test case 4 - syntax error
    def test_gilded_rose_list_all_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_quality()
        self.assertEqual(["Sulfuras"], all_items)




if __name__ == '__main__':
    unittest.main()
