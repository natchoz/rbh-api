import json
from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# async def hello(name: str = "Nat Cho New"): return {"message": f'Hello new "{name}"'}


@app.get("/restaurant-category")
async def restaurantCategory():
    with open("./assets/json/restaurant-category.json") as restaurantCategory:
        response = json.load(restaurantCategory)
    return response


@app.get("/restaurant/{id}")
async def restaurantCategory(id: int):
    with open(f"./assets/json//restaurant/{id}.json") as restaurantCategory:
        response = json.load(restaurantCategory)
    return response
