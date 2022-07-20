import pytest

from app import app


@pytest.mark.parametrize("test_number, expected_result", [
    ('13', '10')
])
def test_sequence_elem_response_ok(test_number, expected_result):
    response = app.test_client().get(f'/sequence/elem/{test_number}')
    response_obtained = response.data.decode('utf-8')

    assert response_obtained == expected_result


@pytest.mark.parametrize("test_number, expected_code", [
    ('13.4', 404),
    ('some_text', 404)
])
def test_sequence_elem_wrong_input(test_number, expected_code):
    response = app.test_client().get(f'/sequence/elem/{test_number}')
    response_code = response.status_code

    assert response_code == expected_code


@pytest.mark.parametrize("test_number, expected_result", [
    ('4', '8')
])
def test_sequence_longest_response_ok(test_number, expected_result):
    response = app.test_client().get(f'/sequence/longest/{test_number}')
    response_obtained = response.data.decode('utf-8')

    assert response_obtained == expected_result


@pytest.mark.parametrize("test_number, expected_code", [
    ('13.4', 404),
    ('some_text', 404)
])
def test_sequence_longest_wrong_input(test_number, expected_code):
    response = app.test_client().get(f'/sequence/elem/{test_number}')
    response_code = response.status_code

    assert response_code == expected_code
