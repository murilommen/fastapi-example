import logging
import sqlite3

from models import Features

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DATABASE_URI = "local.db"


def get_sql_cursor() -> sqlite3.Cursor:
    conn = sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
    return conn.cursor()


def init_db(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS iris_dataset(sepal_length REAL, sepal_width REAL, petal_length REAL, petal_width REAL);"
    )

def write_features_to_db(cursor: sqlite3.Cursor, features: Features) -> None:
    query = "INSERT INTO iris_dataset(sepal_length, sepal_width, petal_length, petal_width) VALUES (?,?,?,?)"
    values_tuple = (
        features.sepal_length, 
        features.sepal_width, 
        features.petal_length, 
        features.petal_width
    )
    cursor.execute(query, values_tuple)
    logger.debug(f"{features} written successfully to DB!")