from . import insert
from . import select
from . import util
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine
from .models import Base, Shop, Site, Page, Review

import re
non_ip_phone_pattern = re.compile(r"^(?!050)")

class CrepeDB:
    def __init__(self, path):
        self.path = path
        try:
            self.engine = create_engine(path)
        except:
            print('Error', file=sys.stderr)
        Base.metadata.create_all(self.engine)  # migrate

        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )

    def __del__(self):
        if self.session:
            self.session.close()

    def insert_shop(self, shop):
        return insert.insert_shop(self.session, shop)

    def insert_shops(self, shops):
        return insert.insert_shops(self.session, shops)

    def insert_site(self, site):
        return insert.insert_site(self.session, site)

    def insert_sites(self, sites):
        return insert.insert_sites(self.session, sites)

    def insert_page(self, page):
        return insert.insert_page(self.session, page)

    def insert_pages(self, pages):
        return insert.insert_pages(self.session, pages)

    # with auto merging
    def insert_page_am(self, page):
        site = self.select_site_from_name(page['site_name'])
        page['site_id'] = site.id

        info = util.get_info_from_google_without_phone_number(page['tel'])
        if info is not None:
            shop = self.select_shop_from_place_id(info['place_id'])
            if shop is None:
                shop = self.insert_shop({
                    'name': info['name'],
                    'address': info['address'],
                    'place_id': info['place_id'],
                    'lat': info['lat'],
                    'lng': info['lng'],
                    'tel': page['tel'] if non_ip_phone_pattern.search(page['tel']) else None
                })
            page['shop_id'] = shop.id

        return insert.insert_page(self.session, page)

    def insert_pages_am(self, pages):
        res = []
        for page in pages:
            res.append(self.insert_page_am(page))
        return res

    def insert_review(self, review):
        return insert.insert_review(self.session, review)

    def insert_reviews(self, reviews):
        return insert.insert_reviews(self.session, reviews)

    def insert_review_am(self, review):
        page = self.select_page_from_original_id(review['page_original_id'])
        review['page_id'] = page.id 
        return insert.insert_review(self.session, review)

    def insert_reviews_am(self, reviews):
        res = []
        for review in reviews:
            res.append(self.insert_review_am(review))
        return res

    def select_shop(self, limit=None, pagenum=1, order_by=Shop.id, descend=False):
        return select.select_shop(self.session, limit, pagenum, order_by, descend)

    def select_shop_lazy(self, limit=1, order_by=Shop.id, descend=False):
        return select.select_shop_lazy(self.session, limit, order_by, descend)

    def select_site(self, limit=None, pagenum=1, order_by=Site.id, descend=False):
        return select.select_site(self.session, limit, pagenum, order_by, descend)

    def select_site_lazy(self, limit=None, pagenum=1, order_by=Page.id, descend=False):
        return select.select_site_lazy(self.session, limit, order_by, descend)

    def select_page(self, limit=None, pagenum=1, order_by=Review.id, descend=False):
        return select.select_page(self.session, limit, pagenum, order_by, descend)

    def select_page_lazy(self, limit=None, order_by=Page.id, descend=False):
        return select.select_page_lazy(self.session, limit, order_by, descend)

    def select_review(self, limit=None, pagenum=1, order_by=Page.id, descend=False):
        return select.select_review(self.session, limit, pagenum, order_by, descend)

    def select_review_lazy(self, limit=None, order_by=Page.id, descend=False):
        return select.select_review_lazy(self.session, limit, order_by, descend)

    def select_shop_from_place_id(self, place_id):
        return select.select_shop_from_place_id(self.session, place_id)

    def select_site_from_name(self, name):
        return select.select_site_from_name(self.session, name)

    def select_page_from_original_id(self, original_id):
        return select.select_page_from_original_id(self.session, original_id)
