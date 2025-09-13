# Controller for Account Service (Buggy)
from service import AccountService

service = AccountService()

def create_account_controller(user_id, balance):
    # BUG: No input validation
    return service.create_account(user_id, balance)

def get_balance_controller(user_id):
    # BUG: No error handling
    return service.get_balance(user_id)
