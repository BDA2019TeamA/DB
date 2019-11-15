# CrepeDB

複数サイトの店舗情報とレビュー情報を管理可能なDBアクセスツール



## How To Install

```
pip install git+https://github.com/BDA2019TeamA/CrepeDB
```



## How To Use

```python
from crepedb import CrepeDB

db = CrepeDB('sqlite:///path/to/db.sqlite3')
db.insert_shop({'name': 'Crepe食堂', 'tel': '01234567890'})
```





