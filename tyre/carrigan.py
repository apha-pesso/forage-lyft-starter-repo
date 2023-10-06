# Carrigan Tyre

from serviceable import Serviceable


class CarriganTyre(Serviceable):
    '''Carrigan Tyre class'''

    def __init__(self, tyre_array):
        self.tyre_array = tyre_array

    def needs_service(self):
        '''Returns True is 1 or more of the array is greater than or equal to 0.9'''
        for tyre in self.tyre_array:
            if tyre >= 0.9:
                return True
        return False
