import unittest

from upside.Battery import Battery


class TestBattery(unittest.TestCase):
    def test_given_battery_is__sufficiently_charged_energy_can_be_delivered(self):
        battery = Battery(5, max_discharge_rate=1.2, self_discharge_rate=0.1)
        self.assertTrue(battery.deliver(4, 3600))
        self.assertAlmostEquals(0.9,battery.energy_capacity())

    def test_given_battery_is__unsufficiently_charged_energy_can_be_delivered(self):
        battery = Battery(5, max_discharge_rate=1.2, self_discharge_rate=0.1)
        self.assertFalse(battery.deliver(6, 3600))
        self.assertAlmostEquals(0,battery.energy_capacity())
