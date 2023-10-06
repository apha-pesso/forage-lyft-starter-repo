# Testing the battery class

import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


# from ..battery import nubbin_battery

# NubbinBattery = __import__('../battery/nubbin_battery')

# NubbinBattery = nubbin_battery.NubbinBattery
# from ..battery.spindler_battery import
# SpindlerBattery = __import__('../battery/spindler_battery')


class TestNubbin(unittest.TestCase):
    '''Test the Nubbin Battery Class'''

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpinlder(unittest.TestCase):
    '''Test the Spindler Battery Class'''

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main(verbosity=2)
