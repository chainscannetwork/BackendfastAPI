from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class InputString(BaseModel): 
    input_string:str

@app.post("/process_string/")
def process_string(input_data: InputString):
    processed_string = f"Processed: {input_data.input_string}"
    return {"result": processed_string}

