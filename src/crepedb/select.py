import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import sessionmaker
from .models import Shop


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
