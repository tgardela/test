import pandas as pd
from pandas.core.frame import DataFrame
import pytest

from iris_pandas.iris_pandas import (
    describe,
    sepal_length
)


def get_test_df() -> DataFrame:
    data = {'sepal_length': [5.1, 3.8, 6.4, 5.3, 4.7, 5.4],
            'sepal_width': [3.1, 3.8, 3.9, 3.7, 3.7, 4.1],
            'petal_length': [1.4, 2.5, 4.6, 5.3, 4.4, 6.3],
            'petal_width': [0.2, 0.4, 1.1, 1.3, 2.1, 2.7],
            'species': ['setosa', 'setosa', 'versicolor', 'versicolor', 'virginica', 'virginica'],
            }

    return pd.DataFrame(data)


@pytest.mark.parametrize("expected_result", [
    '{"sepal_length":{"count":6.0,"mean":5.11666667,"std":0.85654344,"min":3.8,"25%":4.8,"50%":5.2,"75%":5.375,"max":6.4},"sepal_width":{"count":6.0,"mean":3.71666667,"std":0.33714487,"min":3.1,"25%":3.7,"50%":3.75,"75%":3.875,"max":4.1},"petal_length":{"count":6.0,"mean":4.08333333,"std":1.81484618,"min":1.4,"25%":2.975,"50%":4.5,"75%":5.125,"max":6.3},"petal_width":{"count":6.0,"mean":1.3,"std":0.96540147,"min":0.2,"25%":0.575,"50%":1.2,"75%":1.9,"max":2.7}}' # noqa
])
def test_describe(expected_result):
    test_data = get_test_df()

    assert pd.io.json.dumps(describe(test_data), double_precision=8) == expected_result


@pytest.mark.parametrize("test_length, expected_result", [
    (5, {'setosa': '1', 'versicolor': '0', 'virginica': '1'})
])
def test_sepal_length(test_length, expected_result):
    test_data = get_test_df()

    assert sepal_length(test_length, test_data) == expected_result
