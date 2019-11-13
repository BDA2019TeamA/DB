from . import insert
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine
from .models import Base


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
