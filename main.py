from fastapi import FastAPI
from routers import MetaProbe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    hmm = {"Hello": "Running FastAPI", "test": "hmm"}
    return hmm["Hello"]

@app.get("/metaprobe/extract/{url:path}")
async def meta(url: str):
    result = await MetaProbe(url)
    return result
