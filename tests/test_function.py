from utils.function import get_data_from_json, sort_data_executed
from utils.main import operations

def test_get_data_from_json():
    """Проверка на тип list исходных данных"""
    assert type(get_data_from_json()) == list


def test_sort_data_executed():
    """Проверка на то, что все операции проведенные"""
    sorted_operations = sort_data_executed(operations)
    assert sorted_operations[0]["state"] == "EXECUTED"
    assert sorted_operations[1]["state"] == "EXECUTED"
    assert sorted_operations[2]["state"] == "EXECUTED"
    assert sorted_operations[3]["state"] == "EXECUTED"
    assert sorted_operations[4]["state"] == "EXECUTED"
    assert len(sorted_operations) == 5


