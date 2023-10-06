# Spindler Battery Class

from serviceable import Serviceable


class SpindlerBattery(Serviceable):
    '''Spindler Battery Class'''

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        '''Returns True if the battery is more than 3 years old, False otherwise'''
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 3)
        return service_threshold_date < self.current_date
