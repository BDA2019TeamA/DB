from sqlalchemy.orm import sessionmaker
from . import models
from .models import Shop


def insert_shop(session, shop):
    item = Shop()
    item.name = shop['name'] if 'name' in shop else None
    item.address = shop['address'] if 'address' in shop else None
    item.tel = shop['tel'] if 'tel' in shop else None

    session.add(item)
    session.commit()

    return item
