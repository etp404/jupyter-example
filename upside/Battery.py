class Battery:

    def __init__(self,
                 initial_amount_of_energy_stored=0.8,
                 max_discharge_rate=1.2,
                 max_charge_rate= 1,
                 self_discharge_rate=0.1,
                 max_capacity=1.6):
        self._energy_stored = initial_amount_of_energy_stored
        self._max_discharge_rate = max_discharge_rate
        self._max_charge_rate = max_charge_rate
        self._self_discharge_rate = self_discharge_rate
        self._max_capacity = max_capacity

    def energy_stored(self):
        return self._energy_stored

    def deliverMax(self, time_interval):
        return self.deliver(self._max_discharge_rate, time_interval)

    def storeMax(self, time_interval):
        return self.store(self._max_charge_rate, time_interval)

    def store(self, powerToStore, time_interval):
        energyToStore = powerToStore * time_interval / 3600
        totalEnergyIncreaseInBattery = energyToStore - self._energyDischangedInInterval(time_interval)

        if (self._energyIncreaseWouldExceedCapacity(totalEnergyIncreaseInBattery)):
            self._energy_stored = self._max_capacity
            return False
        else:
            self._increaseEnergyHeld(totalEnergyIncreaseInBattery)
            return True

    def deliver(self, powerRequired, time_interval):
        energyRequired = powerRequired*time_interval/3600
        energyLoss = energyRequired + self._energyDischangedInInterval(time_interval)

        if ((energyRequired==0) | (energyLoss<self._energy_stored)):
            self._reduceEnergyHeld(energyLoss)
            return True
        else:
            self._energy_stored=0
            return False

    def _energyDischangedInInterval(self, time_interval):
        energyDischarged = self._self_discharge_rate * time_interval / 3600
        return energyDischarged


    def _increaseEnergyHeld(self, amount):
        self._energy_stored = self._energy_stored + amount

    def _reduceEnergyHeld(self, amount):
        self._energy_stored = max(0, self._energy_stored - amount)

    def _energyIncreaseWouldExceedCapacity(self, totalEnergyIncreaseInBattery):
        return (self._energy_stored + totalEnergyIncreaseInBattery - self._max_capacity) >= 1e-5