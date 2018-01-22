import unittest

from upside.Battery import Battery
from upside.DFFRService import DFFRService


class TestServiceModel(unittest.TestCase):
    def test_given_current_frequency_is_in_deadband_no_energy_delivered(self):
        battery = Battery(initial_amount_of_energy_stored=0.1)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(50.015, time_interval=3600))
        self.assertTrue(dffrService.regulate_load(49.985, time_interval=1))
        self.assertAlmostEquals(0, battery.energy_stored())

    def test_given_battery_has_enough_charge_and_freqency_is_below_freq_min_system_can_apply_regulation_to_reduce_load(self):
        battery = Battery(initial_amount_of_energy_stored=1.4)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(49.8, time_interval=3600))
        self.assertAlmostEquals(0.6508771929, battery.energy_stored())

    def test_given_battery_has_unsufficient_charge_and_freqency_is_below_freq_min_system_cannot_apply_regulation_to_reduce_load(self):
        battery = Battery(initial_amount_of_energy_stored=1.2)
        dffrService = DFFRService(battery=battery)
        self.assertFalse(dffrService.regulate_load(49.6, time_interval=3600))
        self.assertAlmostEquals(0, battery.energy_stored())

    def test_given_battery_has_enough_space_and_frequency_is_above_freq_max_system_can_apply_regulation_to_increase_load(self):
        battery = Battery(initial_amount_of_energy_stored=0)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(50.31, time_interval=3600))
        self.assertAlmostEquals(0.9, battery.energy_stored())

    def test_given_battery_has_not_enough_space_and_frequency_is_above_freq_max_system_cannot_apply_regulation_to_increase_load(self):
        battery = Battery(initial_amount_of_energy_stored=1.5)
        dffrService = DFFRService(battery=battery)
        self.assertFalse(dffrService.regulate_load(50.31, time_interval=3600))
        self.assertAlmostEquals(1.6, battery.energy_stored())

    # Assuming for load reduction change in demand = freq/0.285-175.49
    def test_given_battery_has_capacity_and_frequency_is_above_required_system_applies_expected_regulation(self):
        battery = Battery(initial_amount_of_energy_stored=0)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(50.1, time_interval=3600))
        self.assertAlmostEquals(0.19824561403, battery.energy_stored())

    def test_given_battery_has__insufficient_capacity_and_frequency_is_above_required_system_cannot_apply_expected_regulation(self):
        battery = Battery(initial_amount_of_energy_stored=1.58)
        dffrService = DFFRService(battery=battery)
        self.assertFalse(dffrService.regulate_load(50.1, time_interval=3600))
        self.assertAlmostEquals(1.6, battery.energy_stored())

    # Assuming for load increases change in demand = freq/0.015-3332.33333
    def test_given_battery_has_sufficient_energy_and_frequency_is_below_required_system_applies_expected_regulation(self):
        battery = Battery(initial_amount_of_energy_stored=1.6)
        dffrService = DFFRService(battery=battery)
        self.assertTrue(dffrService.regulate_load(49.8, time_interval=3600))
        self.assertAlmostEquals(0.8508771929, battery.energy_stored())

    def test_given_battery_has_insufficient_energy_and_frequency_is_below_required_system_cannot_apply_expected_regulation(self):
        battery = Battery(initial_amount_of_energy_stored=0.3)
        dffrService = DFFRService(battery=battery)
        self.assertFalse(dffrService.regulate_load(49.8, time_interval=3600))
        self.assertAlmostEquals(0, battery.energy_stored())




