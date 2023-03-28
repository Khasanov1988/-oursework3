from utils.functions import load_json, executed_transactions, sort_by_date, print_report_item


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

