from battery import Battery
from datetime import datetime
from Serviceable import Serviceable

class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return datetime(self.current_date - self.last_service_date).year >= 2