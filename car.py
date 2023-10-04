# Car base model class

from serviceable import Serviceable


class Car(Serviceable):
    '''Car class'''

    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        '''Returns True if the engine or battery needs service, False otherwise'''
        return self.engine.needs_service() or self.battery.needs_service()
