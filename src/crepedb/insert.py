from sqlalchemy.orm import sessionmaker
from . import models
from .models import Shop, Site, Page, Review
from .util import get_info_from_google_without_phone_number

import re
non_ip_phone_pattern = re.compile(r"^(?!050)")

def getParam(dic, key):
    if key in dic:
        return dic[key]
    return None

def insert_shop(session, shop):
    if getParam(shop, 'tel') is None:
        # 一致検索をかけずに直接放り込みます
        item = Shop()
        item.name = getParam(shop, 'name')
        item.address = getParam(shop, 'address')
        session.add(item)
        session.commit()

        return item

    info = get_info_from_google_without_phone_number(shop['tel'])

    if info is None:
        # 情報取得に失敗。一致検索をかけずに直接放り込みます
        item = Shop()
        item.tel = shop['tel']
        item.name = getParam(shop, 'name')
        item.address = getParam(shop, 'address')
        session.add(item)
        session.commit()

        return item

    item = session.query(Shop).filter(getParam(info, 'place_id') == Shop.place_id).first()
    if item is None:
        item = Shop()
        item.place_id = getParam(info, 'place_id')
        item.name = getParam(info, 'name')
        item.address = getParam(info, 'address')

    if non_ip_phone_pattern.search(shop['tel']):
        item.tel = shop['tel']

    session.add(item)
    session.commit()

    return item


def insert_shops(session, shops):
    place_ids = {item.place_id for item in session.query(Shop).all()}
    items = []
    for shop in shops:
        if getParam(shop, 'tel') is None:
            item = Shop()
            item.name = getParam(shop, 'name')
            item.address = getParam(shop, 'address')
            items.append(item)
            continue

        info = get_info_from_google_without_phone_number(shop['tel'])

        if info is None:
            item = Shop()
            item.tel = shop['tel']
            item.name = getParam(shop, 'name')
            item.address = getParam(shop, 'address')
            items.append(item)
            continue

        if info["place_id"] not in place_ids:
            item = Shop()
            item.place_id = getParam(info, 'place_id')
            item.name = getParam(info, 'name')
            item.address = getParam(info, 'address')
        else:
            item = session.query(Shop).filter(info['place_id'] == Shop.place_id).first()
        if non_ip_phone_pattern.search(shop['tel']):
            item.tel = shop['tel']
 
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
