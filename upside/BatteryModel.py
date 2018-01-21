class BatteryModel:

    def __init__(self, start_store,
                 max_discharge_rate=1.2,
                 max_charge_rate= 1,
                 self_discharge_rate=0.1,
                 max_capacity=1.6):
        self._energy_held = start_store
        self._max_discharge_rate = max_discharge_rate
        self._max_charge_rate = max_charge_rate
        self._self_discharge_rate = self_discharge_rate
        self._max_capacity = max_capacity

    def deliverMax(self, time_interval):
        return self.deliver(self._max_discharge_rate, time_interval)

    def storeMax(self, time_interval):
        return self.store(self._max_charge_rate-self._self_discharge_rate)

    def store(self, energyToStore):
        self._increaseEnergyHeld(energyToStore)
        return True

    def deliver(self, powerRequired, time_interval):
        energyRequired = powerRequired*time_interval/3600
        energyDischarged = self._self_discharge_rate*time_interval/3600
        energyLoss = energyRequired+energyDischarged
        if ((energyRequired==0) | (energyLoss<self._energy_held)):
            self._reduceEnergyHeld(energyLoss)
            return True
        else:
            self._energy_held=0
            return False

    def energy_capacity(self):
        return self._energy_held

    def _increaseEnergyHeld(self, amount):
        self._energy_held = self._energy_held + amount

    def _reduceEnergyHeld(self, amount):
        self._energy_held = max(0, self._energy_held - amount)