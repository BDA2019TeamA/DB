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



