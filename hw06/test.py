import pytest
from average import Average


@pytest.fixture
def list_1():
    return [1, 3, 5, 7]


@pytest.fixture
def list_2():
    return [2, 4, 6, 8]


def test_init_attributes(list_1, list_2):
    value_list = Average(list_1, list_2)
    assert value_list.list_1 == list_1
    assert value_list.list_2 == list_2


def test_average_function(list_1, list_2):
    assert Average.average(list_1) == 4
    assert Average.average(list_2) == 5


def test_compare_method():
    assert Average(
        [2, 4, 6, 8],
        [1, 3, 5, 7],
    ).compare() == "Первый список имеет большее среднее значение."

    assert Average(
        [2, 4, 6, 8],
        [2, 4, 6, 8],
    ).compare() == "Средние значения равны"

    assert Average(
        [1, 3, 5, 7],
        [2, 4, 6, 8],
    ).compare() == "Второй список имеет большее среднее значение"
