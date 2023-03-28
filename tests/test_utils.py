from utils.functions import load_json, executed_transactions, sort_by_date, print_report_item

test_item = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

test_report = "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."

def test_load_json():
    assert load_json('test') is None
    assert load_json('test_operations.json') == [1, 2, 3]


def test_executed_transactions():
    assert executed_transactions([]) == []
    assert executed_transactions([{}]) == []
    assert executed_transactions([{'date': 'Null', 'state': "EXECUTED"}, {'money': 500, 'state': "NOT_EXECUTED"}]) == [{
        'date': 'Null', 'state': "EXECUTED"}]


def test_sort_by_date():
    assert sort_by_date(
        [{'id': 2, 'date': '2019-06-30T15:11:53.136004'}, {'id': 1, 'date': '2019-06-30T15:11:59.000000'}]) == [
               {'id': 1, 'date': '2019-06-30T15:11:59.000000'}, {'id': 2, 'date': '2019-06-30T15:11:53.136004'}]


def test_print_report_item(capsys):
    print_report_item(test_item)
    captured = capsys.readouterr()
    assert captured.out == test_report
