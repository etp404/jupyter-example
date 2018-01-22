from upside.systemsimulation.AdjustmentZoneCalculator import AdjustmentZoneCalculator
from upside.systemsimulation.Battery import Battery


class DFFRService(object):
    def __init__(self, battery=Battery(),
                 adjustmentCalculator=AdjustmentZoneCalculator(freq_min=49.7, freq_max=50.3,deadband=0.03,freq_opt=50),
                 freq_opt = 50, deadband = 0.03, freq_max=50.3, freq_min=49.7):
        self._freq_opt = freq_opt
        self._deadband = deadband
        self._freq_max = freq_max
        self._freq_min = freq_min
        self._battery = battery
        self._adjustmentCalculator = adjustmentCalculator

    def regulate_load(self, frequency, time_interval):
        if (self._in_deadband(frequency)):
            return self._battery.deliver(0, time_interval)
        elif (self._frequence_below_fMin(frequency)):
            return self._battery.deliverMax(time_interval)
        elif (self._frequency_exceeds_fMax(frequency)):
            return self._battery.storeMax(time_interval)
        elif (frequency>self._freq_opt):
            return self._battery.store(self._adjustmentCalculator.amountOfPowerChangeIfTooHigh(frequency), time_interval)
        elif (frequency<self._freq_opt):
            return self._battery.deliver(self._adjustmentCalculator.amountOfPowerChangeIfTooLow(frequency), time_interval)

    def _frequence_below_fMin(self, frequency):
        return frequency - self._freq_min  < 0

    def _frequency_exceeds_fMax(self, frequency):
        return frequency - self._freq_max > 0

    def _in_deadband(self, frequency):
        return abs(self._freq_opt - frequency) <= self._deadband / 2