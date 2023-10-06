# Octoprime Tyre

from serviceable import Serviceable


class OctoprimeTyre(Serviceable):
    '''Octoprime Tyre class'''

    def __init__(self, tyre_array):
        self.tyre_array = tyre_array

    def needs_service(self):
        '''Returns True if the sum of the array is greater or equal to 3'''
        return sum(self.tyre_array) >= 3
