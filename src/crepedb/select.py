import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import sessionmaker
from .models import Shop, Site, Page, Review


# https://blog.mmmcorp.co.jp/blog/2018/03/22/sql_order_by/
# order_byがid以外のときはidと組み合わせることでuniqueにする
def select_shop(session,
                limit=None,
                pagenum=1,
                order_by=Shop.id,
                descend=False):
    order = desc if descend else asc
    query = session.query(Shop)
    if order_by is Shop.id:
        query = query.order_by(order(order_by))
    else:
        query = query.order_by(order(order_by), Shop.id.asc())

    if limit is None:
        return query.all()
    else:
        return query.offset(limit * pagenum) \
                    .limit(limit) \
                    .all()

def select_shop_lazy(session, limit=None, order_by=Shop.id, descend=False):
    shops = None
    order = desc if descend else asc
    offset = 0

    while True:
        query = session.query(Shop)
        if order_by is Shop.id:
            query = query.order_by(order(order_by))
        else:
            query = query.order_by(order(order_by), Shop.id.asc())

        shops = query.offset(offset).limit(limit).all()

        if not shops:
            break

        offset += len(shops)
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


def select_site(session,
                limit=None,
                pagenum=1,
                order_by=Site.id,
                descend=False):
    order = desc if descend else asc
    query = session.query(Site)
    if order_by is Site.id:
        query = query.order_by(order(order_by))
    else:
        query = query.order_by(order(order_by), Site.id.asc())

    if limit is None:
        return query.all()
    else:
        return query.offset(limit * pagenum) \
                    .limit(limit) \
                    .all()

def select_site_lazy(session, limit=None, order_by=Site.id, descend=False):
    sites = None
    order = desc if descend else asc
    offset = 0

    while True:
        query = session.query(Site)
        if order_by is Site.id:
            query = query.order_by(order(order_by))
        else:
            query = query.order_by(order(order_by), Site.id.asc())

        sites = query.offset(offset).limit(limit).all()

        if not sites:
            break

        offset += len(sites)
        yield sites


def select_page(session,
                limit=None,
                pagenum=1,
                order_by=Page.id,
                descend=False):
    order = desc if descend else asc
    query = session.query(Page)
    if order_by is Page.id:
        query = query.order_by(order(order_by))
    else:
        query = query.order_by(order(order_by), Page.id.asc())

    if limit is None:
        return query.all()
    else:
        return query.offset(limit * pagenum) \
                    .limit(limit) \
                    .all()


def select_page_lazy(session, limit=None, order_by=Page.id, descend=False):
    pages = None
    order = desc if descend else asc
    offset = 0

    while True:
        query = session.query(Page)
        if order_by is Page.id:
            query = query.order_by(order(order_by))
        else:
            query = query.order_by(order(order_by), Page.id.asc())

        pages = query.offset(offset).limit(limit).all()

        if not pages:
            break

        offset += len(pages)
        yield pages


def select_review(session,
                  limit=None,
                  pagenum=1,
                  order_by=Review.id,
                  descend=False):
    order = desc if descend else asc
    query = session.query(Review)
    if order_by is Review.id:
        query = query.order_by(order(order_by))
    else:
        query = query.order_by(order(order_by), Review.id.asc())

    if limit is None:
        return query.all()
    else:
        return query.offset(limit * pagenum) \
                    .limit(limit) \
                    .all()


def select_review_lazy(session, limit=None, order_by=Review.id, descend=False):
    reviews = None
    order = desc if descend else asc
    offset = 0

    while True:
        query = session.query(Review)
        if order_by is Review.id:
            query = query.order_by(order(order_by))
        else:
            query = query.order_by(order(order_by), Review.id.asc())

        reviews = query.offset(offset).limit(limit).all()

        if not reviews:
            break

        offset += len(reviews)
        yield reviews
