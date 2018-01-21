import unittest

from upside.BatteryModel import BatteryModel


class TestBatteryModel(unittest.TestCase):
    def test_given_battery_is__sufficiently_charged_energy_can_be_delivered(self):
        battery = BatteryModel(5, max_discharge_rate=1.2, self_discharge_rate=0.1)
        self.assertTrue(battery.deliver(4))
        self.assertEqual(1,battery.energy_capacity())

    def test_given_battery_is__unsufficiently_charged_energy_can_be_delivered(self):
        battery = BatteryModel(5, max_discharge_rate=1.2, self_discharge_rate=0.1)
        self.assertFalse(battery.deliver(6))
        self.assertEqual(0,battery.energy_capacity())
