from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, quantity: Union[str, None] = None):
    return {"item_id": item_id, "q": quantity}


@app.get("/version.txt", include_in_schema=False)
async def version():
    return FileResponse("./static/version.txt")
