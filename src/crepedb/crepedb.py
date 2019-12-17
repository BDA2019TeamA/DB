from . import insert
from . import select
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine
from .models import Base, Shop


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

    def select_shop(self, limit=None, pagenum=1, order_by=Shop.id, descend=False):
        return select.select_shop(self.session, limit, pagenum, order_by, descend)

    def select_shop_lazy(self, limit=1, order_by=Shop.id, descend=False):
        return select.select_shop_lazy(self.session, limit, order_by, descend)
