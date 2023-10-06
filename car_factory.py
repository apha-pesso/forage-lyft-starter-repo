# Cars are created here

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tyre.carrigan import CarriganTyre
from tyre.octoprime import OctoprimeTyre


class CarFactory():
    '''Car factory class'''

    @staticmethod
    def create_calliope(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage,
            tyre_array):
        '''Creates a Calliope model car'''
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tyres = CarriganTyre(tyre_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_glissade(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage,
            tyre_array):
        '''Creates a Glissade model car'''
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tyres = CarriganTyre(tyre_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_palindrome(
            current_date,
            last_service_date,
            warning_light_on,
            tyre_array):
        '''Creates a Palindrome model car'''
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tyres = OctoprimeTyre(tyre_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_rorschach(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage,
            tyre_array):
        '''Creates a Rorschach model car'''
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tyres = CarriganTyre(tyre_array)
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_thovex(
            current_date,
            last_service_date,
            current_mileage,
            last_service_mileage,
            tyre_array):
        '''Creates a Thovex model car'''
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tyres = OctoprimeTyre(tyre_array)
        car = Car(engine, battery, tyres)
        return car
