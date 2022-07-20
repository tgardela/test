from app import app

def test_index():
    expected_result = "Solutions of tasks for Python Developer interview."
    response = app.test_client().get('/')
    res = response.data.decode('utf-8')

    assert res == expected_result
