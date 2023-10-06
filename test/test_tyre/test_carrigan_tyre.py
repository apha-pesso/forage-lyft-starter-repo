# Test Carrigan Tyre Class

import unittest
from tyre.carrigan import CarriganTyre


class TestCarrigan(unittest.TestCase):
    '''Test the Carrigan Tyre Class'''

    def test_tyre_should_be_serviced(self):
        tyre = CarriganTyre([0.6, 0.8, 0.5, 0.9])
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre = CarriganTyre([0.3, 0.7, 0.5, 0.8])
        self.assertFalse(tyre.needs_service())
