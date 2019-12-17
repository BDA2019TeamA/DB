import unittest
from crepedb.util import normalize, partial_eq

class TestAddress(unittest.TestCase):
    def test(self):
        # 叙々苑渋谷店
        # Hotpepper vs Retty
        self.assertTrue(partial_eq(
            normalize("東京都渋谷区宇田川町２６-２ サンルイビル８階"),
            normalize("東京都渋谷区宇田川町２６-２ サンルイビル ８F")
        ))
        # ぐるなび vs Hotpepper
        self.assertTrue(partial_eq(
            normalize("東京都渋谷区宇田川町２６-２ サンルイビル８階"),
            normalize("東京都渋谷区宇田川町26-2 サンルイビル8F")
        ))
        # ぐるなび vs Retty
        self.assertTrue(partial_eq(
            normalize("東京都渋谷区宇田川町２６-２ サンルイビル ８F"),
            normalize("東京都渋谷区宇田川町26-2 サンルイビル8F")
        ))
        
        # 大衆酒場ちばチャン 渋谷店
        # Retty vs ぐるなび
        self.assertTrue(partial_eq(
            normalize("東京都渋谷区宇田川町１３-８"),
            normalize("東京都渋谷区宇田川町13-8 ちとせ会館ビル4F")
        ))
        # ぐるなび vs Hotpepper
        self.assertTrue(partial_eq(
            normalize("東京都渋谷区宇田川町13-8 ちとせ会館ビル4F"),
            normalize("東京都渋谷区宇田川町13-8　ちとせ会館4F")
        ))
        # Retty vs Hotpepper
        self.assertTrue(partial_eq(
            normalize("東京都渋谷区宇田川町１３-８"),
            normalize("東京都渋谷区宇田川町13-8　ちとせ会館4F")
        ))
