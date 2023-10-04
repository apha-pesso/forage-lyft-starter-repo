# SternmanEngine Class

from serviceable import Serviceable


class SternmanEngine(Serviceable):
    '''SternmanEngine Class'''

    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        '''Returns True if the warning light is on, False otherwise'''
        if self.warning_light_is_on:
            return True
        else:
            return False
