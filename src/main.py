import uvicorn
import sys
import json

from fastapi import FastAPI
from src import user_service

app = FastAPI()


@app.get("/user/{user_id}")
def get_user_information(user_id: str):
    return user_service.get_user_information(user_id)


@app.get("/user/{user_id}/friendlist")
def get_friends(user_id: str):
    return user_service.get_friends(user_id)


def get_openapi_spec():
    return app.openapi()


if __name__ == "__main__":
    with open('../swagger.json', 'w') as file:
        file.write(json.dumps(get_openapi_spec()))
    uvicorn.run(app, host="0.0.0.0", port=8000)

if sys.argv[1] == "openapi":
    print(get_openapi_spec())
