import os
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

    def test_insert_site(self):
        site = self.db.insert_site({'name': 'ぐるなび', 'url': 'gnavi.co.jp'})
        self.assertEqual(site.id, 1)
        self.assertEqual(site.name, 'ぐるなび')
        self.assertEqual(site.url, 'gnavi.co.jp')

    def test_insert_sites(self):
        sites = [
            {'name': 'ぐるなび', 'url': 'gnavi.co.jp'},
            {'name': 'Retty', 'url': 'retty.me'}
        ]
        res = self.db.insert_sites(sites)

        self.assertEqual(res[0].id, 1)
        self.assertEqual(res[0].name, 'ぐるなび')
        self.assertEqual(res[0].url, 'gnavi.co.jp')
        self.assertEqual(res[1].id, 2)
        self.assertEqual(res[1].name, 'Retty')
        self.assertEqual(res[1].url, 'retty.me')

    def test_insert_page(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890', 'address': 'ぽぽぽ'})
        site = self.db.insert_site({'name': 'ぐるなび', 'url': 'gnavi.co.jp'})
        page = self.db.insert_page({
            'evaluation': 5,
            'url': 'gnavi.co.jp/shops/1',
            'genre': '食堂',
            'original_id': 'g1',
            'site_id': site.id,
            'shop_id': shop.id
        })

        self.assertEqual(page.evaluation, 5)
        self.assertEqual(page.url, 'gnavi.co.jp/shops/1')
        self.assertEqual(page.original_id, 'g1')
        self.assertEqual(page.genre, '食堂')
        self.assertEqual(page.site_id, 1)
        self.assertEqual(page.shop_id, 1)

    def test_insert_pages(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890', 'address': 'ぽぽぽ'})
        sites = self.db.insert_sites([
            {'name': 'ぐるなび', 'url': 'gnavi.co.jp'},
            {'name': 'Retty', 'url': 'retty.me'}
        ])
        pages = self.db.insert_pages([{
            'evaluation': 5,
            'url': 'gnavi.co.jp/shops/1',
            'genre': '食堂',
            'original_id': 'g1',
            'site_id': sites[0].id,
            'shop_id': shop.id
        },{
            'evaluation': 4,
            'url': 'retty.me/shops/1',
            'genre': '食堂',
            'original_id': 'r1',
            'site_id': sites[1].id,
            'shop_id': shop.id
        }])

        self.assertEqual(pages[0].evaluation, 5)
        self.assertEqual(pages[0].url, 'gnavi.co.jp/shops/1')
        self.assertEqual(pages[0].original_id, 'g1')
        self.assertEqual(pages[0].genre, '食堂')
        self.assertEqual(pages[0].site_id, 1)
        self.assertEqual(pages[0].shop_id, 1)
        self.assertEqual(pages[1].evaluation, 4)
        self.assertEqual(pages[1].url, 'retty.me/shops/1')
        self.assertEqual(pages[1].original_id, 'r1')
        self.assertEqual(pages[1].genre, '食堂')
        self.assertEqual(pages[1].site_id, 2)
        self.assertEqual(pages[1].shop_id, 1)

    def test_insert_review(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890', 'address': 'ぽぽぽ'})
        site = self.db.insert_site({'name': 'ぐるなび', 'url': 'gnavi.co.jp'})
        page = self.db.insert_page({
            'evaluation': 5,
            'url': 'gnavi.co.jp/shops/1',
            'genre': '食堂',
            'original_id': 'g1',
            'site_id': site.id,
            'shop_id': shop.id
        })
        review = self.db.insert_review({
            'reviewer': 'po',
            'comment': 'うまい',
            'evaluation': 3,
            'original_id': 2,
            'page_id': page.id
        })

        self.assertEqual(review.reviewer, 'po')
        self.assertEqual(review.comment, 'うまい')
        self.assertEqual(review.evaluation, 3)
        self.assertEqual(review.original_id, 2)
        self.assertEqual(review.page_id, 1)

    def test_insert_reviews(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890', 'address': 'ぽぽぽ'})
        site = self.db.insert_site({'name': 'ぐるなび', 'url': 'gnavi.co.jp'})
        page = self.db.insert_page({
            'evaluation': 5,
            'url': 'gnavi.co.jp/shops/1',
            'genre': '食堂',
            'original_id': 'g1',
            'site_id': site.id,
            'shop_id': shop.id
        })
        reviews = self.db.insert_reviews([{
            'reviewer': 'reviewer1',
            'comment': 'うまい',
            'evaluation': 3,
            'original_id': 2,
            'page_id': page.id
        }, {
            'reviewer': 'reviewer2',
            'comment': '内装が綺麗',
            'evaluation': 5,
            'original_id': 3,
            'page_id': page.id
        }])

        self.assertEqual(reviews[0].reviewer, 'reviewer1')
        self.assertEqual(reviews[0].comment, 'うまい')
        self.assertEqual(reviews[0].evaluation, 3)
        self.assertEqual(reviews[0].original_id, 2)
        self.assertEqual(reviews[0].page_id, 1)
        self.assertEqual(reviews[1].reviewer, 'reviewer2')
        self.assertEqual(reviews[1].comment, '内装が綺麗')
        self.assertEqual(reviews[1].evaluation, 5)
        self.assertEqual(reviews[1].original_id, 3)
        self.assertEqual(reviews[1].page_id, 1)

    def test_insert_revierws_am(self):
        shop = self.db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890', 'address': 'ぽぽぽ'})
        site = self.db.insert_site({'name': 'ぐるなび', 'url': 'gnavi.co.jp'})
        page = self.db.insert_page({
            'evaluation': 5,
            'url': 'gnavi.co.jp/shops/1',
            'genre': '食堂',
            'original_id': 'g1',
            'site_id': site.id,
            'shop_id': shop.id
        })
        reviews = self.db.insert_reviews_am([{
            'reviewer': 'reviewer1',
            'comment': 'うまい',
            'evaluation': 3,
            'page_original_id': 'g1',
        }, {
            'reviewer': 'reviewer2',
            'comment': '内装が綺麗',
            'evaluation': 5,
            'page_original_id': 'g1',
        }])

        self.assertEqual(reviews[0].page_id, page.id)
        self.assertEqual(reviews[1].page_id, page.id)

    # 手元では通ってます
    @unittest.skipUnless(os.getenv("GOOGLE_MAPS_API_KEY"), "Please set your Google Maps API Key.")
    def test_insert_pages_am(self):
        sites = self.db.insert_sites([
            {'name': 'ぐるなび', 'url': 'gnavi.co.jp'},
            {'name': 'Retty', 'url': 'retty.me'}
        ])
        pages = self.db.insert_pages_am([{
            'site_name': 'ぐるなび',
            'tel': '03-5731-5230',
            'name': '九絵',
            'address': '東京都目黒区大岡山2-2-1'
        },{
            'site_name': 'Retty',
            'tel': '03-5731-5230',
            'name': '漁師料理 九絵',
            'address': '東京都目黒区大岡山２-２-１'
        }])

        shop = self.db.select_shop()[0]
        self.assertEqual(shop.name, '漁師料理 九絵')
        self.assertEqual(shop.address, '日本、〒152-0033 東京都目黒区大岡山２丁目２−１')
        self.assertEqual(shop.tel, '03-5731-5230')
        self.assertEqual(shop.place_id, 'ChIJlWQdPS71GGARNCq9u5kpvUY')
        self.assertEqual(shop.latitude, "35.607969")
        self.assertEqual(shop.longitude, "139.6855287")
        self.assertEqual(pages[0].site_id, sites[0].id)
        self.assertEqual(pages[1].site_id, sites[1].id)
        self.assertEqual(pages[0].shop_id, shop.id)
        self.assertEqual(pages[1].shop_id, shop.id)


