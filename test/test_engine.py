# Test engine

import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    """Test CapuletEngine"""

    def test_capulet_needs_service(self):
        current_mileage = 30500
        last_service_mileage = 100
        engine = CapuletEngine(current_mileage, last_service_mileage)
        res = engine.needs_service()
        self.assertTrue(res)

    def test_capulet_does_not_need_service(self):
        current_mileage = 30000
        last_service_mileage = 100
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    '''Test SternmanEngine'''

    def test_sternman_needs_service(self):
        warning_light = True
        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_sternman_does_not_need_service(self):
        warning_light = False
        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    '''Test WilloughbyEngine'''

    def test_willoughby_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_does_not_need_service(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main(verbosity=2)
