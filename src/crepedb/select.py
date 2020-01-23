import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import sessionmaker
from .models import Shop, Site, Page, Review, ReviewScore, ShopScore


def select_shop(session,
                limit=None,
                pagenum=1,
                order_by=Shop.id,
                descend=False):
    order = desc if descend else asc
    if limit is None:
        return session.query(Shop) \
                      .order_by(order(order_by)) \
                      .all()
    else:
        return session.query(Shop) \
                      .order_by(order(order_by)) \
                      .limit(limit) \
                      .offset(limit * pagenum) \
                      .all()


def select_shop_lazy(session, limit=None, order_by=Shop.id, descend=False):
    shops = None
    last = None

    while True:
        query = session.query(Shop) \
            .order_by(desc(order_by) if descend else asc(order_by))

        if shops and descend:
            query = query.filter(order_by < last)
        if shops and not descend:
            query = query.filter(order_by > last)

        shops = query.limit(limit).all()

        if not shops:
            break

        last = getattr(shops[-1], order_by.key)
        yield shops

def select_shop_from_place_id(session, place_id):
    return session.query(Shop) \
        .filter(Shop.place_id == place_id) \
        .scalar()

def select_site_from_name(session, name):
    return session.query(Site) \
        .filter(Site.name == name) \
        .scalar()

def select_page_from_original_id(session, original_id):
    return session.query(Page) \
        .filter(Page.original_id == original_id) \
        .scalar()

def select_review_score(session,
                limit=None,
                pagenum=1,
                order_by=ReviewScore.id,
                descend=False):
    order = desc if descend else asc
    if limit is None:
        return session.query(ReviewScore) \
                      .order_by(order(order_by)) \
                      .all()
    else:
        return session.query(ReviewScore) \
                      .order_by(order(order_by)) \
                      .limit(limit) \
                      .offset(limit * pagenum) \
                      .all()


def select_review_score_lazy(session, limit=None, order_by=ReviewScore.id, descend=False):
    reviews = None
    last = None

    while True:
        query = session.query(ReviewScore) \
            .order_by(desc(order_by) if descend else asc(order_by))

        if reviews and descend:
            query = query.filter(order_by < last)
        if reviews and not descend:
            query = query.filter(order_by > last)

        reviews = query.limit(limit).all()

        if not reviews:
            break

        last = getattr(reviews[-1], order_by.key)
        yield reviews

def select_review_score_from_shop_id(session, shop_id,
    limit=None, pagenum=1, order_by=ReviewScore.id, descend=False):
    order = desc if descend else asc
    query = session.query(ReviewScore)\
                    .join(Review, Review.id == ReviewScore.review_id)\
                    .join(Page, Page.id == Review.page_id)\
                    .join(Shop, Shop.id == Page.shop_id)\
                    .filter(Shop.id == shop_id)\
                    .order_by(order(order_by))
    if limit is None:
        return query.all()
    else:
        return query.limit(limit)\
                    .offset(limit * pagenum)\
                    .all()


def select_shop_score(session,
                limit=None,
                pagenum=1,
                order_by=ShopScore.id,
                descend=False):
    order = desc if descend else asc
    if limit is None:
        return session.query(ShopScore) \
                      .order_by(order(order_by)) \
                      .all()
    else:
        return session.query(ShopScore) \
                      .order_by(order(order_by)) \
                      .limit(limit) \
                      .offset(limit * pagenum) \
                      .all()


def select_shop_score_lazy(session, limit=None, order_by=ShopScore.id, descend=False):
    shops = None
    last = None

    while True:
        query = session.query(ShopScore) \
            .order_by(desc(order_by) if descend else asc(order_by))

        if shops and descend:
            query = query.filter(order_by < last)
        if shops and not descend:
            query = query.filter(order_by > last)

        shops = query.limit(limit).all()

        if not shops:
            break

        last = getattr(shops[-1], order_by.key)
        yield shops
