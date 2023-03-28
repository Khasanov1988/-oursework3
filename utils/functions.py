import datetime
import json
import os
from operator import itemgetter


def load_json(filename: str):
    """
    Функция загружает исходный файл с данными и конвертирует в список
    :param filename: имя файла в формате json
    :return: список из файла
    """
    if os.path.exists(os.path.join(filename)):
        file = open(os.path.join(filename), "r", encoding="utf-8")
        content = file.read()
        return json.loads(content)
    else:
        print(f"Файла {filename} в папке с проектом не существует")
        return None


def executed_transactions(transactions: list[dict]):
    """
    Функция оставляет только успешные транзакции.
    :param transactions: Исходный список транзакций
    :return: Список успешных транзакций
    """
    answer = []
    for transaction in transactions:
        if not transaction:
            print("<<<В исходных данных есть пустой словарь>>>\n")
        else:
            if transaction['state'] == "EXECUTED":
                answer.append(transaction)
    return answer


def sort_by_date(transactions: list[dict]):
    """
    Функция конвертирует и добавляет в исходный список транзакций время с эпохи
    :param transactions: исходный список транзакций
    :return: список транзакций с добавленным ключом "time" для времени с эпохи
    """
    return sorted(transactions, key=lambda row: row['date'], reverse=True)


def print_report_item(item: dict[str, any]):
    """
    Функция выводит в консоль данные о транзакциях из словаря в требуемом формате
    :param item: исходный словарь
    :return: None
    """
    # Получаем дату и время транзакции из словаря
    transaction_date = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')

    # Получаем данные отправителя и получателя транзакции
    if 'from' in item:
        sender = item['from'].split()
        sender[1] = f"{sender[1][:4]} {sender[1][4:6]}** **** {sender[1][-4:]}"
    else:
        sender = ['<ОТКРЫТИЕ', 'ВКЛАДА>']

    recipient = item.get('to', '<НЕИЗВЕСТНАЯ_ПЛАТЕЖНАЯ_СИСТЕМА> <СЧЕТ>').split()
    recipient[1] = recipient[1][-4:]

    # Форматируем и выводим данные транзакции в консоль
    print(f"{transaction_date:%d.%m.%Y} {item['description']}\n"
          f"{sender[0]} {sender[1]} -> {recipient[0]} **{recipient[1]}\n"
          f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")
