import logging

import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/features")
def write_features(features: Features):
    logger.info(features)
    # parse features
    # connect to DB
    # write to database
    # return/log success message



if __name__ == "__main__":
    uvicorn.run(app, port=8000)