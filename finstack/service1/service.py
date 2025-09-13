# Service 1: Account Service (Buggy)
class AccountService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id, balance):
        # BUG: Should check if user_id already exists
        self.accounts[user_id] = balance
        return True

    def get_balance(self, user_id):
        # BUG: Should handle missing user_id
        return self.accounts[user_id]
