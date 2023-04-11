import streamlit as st
import requests 
from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}



user_input = st.text_input("Enter your name:")
if st.button("Submit"):
    response = requests.get("http://localhost:8000/hello")
    st.write(response.json())



# Learn - samples
'''
# GET Request with String Parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}"}

# GET Request with Integer Parameter
@app.get("/square/{num}")
def square(num: int):
    return {"result": num*num}


# GET Request with Optional Parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# POST Request
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}




    
uvicorn main:app --reload

'''