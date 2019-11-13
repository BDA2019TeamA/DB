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
