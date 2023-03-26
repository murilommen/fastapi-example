import logging
import sqlite3
from typing import Union, Optional

from iris_model.models import Features

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DATABASE_URI = "local.db"
_connection: sqlite3.Connection


def get_sql_cursor(connection: Optional[sqlite3.Connection] = None) -> sqlite3.Cursor:
    global _connection
    _connection = connection or sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
    return _connection.cursor()


def init_db(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS iris_dataset(id INTEGER PRIMARY KEY, sepal_length REAL, sepal_width REAL, petal_length REAL, petal_width REAL);"
    )


def write_features_to_db(
        cursor: sqlite3.Cursor, 
        features: Features, 
        connection: Optional[sqlite3.Connection] = None
    ) -> None:
    connection = _connection or connection
    if not connection:
        raise ValueError("you must define a sqlite connection")
    
    query = "INSERT INTO iris_dataset(sepal_length, sepal_width, petal_length, petal_width) VALUES (?,?,?,?)"
    values_tuple = (
        features.sepal_length, 
        features.sepal_width, 
        features.petal_length, 
        features.petal_width
    )
    cursor.execute(query, values_tuple)
    connection.commit()
    logger.debug(f"{features} written successfully to DB!")


def get_feature_by_id(cursor: sqlite3.Cursor, id: int) -> Union[Features, str]:
    result = cursor.execute("SELECT * FROM iris_dataset WHERE id=?", (id,))
    data = result.fetchone()
    logger.debug(f"result_data_is {data}")
    if data:
        features = Features(
            sepal_length = data[1],
            sepal_width = data[2],
            petal_length = data[3],
            petal_width = data[4]
        )

        return features
    else:
        return f"Did not find anything with id = {id}" 