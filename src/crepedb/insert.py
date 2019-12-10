from sqlalchemy.orm import sessionmaker
from . import models
from .models import Shop, Site, Page, Review


def getParam(dic, key):
    if key in dic:
        return dic[key]
    return None


def insert_shop(session, shop):
    item = session.query(Shop).filter(shop.tel == Shop.tel).first()
    if item is None:
        item = Shop()
        item.name = getParam(shop, 'name')
        item.address = getParam(shop, 'address')
        item.tel = getParam(shop, 'tel')

        session.add(item)
        session.commit()

    return item


def insert_shops(session, shops):
    tels = {item.tel for item in session.query(Shop).all()}
    items = []
    for shop in shops:
        if shop.tel not in tels:
            item = Shop()
            item.name = getParam(shop, 'name')
            item.address = getParam(shop, 'address')
            item.tel = getParam(shop, 'tel')
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


def insert_sites(session, sites):
    items = []

    for site in sites:
        item = Site()

        item.name = getParam(site, 'name')
        item.url = getParam(site, 'url')
        items.append(item)

    session.add_all()
    session.commit()


def insert_page(session, page):
    item = Page()

    item.evaluation = getParam(page, 'evaluation')
    item.url = getParam(page, 'url')
    item.genre = getParam(page, 'genre')
    site_id = getParam(page, 'site_id')
    shop_id = getParam(page, 'shop_id')

    session.add(item)
    session.commit()


def insert_pages(session, pages):
    items = []
    for page in pages:
        item = Page()

        item.evaluation = getParam(page, 'evaluation')
        item.url = getParam(page, 'url')
        item.genre = getParam(page, 'genre')
        site_id = getParam(page, 'site_id')
        shop_id = getParam(page, 'shop_id')
        items.push(item)

    session.add_all(items)
    session.commit()


def insert_review(session, review):
    item = Review()

    reviewer = getParam(review, 'reviewer')
    comment = getParam(review, 'comment')
    evaluation = getParam(review, 'evaluation')
    original_id = getParam(review, 'original_id')
    page_id = getParam(review, 'page_id')

    session.add(item)
    session.commit()


def insert_reviews(session, reviews):
    items = []

    for review in reviews:
        item = Review()

        reviewer = getParam(review, 'reviewer')
        comment = getParam(review, 'comment')
        evaluation = getParam(review, 'evaluation')
        original_id = getParam(review, 'original_id')
        page_id = getParam(review, 'page_id')

    session.add_all(items)
    session.commit()
