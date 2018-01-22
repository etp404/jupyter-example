class AdjustmentZoneCalculator(object):
    def __init__(self, freq_min, freq_max, deadband, freq_opt):
        self._freq_min = freq_min
        self._freq_max = freq_max
        self._deadband = deadband
        self._freq_opt = freq_opt

    def amountOfPowerChangeIfTooLow(self, frequency):
        return (2*(frequency-self._freq_opt)+self._deadband)/(2*(self._freq_min-self._freq_opt)+self._deadband)

    def amountOfPowerChangeIfTooHigh(self, frequency):
        return (2*(frequency-self._freq_opt)-self._deadband)/(2*(self._freq_max-self._freq_opt)-self._deadband)
