import pytest

from app import app


@pytest.mark.parametrize("test_length, expected_result", [
    ('5.3', '{"setosa":"39","versicolor":"5","virginica":"1"}\n'),
    ('5,3', "Provided input is not an int(6) or a float(6.0)")
])
def test_iris_sepal_length_reponse_ok(test_length, expected_result):
    response = app.test_client().get(f'/iris/group/sepal_length/{test_length}')
    response_obtained = response.data.decode('utf-8')

    assert response_obtained == expected_result


@pytest.mark.parametrize("expected_result", [
    '{"petal_length":{"25%":1.6,"50%":4.35,"75%":5.1,"count":150.0,"max":6.9,"mean":3.7580000000000005,"min":1.0,"std":1.7652982332594662},"petal_width":{"25%":0.3,"50%":1.3,"75%":1.8,"count":150.0,"max":2.5,"mean":1.1993333333333336,"min":0.1,"std":0.7622376689603465},"sepal_length":{"25%":5.1,"50%":5.8,"75%":6.4,"count":150.0,"max":7.9,"mean":5.843333333333334,"min":4.3,"std":0.828066127977863},"sepal_width":{"25%":2.8,"50%":3.0,"75%":3.3,"count":150.0,"max":4.4,"mean":3.0573333333333337,"min":2.0,"std":0.4358662849366982}}\n' # noqa

])
def test_iris_describe(expected_result):
    response = app.test_client().get('/iris/describe')
    response_obtained = response.data.decode('utf-8')

    assert response_obtained == expected_result
