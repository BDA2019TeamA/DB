import unittest
from crepedb import CrepeDB
from crepedb.models import Shop


class TestSelect(unittest.TestCase):
    def setUp(self):
        self.db = CrepeDB('sqlite:///:memory:')

    def test_select_shop(self):
        # insertは成功する前提
        shops = [
            {'name': 'Crepe食堂', 'tel': '01234567890'},
            {'name': 'Crepe喫茶', 'tel': '0312345678'},
            {'name': 'Crepeレストラン', 'address': '東京都目黒区'},
        ]
        inserted = self.db.insert_shops(shops)

        # sorted(['食堂','喫茶','レストラン'],reverse=True)[0] > '食堂'
        res_shops = self.db.select_shop(order_by=Shop.name, descend=True)
        self.assertEqual(res_shops[0], inserted[0])

        res_shop = self.db.select_shop(limit=1, pagenum=2)
        self.assertEqual(res_shop[0], inserted[2])

    def test_select_shop_lazy(self):
        shops = [
            {'name': 'Crepe食堂', 'tel': '01234567890'},
            {'name': 'Crepe喫茶', 'tel': '0312345678'},
            {'name': 'Crepeレストラン', 'address': '東京都目黒区'},
            {'name': 'Crepeレストラン 2号店', 'address': '東京都目黒区'},
            {'name': 'Crepeレストラン 3号店', 'address': '東京都目黒区'},
        ]
        insertedShops = self.db.insert_shops(shops)

        for inserted, selected in zip(range(0, len(insertedShops), 2),
                                      self.db.select_shop_lazy(limit=2)):
            self.assertEqual(insertedShops[inserted:inserted + 2], selected)

        insertedShops.reverse()

        for inserted, selected in zip(
                insertedShops, self.db.select_shop_lazy(limit=1,
                                                        descend=True)):
            self.assertEqual(inserted, selected[0])

    # 他はロジックが全く一緒なので飛ばします

    def test_select_shop_from_place_id(self):
        self.db.insert_shop({
            'name': '漁師料理 九絵',
            'address': '日本、〒152-0033 東京都目黒区大岡山２丁目２−１',
            'tel': '03-5731-5230',
            'place_id': 'ChIJlWQdPS71GGARNCq9u5kpvUY'
        })
        shop = self.db.select_shop_from_place_id('ChIJlWQdPS71GGARNCq9u5kpvUY')
        self.assertEqual(shop.name, '漁師料理 九絵')
        self.assertEqual(shop.address, '日本、〒152-0033 東京都目黒区大岡山２丁目２−１')
        self.assertEqual(shop.tel, '03-5731-5230')

    def test_select_site_from_name(self):
        self.db.insert_site({
            'name': 'ぐるなび', 'url': 'gnavi.co.jp'
        })
        site = self.db.select_site_from_name('ぐるなび')
        self.assertEqual(site.url, 'gnavi.co.jp')

    def test_select_page_from_original_id(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890', 'address': 'ぽぽぽ'})
        site = self.db.insert_site({'name': 'ぐるなび', 'url': 'gnavi.co.jp'})
        pages = self.db.insert_page({
            'evaluation': 5,
            'url': 'gnavi.co.jp/shops/1',
            'genre': '食堂',
            'original_id': 'g1',
            'site_id': site.id,
            'shop_id': shop.id
        })

        page = self.db.select_page_from_original_id('g1')
        self.assertEqual(page.shop.name, 'Crepe食堂')
        self.assertEqual(page.site.name, 'ぐるなび')
        self.assertEqual(page.genre, '食堂')
