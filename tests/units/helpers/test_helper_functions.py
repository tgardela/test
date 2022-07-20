import pytest

from helpers.helper_functions import is_float


@pytest.mark.parametrize("input, expected_result", [
    ('5', True),
    ('5.0', True),
    ('5,0', False),
    ('sadas', False)
])
def test_is_float(input, expected_result):
    assert is_float(input) == expected_result
