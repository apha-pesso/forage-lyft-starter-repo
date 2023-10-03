# Nubbin Battery Class

from abc import ABC
from car import Car
from datetime import datetime


class NubbinBattery(Car, ABC):
    '''NubbinBattery Class'''
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def battery_should_be_serviced(self):
        '''Returns True if the battery is more than 4 years old, False otherwise'''
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
