# WilloughbyEngine Class

from serviceable import Serviceable


class WilloughbyEngine(Serviceable):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        '''Returns True if the engine has more than 60,000 miles from last service, False otherwise'''
        return self.current_mileage - self.last_service_mileage > 60000
