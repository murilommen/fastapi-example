import logging
import sqlite3

import uvicorn
from fastapi import FastAPI

from actions import get_sql_cursor, init_db, write_features_to_db
from models import Features

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
cursor: sqlite3.Cursor


@app.on_event("startup")
def get_or_create_db():
    global cursor
    cursor = get_sql_cursor()
    init_db(cursor=cursor)


@app.post("/features")
def write_features(features: Features) -> None:
    write_features_to_db(features=features, cursor=cursor)
    logger.debug(features)



if __name__ == "__main__":
    uvicorn.run(app, port=8090)