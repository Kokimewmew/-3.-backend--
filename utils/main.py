from utils import function

def main():
    """ Запуск программы. Вывод данных в зависимости есть ли исходный отправитель ["from"]"""
    for item in reformat_date_operations:
        if "from" in item:
            print(f'''{item["date"]} {item["description"]}
{function.reformat_card(item["from"])} -> {function.reformat_card(item["to"])}
{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}
''')

        else:
            print(f'''{item["date"]} {item["description"]}
{function.reformat_card(item["to"])} 
{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}
''')


operations = function.get_data_from_json()
five_last_operations = function.sort_data_executed(operations)
reformat_date_operations = function.reformat_date(five_last_operations)

main()
