# Palindrome Model Class


from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        '''Returns True if the engine or battery needs service, False otherwise'''
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()