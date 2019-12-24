import unittest
from crepedb import CrepeDB


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.db = CrepeDB('sqlite:///:memory:')

    def test_insert_shop(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890'})
        self.assertEqual(shop.id, 1)
        self.assertEqual(shop.name, 'Crepe食堂')
        self.assertEqual(shop.address, None)
        self.assertEqual(shop.tel, '01234567890')

    def test_insert_shops(self):
        shops = [
            {'name': 'Crepe喫茶', 'tel': '0312345678'},
            {'name': 'Crepeレストラン', 'address': '東京都目黒区'},
        ]
        res = self.db.insert_shops(shops)

        self.assertEqual(res[0].id, 1)
        self.assertEqual(res[0].name, 'Crepe喫茶')
        self.assertEqual(res[0].address, None)
        self.assertEqual(res[0].tel, '0312345678')
        self.assertEqual(res[1].id, 2)
        self.assertEqual(res[1].name, 'Crepeレストラン')
        self.assertEqual(res[1].address, '東京都目黒区')
        self.assertEqual(res[1].tel, None)

