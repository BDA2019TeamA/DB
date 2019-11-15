import sqlalchemy
from sqlalchemy import asc, desc
from sqlalchemy.orm import sessionmaker
from .models import Shop
from typing import Optional, List

def select_shop(session,
                limit=None, pagenum=1,
                order_by=Shop.id, descend=False):
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

def select_shop_lazy(session, limit=None,
                     order_by=Shop.id, descend=False):
    if descend:
        # first loop
        shops = session.query(Shop) \
                    .order_by(desc(order_by)) \
                    .limit(limit) \
                    .all()
        yield shops
        while shops:
            shops = session.query(Shop) \
                        .order_by(desc(order_by)) \
                        .limit(limit) \
                        .all()
            yield shops
    else:
        # first loop
        shops = session.query(Shop) \
                    .order_by(asc(order_by)) \
                    .limit(limit) \
                    .all()
        yield shops
        while True:
            shops = session.query(Shop) \
                        .order_by(asc(order_by)) \
                        .filter(order_by > getattr(shops[-1], order_by.key)) \
                        .limit(limit) \
                        .all()
            yield shops
