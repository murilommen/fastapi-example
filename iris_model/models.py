from pydantic import BaseModel, create_model


query_params = {"row_number": (int, 0)}
query_model = create_model("Query", **query_params) 


class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float