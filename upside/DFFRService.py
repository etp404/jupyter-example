from upside.Battery import Battery


class DFFRService(object):
    _floatMaxPrecision = 1e-5

    def __init__(self, battery=Battery(), ideal_frequency = 50, deadband = 0.03, freq_max=50.3, freq_min=49.97):
        self._ideal_frequency = ideal_frequency
        self._deadband = deadband
        self._freq_max = freq_max
        self._freq_min = freq_min
        self._battery = battery

    def regulate_load(self, frequency, time_interval):
        if (self._in_deadband(frequency)):
            return self._battery.deliver(0, time_interval)
        elif (self._freq_max-frequency <= self._floatMaxPrecision):
            return self._battery.deliverMax(time_interval)
        elif (frequency - self._freq_min <= self._floatMaxPrecision):
            return self._battery.storeMax(time_interval)
        elif (frequency>self._ideal_frequency):
            return self._battery.store(self._amountOfPowerChangeIfTooHigh(frequency), time_interval)
        elif (frequency<self._ideal_frequency):
            return self._battery.deliver(self._amountOfPowerChangeIfTooLow(frequency), time_interval)

    def _requiredEnergyForNextSecond(self, frequency):
        pass

    def _in_deadband(self, frequency):
        return (abs(self._ideal_frequency - frequency)-self._deadband/2) <= self._floatMaxPrecision

    def _amountOfPowerChangeIfTooHigh(self, frequency):
        return frequency/0.285-175.49

    def _amountOfPowerChangeIfTooLow(self, frequency):
        return -frequency/0.015+3332.33333