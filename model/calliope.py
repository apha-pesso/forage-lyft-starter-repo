# Calliope Model Class


from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    '''Calliope Model Class'''
    def needs_service(self):
        '''Returns True if the engine or battery needs service, False otherwise'''
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()
