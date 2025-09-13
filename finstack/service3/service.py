# Service 3: Analytics Service (Buggy)
class AnalyticsService:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        # BUG: Should check for valid value
        self.data.append(value)
        return True

    def average(self):
        # BUG: Should handle empty data
        return sum(self.data) / len(self.data)
