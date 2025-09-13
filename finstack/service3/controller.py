# Controller for Analytics Service (Buggy)
from service import AnalyticsService

service = AnalyticsService()

def add_data_controller(value):
    # BUG: No input validation
    return service.add_data(value)

def average_controller():
    # BUG: No error handling
    return service.average()
