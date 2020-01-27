import unittest
from crepedb import CrepeDB


class TestModels(unittest.TestCase):
    def setUp(self):
        self.db = CrepeDB('sqlite:///:memory:')

    def test_tableList(self):
        self.assertEqual(set(['pages', 'reviews', 'shops', 'sites', 'reviewscores', 'shopscores']),
                         set(self.db.engine.table_names()))
