# Spindler Battery Class

from datetime import datetime
from abc import ABC
from car import Car

class SpindlerBattery(Car, ABC):
    '''Spindler Battery Class'''
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False