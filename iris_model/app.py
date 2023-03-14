import logging
import sqlite3
from typing import Any

import uvicorn
from fastapi import FastAPI, Depends

from actions import *
from models import Features, query_model

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


@app.get("/features")
def get_features(params: query_model = Depends()) -> Any:
    query_dict = params.dict()
    features = get_feature_by_id(cursor=cursor, id=query_dict.get("row_number"))
    return features


if __name__ == "__main__":
    uvicorn.run(app, port=8080)