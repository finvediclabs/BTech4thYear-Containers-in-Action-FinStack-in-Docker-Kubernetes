# Controller for Transaction Service (Buggy)
from service import TransactionService

service = TransactionService()

def add_transaction_controller(user_id, amount):
    # BUG: No input validation
    return service.add_transaction(user_id, amount)

def get_transactions_controller(user_id):
    # BUG: No error handling
    return service.get_transactions(user_id)
