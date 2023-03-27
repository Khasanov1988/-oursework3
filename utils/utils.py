import datetime
import json
import os
from operator import itemgetter


def load_json(filename):
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


def executed_transactions(transactions):
    """
    Функция оставляет только успешные транзакции.
    :param transactions: исходный список транзакций
    :return: список успешных транзакций
    """
    answer = []
    for transaction in transactions:
        if 'date' in transaction:
            if transaction['state'] == "EXECUTED":
                answer.append(transaction)
    return answer


def date_format(transactions):
    """
    Функция конвертирует и добавляет в исходный список транзакций время с эпохи
    :param transactions: исходный список транзакций
    :return: список транзакций с добавленным ключом "time" для времени с эпохи
    """
    return sorted(transactions, key=lambda row: row['date'], reverse=True)
