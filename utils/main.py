import function


def main():
    for item in function.reformat_date_operations:
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


main()
