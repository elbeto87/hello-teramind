from fastapi import FastAPI

from app.database import Base, engine
from app import models # noqa


Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Teramind"}
