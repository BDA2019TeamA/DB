# CrepeDB


![](https://github.com/BDA2019TeamA/CrepeDB/workflows/Test%20CrepeDB/badge.svg)

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



## Tables

- Shop (店舗情報)
- Site (出典サイト情報)
- Page (各サイト毎の店舗情報)
- Reviewer (レビュー情報)


### Shop

|          | カラム名 | 型          | Unique | Nullable | 例             |
| -------- | -------- | ----------- | ------ | -------- | -------------- |
| ShopID   | id       | Integer     | o      | x        | `1`(自動付与)  |
| 店舗名   | name     | String(255) | -      | x        | `Crepe食堂`    |
| 住所     | address  | String(255) | -      | o        | `東京都目黒区` |
| 電話番号 | tel      | String(11)  | -      | o        | `0123456789`   |


### Site

|           | カラム名 | 型          | Unique | Nullable | 例                            |
| --------- | -------- | ----------- | ------ | -------- | ----------------------------- |
| SiteID    | id       | Integer     | o      | x        | `1`(自動付与)                 |
| サイト名  | name     | String(255) | -      | x        | `クレープなび`                |
| サイトURL | url      | String(255) | -      | o        | `https://sample.crepenavi.jp` |


### Page

|                        | カラム名   | 型          | Unique | Nullable | 例            |
| ---------------------- | ---------- | ----------- | ------ | -------- | ------------- |
| PageID                 | id         | Integer     | o      | x        | `1`(自動付与) |
| 評価                   | evaluation | Integer     | -      | o        | `4`           |
| URL                    | url        | String(512) | -      | o        |               |
| ジャンル               | genre      | String(128) | -      | o        | `中華料理`    |
| SiteID                 | site_id    | Integer     | -      | x        | `1`           |
| ShopID                 | shop_id    | Integer     | -      | x        | `3`           |
| Siteデータ(Selectのみ) | site       | Site        | -      | x        |               |
| Shopデータ(Selectのみ) | shop       | Shop        | -      | x        |               |


### Review

|                        | カラム名    | 型           | Unique | Nullable | 例            |
| ---------------------- | ----------- | ------------ | ------ | -------- | ------------- |
| ReviewID               | id          | Integer      | o      | x        | `1`(自動付与) |
| レビュアー             | reviewer    | String(255)  | -      | o        | `Abc`         |
| コメント               | comment     | String(1024) | -      | o        | `おいしい`    |
| 評価                   | evaluation  | Integer      | -      | o        | `1`           |
| 出典元ReviewID         | original_id | Integer      | -      | x        | `999`         |
| PageID                 | page_id     | Integer      | -      | x        | `3`           |
| Pageデータ(Selectのみ) | page        | Page         | -      | x        |               |



