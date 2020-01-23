from sqlalchemy.orm import sessionmaker
from . import models
from .models import Shop, Site, Page, Review, ReviewScore, ShopScore
from .util import get_info_from_google_without_phone_number

def getParam(dic, key):
    if key in dic:
        return dic[key]
    return None

def insert_shop(session, shop):
    item = Shop()
    item.name = getParam(shop, 'name')
    item.address = getParam(shop, 'address')
    item.tel = getParam(shop, 'tel')
    item.place_id = getParam(shop, 'place_id')

    session.add(item)
    session.commit()

    return item

def insert_shops(session, shops):
    items = []
    for shop in shops:
        item = Shop()
        item.name = getParam(shop, 'name')
        item.address = getParam(shop, 'address')
        item.tel = getParam(shop, 'tel')
        item.place_id = getParam(shop, 'place_id')
 
        items.append(item)

    session.add_all(items)
    session.commit()

    return items


def insert_site(session, site):
    item = Site()

    item.name = getParam(site, 'name')
    item.url = getParam(site, 'url')

    session.add(item)
    session.commit()

    return item


def insert_sites(session, sites):
    items = []

    for site in sites:
        item = Site()

        item.name = getParam(site, 'name')
        item.url = getParam(site, 'url')
        items.append(item)

    session.add_all(items)
    session.commit()

    return items


def insert_page(session, page):
    item = Page()

    item.evaluation = getParam(page, 'evaluation')
    item.url = getParam(page, 'url')
    item.genre = getParam(page, 'genre')
    item.original_id = getParam(page, 'original_id')
    item.site_id = getParam(page, 'site_id')
    item.shop_id = getParam(page, 'shop_id')

    session.add(item)
    session.commit()

    return item

def insert_pages(session, pages):
    items = []
    for page in pages:
        item = Page()

        item.evaluation = getParam(page, 'evaluation')
        item.url = getParam(page, 'url')
        item.genre = getParam(page, 'genre')
        item.site_id = getParam(page, 'site_id')
        item.shop_id = getParam(page, 'shop_id')
        item.original_id = getParam(page, 'original_id')
        items.append(item)

    session.add_all(items)
    session.commit()

    return items

def insert_review(session, review):
    item = Review()

    item.reviewer = getParam(review, 'reviewer')
    item.comment = getParam(review, 'comment')
    item.evaluation = getParam(review, 'evaluation')
    item.original_id = getParam(review, 'original_id')
    item.page_id = getParam(review, 'page_id')

    session.add(item)
    session.commit()

    return item

def insert_reviews(session, reviews):
    items = []

    for review in reviews:
        item = Review()

        item.reviewer = getParam(review, 'reviewer')
        item.comment = getParam(review, 'comment')
        item.evaluation = getParam(review, 'evaluation')
        item.original_id = getParam(review, 'original_id')
        item.page_id = getParam(review, 'page_id')
        items.append(item)

    session.add_all(items)
    session.commit()

    return items

def insert_review_score(session, score):
    item = ReviewScore()
    item.review_id = getParam(score, 'review_id')
    item.category = getParam(score, 'category')
    item.score = getParam(score, 'score')

    session.add(item)
    session.commit()

    return item

def insert_review_scores(session, scores):
    items = []
    for score in scores:
        item = ReviewScore()
        item.review_id = getParam(score, 'review_id')
        item.category = getParam(score, 'category')
        item.score = getParam(score, 'score')
        items.append(item)

    session.add_all(items)
    session.commit()

    return items

def insert_shop_score(session, score):
    item = ShopScore()
    item.shop_id = getParam(score, 'shop_id')
    item.category = getParam(score, 'category')
    item.score = getParam(score, 'score')

    session.add(item)
    session.commit()

    return item

def insert_shop_scores(session, scores):
    items = []
    for score in scores:
        item = ShopScore()
        item.shop_id = getParam(score, 'shop_id')
        item.category = getParam(score, 'category')
        item.score = getParam(score, 'score')
        items.append(item)

    session.add_all(items)
    session.commit()

    return items

