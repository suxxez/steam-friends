import requests
import uvicorn

from src.helpers import convert_id
from steam_api_key import STEAM_API_KEY

from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{user_id}")
def get_user_information(user_id: str):
    user_id = convert_id(user_id)
    response = requests.get(
        f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={user_id}"
    )

    user_information = response.json()

    return user_information


@app.get("/user/{user_id}/friendlist")
def get_friends(user_id: str):
    user_id = convert_id(user_id)
    response = requests.get(
        f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={STEAM_API_KEY}&steamid={user_id}&relationship=friend"
    )

    friends = response.json()

    return friends


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
