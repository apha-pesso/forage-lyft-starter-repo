# Rorschach Model Class


from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(WilloughbyEngine, NubbinBattery):
    '''Rorschach Model Class'''
    def needs_service(self):
        '''Returns True if the engine or battery needs service, False otherwise'''
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()