
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car

class CarFactory():
    '''Car factory class'''

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        '''Creates a Calliope model car'''
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        '''Creates a Glissade model car'''
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        '''Creates a Palindrome model car'''
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        '''Creates a Rorschach model car'''
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        '''Creates a Thovex model car'''
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car