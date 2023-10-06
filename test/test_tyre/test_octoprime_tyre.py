# Test the OctoPrime Tyre Class

import unittest
from tyre.octoprime import OctoprimeTyre


class TestOctoprime(unittest.TestCase):
    '''Test the Octoprime Tyre Class'''

    def test_tyre_should_be_serviced(self):
        tyre = OctoprimeTyre([1, 0.8, 0.5, 0.9])
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre = OctoprimeTyre([0.3, 0.7, 0.5, 0.8])
        self.assertFalse(tyre.needs_service())
