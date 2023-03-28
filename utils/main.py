from functions import load_json, sort_by_date, executed_transactions

transactions = load_json('operations.json')
print(transactions)
ex_transactions = executed_transactions(transactions)
print(ex_transactions)
sorted_transactions = sort_by_date(ex_transactions)
print(sorted_transactions)


