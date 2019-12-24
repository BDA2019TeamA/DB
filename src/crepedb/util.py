from os import getenv
from sys import stderr
import requests

GOOGLE_MAPS_API_KEY = getenv("GOOGLE_MAPS_API_KEY")
FIND_PLACE_ENDPOINT = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
PLACE_DETAIL_ENDPOINT = "https://maps.googleapis.com/maps/api/place/details/json"


def get_info_from_google(tel):
    if GOOGLE_MAPS_API_KEY is None:
        print("API Key not set", file=stderr)
        return None

    if tel is None:
        print("cannot fetch phone number", file=stderr)
        return None

    r = requests.get(FIND_PLACE_ENDPOINT,
                     params={
                         "key": GOOGLE_MAPS_API_KEY,
                         "inputtype": "text",
                         "input": tel,
                     })

    if not r.status_code == requests.codes.ok:
        print("request failed:", r.reason, file=stderr)
        return None

    info = r.json()

    if len(info["candidates"]) == 0:
        print("not found", file=stderr)
        return None

    # 最有力候補を取得。間違っている可能性もあることに注意
    place_id = info["candidates"][0]["place_id"]

    r = requests.get(PLACE_DETAIL_ENDPOINT,
                     params={
                         "key": GOOGLE_MAPS_API_KEY,
                         "place_id": place_id
                     })

    if not r.status_code == requests.codes.ok:
        print("request failed:", r.reason, file=stderr)
        return None

    details = r.json()["result"]
    res = {}

    res["name"] = details["name"]
    res["tel"] = details["formatted_phone_number"]
    res["address"] = details["formatted_address"]
    res["place_id"] = details["place_id"]

    return res


def get_info_from_google_without_phone_number(tel):
    """ 
        電話番号の取得を諦め、リソースの取得を1回に抑える
        (DBで一致検索をかけられるなら電話番号は必要ないという説はある 03始まりのやつが来たらそれを入れとく感じで)
    """
    if GOOGLE_MAPS_API_KEY is None:
        print("API Key not set", file=stderr)
        return None

    if tel is None:
        print("cannot fetch phone number", file=stderr)
        return None

    r = requests.get(FIND_PLACE_ENDPOINT,
                     params={
                         "key": GOOGLE_MAPS_API_KEY,
                         "inputtype": "text",
                         "input": tel,
                         "fields": "place_id,name,formatted_address"
                     })
    if not r.status_code == requests.codes.ok:
        print("request failed:", r.reason, file=stderr)
        return None

    info = r.json()

    if len(info["candidates"]) == 0:
        print("not found", file=stderr)
        return None

    # 最有力候補を取得。間違っている可能性もあることに注意
    cand = info["candidates"][0]
    res = {}

    res["name"] = cand["name"]
    res["address"] = cand["formatted_address"]
    res["place_id"] = cand["place_id"]

    return res