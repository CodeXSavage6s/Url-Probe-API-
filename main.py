from fastapi import FastAPI
from routers import MetaProbe

app = FastAPI()


@app.get("/")
def read_root():
    hmm = {"Hello": "World", "test": "hmm"}
    return hmm["Hello"]

@app.get("/metaprobe/extract/{url:path}")
async def meta(url: str):
    hmm = {"Hello": "World", "test": "hmm"}
    result = await MetaProbe(url)
    return result

  

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}