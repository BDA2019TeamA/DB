import re

# ざっくり変換テーブル
# TODO: 漢数字(とりあえず番地に漢数字使ってるとこなさそうなので妥協)
translateTable = str.maketrans({
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "５": "5",
    "６": "6",
    "７": "7",
    "８": "8",
    "９": "9",
    "０": "0",
    "Ｆ": "F",
    "階": "F",
    "　": " "
})

choume_banchi = re.compile("(丁目|番地)")
space = re.compile(r"\s+")

# ざっくり正規化
def normalize(addr: str) -> str:
    return choume_banchi.sub(
        space.sub(addr.translate(translateTable), " "), "-")

# ??????
def partial_eq(left: str, right: str) -> bool:
    return left in right or right in left
