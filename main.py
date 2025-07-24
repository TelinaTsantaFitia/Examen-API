from fastApi import FastAPI
from pydantic import BaseModel
from starlette import JSONresponse
from starlette.requests import Request

app = FastAPI

# exo 1

@app.get("/hello")
def hello_world():
    return {"message": "GET utilisé"}

# question 2

@app.get("/get/welcome")
def welcome (name : str):
    return {"message": "Hello world{name}"}
