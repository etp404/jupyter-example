import unittest

from upside.BatteryModel import BatteryModel
from upside.DFFRService import DFFRService


class TestServiceModel(unittest.TestCase):
    def test_given_current_frequency_is_in_deadband_no_energy_delivered(self):
        battery = BatteryModel(0.1)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(50.015, time_interval=3600))
        self.assertTrue(dffrService.regulate_load(49.985, time_interval=1))
        self.assertAlmostEquals(0, battery.energy_capacity())

    def test_given_battery_has_enough_charge_system_can_apply_regulation_to_reduce_load(self):
        battery = BatteryModel(1.4)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(50.3, time_interval=3600))
        self.assertAlmostEquals(0.1, battery.energy_capacity())

    def test_given_battery_has_unsufficient_charge_system_cannot_apply_regulation_to_reduce_load(self):
        battery = BatteryModel(1.2)
        dffrService = DFFRService(battery=battery)
        self.assertFalse(dffrService.regulate_load(50.3, time_interval=3600))
        self.assertAlmostEquals(0, battery.energy_capacity())

    def test_given_battery_has_enough_space_system_can_apply_regulation_to_increase_load(self):
        battery = BatteryModel(0)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(49.97, time_interval=3600))
        self.assertAlmostEquals(0.9, battery.energy_capacity())