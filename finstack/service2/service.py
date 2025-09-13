# Service 2: Transaction Service (Buggy)
class TransactionService:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, user_id, amount):
        # BUG: Should check for valid amount
        self.transactions.append({'user_id': user_id, 'amount': amount})
        return True

    def get_transactions(self, user_id):
        # BUG: Should filter by user_id
        return self.transactions
