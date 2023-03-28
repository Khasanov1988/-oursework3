from functions import load_json, sort_by_date, executed_transactions, print_report_item


# Загружаем файл со всеми операциями в формате json
transactions = load_json('operations.json')
# Оставляем только успешные транзакции
ex_transactions = executed_transactions(transactions)
# Сортируем транзакции от более ранних к более поздним
sorted_transactions = sort_by_date(ex_transactions)
# Выводим информацию по последним 5 транзакциям
for i in range(min(5, len(sorted_transactions))):
    print_report_item(sorted_transactions[i])


