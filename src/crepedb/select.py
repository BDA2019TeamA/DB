import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import sessionmaker
from .models import Shop, Site, Page, Review


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

def select_site(session,
                limit=None,
                pagenum=1,
                order_by=Site.id,
                descend=False):
    order = desc if descend else asc
    if limit is None:
        return session.query(Site) \
                      .order_by(order(order_by)) \
                      .all()
    else:
        return session.query(Site) \
                      .order_by(order(order_by)) \
                      .limit(limit) \
                      .offset(limit * pagenum) \
                      .all()


def select_site_lazy(session, limit=None, order_by=Site.id, descend=False):
    sites = None
    last = None

    while True:
        query = session.query(Site) \
            .order_by(desc(order_by) if descend else asc(order_by))

        if sites and descend:
            query = query.filter(order_by < last)
        if sites and not descend:
            query = query.filter(order_by > last)

        sites = query.limit(limit).all()

        if not sites:
            break

        last = getattr(sites[-1], order_by.key)
        yield sites

def select_page(session,
                limit=None,
                pagenum=1,
                order_by=Page.id,
                descend=False):
    order = desc if descend else asc
    if limit is None:
        return session.query(Page) \
                      .order_by(order(order_by)) \
                      .all()
    else:
        return session.query(Page) \
                      .order_by(order(order_by)) \
                      .limit(limit) \
                      .offset(limit * pagenum) \
                      .all()


def select_page_lazy(session, limit=None, order_by=Page.id, descend=False):
    pages = None
    last = None

    while True:
        query = session.query(Page) \
            .order_by(desc(order_by) if descend else asc(order_by))

        if pages and descend:
            query = query.filter(order_by < last)
        if pages and not descend:
            query = query.filter(order_by > last)

        pages = query.limit(limit).all()

        if not pages:
            break

        last = getattr(pages[-1], order_by.key)
        yield pages

def select_review(session,
                limit=None,
                pagenum=1,
                order_by=Review.id,
                descend=False):
    order = desc if descend else asc
    if limit is None:
        return session.query(Review) \
                      .order_by(order(order_by)) \
                      .all()
    else:
        return session.query(Review) \
                      .order_by(order(order_by)) \
                      .limit(limit) \
                      .offset(limit * pagenum) \
                      .all()


def select_review_lazy(session, limit=None, order_by=Review.id, descend=False):
    reviews = None
    last = None

    while True:
        query = session.query(Review) \
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
