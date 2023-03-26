from unittest.mock import MagicMock

import pytest

from iris_model.actions import get_feature_by_id
from iris_model.models import Features


@pytest.fixture
def mock_cursor() -> MagicMock:
    cursor = MagicMock()
    cursor.execute().fetchone.return_value = [1,2,3,4,5]
    return cursor


def test_write_features_to_db(mock_cursor):
    expected_data = [1,2,3,4,5]
    
    actual_result = get_feature_by_id(cursor=mock_cursor, id=1)

    assert actual_result == Features(
        sepal_length=expected_data[1],
        sepal_width=expected_data[2],
        petal_length=expected_data[3],
        petal_width=expected_data[4]
    )

    mock_cursor.execute.assert_called_with("SELECT * FROM iris_dataset WHERE id=?", (1,))
