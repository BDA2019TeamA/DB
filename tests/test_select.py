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
