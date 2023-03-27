from utils import load_json, date_format, executed_transactions

transactions = load_json('operations.json')
print(transactions)
execut_transactions = executed_transactions(transactions)
print(execut_transactions)
sorted_transactions = date_format(execut_transactions)
print(sorted_transactions)


