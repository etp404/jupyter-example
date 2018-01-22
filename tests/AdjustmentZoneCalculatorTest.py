import unittest

from upside.AdjustmentZoneCalculator import AdjustmentZoneCalculator


class AdjustmentZoneCalculatorTest(unittest.TestCase):
    def test_given_frequency_between_deadline_and_fmin_expected_adjustment_calculated(self):
        fMin= 34
        fMax= 55
        f_opt= 50
        deadzone= 0.5
        calculator = AdjustmentZoneCalculator(fMin, fMax, deadzone, f_opt)
        self.assertEqual(1, calculator.amountOfPowerChangeIfTooLow(fMin))
        self.assertEqual(0, calculator.amountOfPowerChangeIfTooLow(f_opt-0.25))
        self.assertEqual(1, calculator.amountOfPowerChangeIfTooHigh(fMax))
        self.assertEqual(0, calculator.amountOfPowerChangeIfTooHigh(f_opt+0.25))
