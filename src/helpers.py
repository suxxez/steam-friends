import requests

from steam_api_key import STEAM_API_KEY


def convert_id(user_id: int | str):
    if isinstance(user_id, int):
        return user_id

    res = requests.get(
        f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={STEAM_API_KEY}&vanityurl={user_id}"
    )

    if res.status_code == 200:
        return res.json().get("response").get("steamid")
    else:
        # todo: error handling
        return user_id
