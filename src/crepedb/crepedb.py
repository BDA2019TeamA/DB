import sys
from sqlalchemy import create_engine


class CrepeDB:
    def __init__(self, path):
        self.path = path
        try:
            self.engine = create_engine(path)
        except:
            print('Error', file=sys.stderr)


if __name__ == '__main__':
    db = CrepeDB('sqlite:///:memory:')
