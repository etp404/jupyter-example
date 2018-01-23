
# Exists to calculate the required response of the system to a given frequency. I extracted it so I could
# use a couple of small unit tests to make sure that it's working as required.
class AdjustmentZoneCalculator(object):
    def __init__(self, freq_min, freq_max, deadband, freq_opt):
        self._freq_min = freq_min
        self._freq_max = freq_max
        self._deadband = deadband
        self._freq_opt = freq_opt

    def amount_of_power_change_if_too_low(self, frequency):
        return (2*(frequency-self._freq_opt)+self._deadband)/(2*(self._freq_min-self._freq_opt)+self._deadband)

    def amount_of_power_change_if_too_high(self, frequency):
        return (2*(frequency-self._freq_opt)-self._deadband)/(2*(self._freq_max-self._freq_opt)-self._deadband)
