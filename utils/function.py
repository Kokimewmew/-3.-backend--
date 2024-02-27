import json
import os
from datetime import datetime


def get_data_from_json():
    """Открывает и читает файл json """
    with open(os.path.join("..", "operations.json"), "r", encoding="utf8") as f:
        operations = json.load(f)
    return operations


def sort_data_executed(operations):
    """Возвращает 5 выполненных операции отсортированных датой с конца"""
    executed_operations_ = []

    for operation in operations:
        if "state" in operation and operation["state"] == "EXECUTED":
            executed_operations_.append(operation)
    sort_executed_operations = sorted(executed_operations_, key=lambda x: x["date"], reverse=True)
    return sort_executed_operations[:5]


def reformat_date(five_last_operations):
    """Реформатирование даты в виде дд.мм.гггг"""
    reformat_date = five_last_operations
    for item in reformat_date:
        item["date"] = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return reformat_date


def reformat_card(item):
    """Реформатирование номеров карт и счетов, скрыв часть цифр символом *"""
    bank_digits = item.split()[-1]
    bank_name = item.split()[:-1]
    bank_name = " ".join(bank_name)
    if bank_name == "Счет":
        bank_digits = "**" + bank_digits[-4:]
    else:
        bank_digits = bank_digits[:4] + " " + bank_digits[4:6] + "** " + "*" * 4 + " " + bank_digits[-4:]

    masked_cred = "".join(bank_name + " " + bank_digits)

    return masked_cred
