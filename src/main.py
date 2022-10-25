import uvicorn


from fastapi import FastAPI
from src import user_service

app = FastAPI()


@app.get("/user/{user_id}")
def get_user_information(user_id: str):
    return user_service.get_user_information(user_id)


@app.get("/user/{user_id}/friendlist")
def get_friends(user_id: str):
    return user_service.get_friends(user_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
