import requests

from steam_api_key import STEAM_API_KEY


def convert_id(id):
    if isinstance(id, int):
        return id

    res = requests.get(
        f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={STEAM_API_KEY}&vanityurl={id}"
    )

    if res.status_code == 200:
        return res.json().get("response").get("steamid")
    else:
        # todo: error handling
        return id
