from utils import function
from utils.function import operations, five_last_operations


def test_get_data_from_json():
    assert type(function.get_data_from_json()) == list


def test_sort_data_executed():
    sorted_operations = function.sort_data_executed(operations)
    assert sorted_operations[0]["state"] == "EXECUTED"
    assert sorted_operations[1]["state"] == "EXECUTED"
    assert sorted_operations[2]["state"] == "EXECUTED"
    assert sorted_operations[3]["state"] == "EXECUTED"
    assert sorted_operations[4]["state"] == "EXECUTED"
    assert len(sorted_operations) == 5


def test_reformat_card(item="Visa Classic 6831982476737658"):

    assert function.reformat_card(item) == "Visa Classic 6831 98** **** 7658"

