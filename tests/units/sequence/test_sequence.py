import pytest

from sequence.sequence import (
    longest_sequence,
    sequence
)


@pytest.mark.parametrize("number, expected_result", [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 8),
    (13, 10),
])
def test_sequence_correct(number, expected_result):
    assert sequence(number) == expected_result


@pytest.mark.parametrize("number, expected_result", [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 8)
])
def test_longest_sequence_correct(number, expected_result):
    assert longest_sequence(number) == expected_result
