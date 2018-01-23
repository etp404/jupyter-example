class Battery:

    def __init__(self,
                 initial_amount_of_energy_stored=0.8,
                 max_discharge_rate=1.2,
                 max_charge_rate= 1,
                 self_discharge_rate=0.01,
                 max_capacity=1.6):
        self._energy_stored = initial_amount_of_energy_stored
        self._max_discharge_rate = max_discharge_rate
        self._max_charge_rate = max_charge_rate
        self._self_discharge_rate = self_discharge_rate
        self._max_capacity = max_capacity

    def energy_stored(self):
        return self._energy_stored

    def deliver_max(self, time_interval):
        return self.deliver(self._max_discharge_rate, time_interval)

    def store_max(self, time_interval):
        return self.store(self._max_charge_rate, time_interval)

    def store(self, power_to_store, time_interval):
        energy_to_store = power_to_store * time_interval / 3600
        total_energy_increase_in_battery = energy_to_store - self._energy_dischanged_in_interval(time_interval)

        if (self._energy_increase_would_exceed_capacity(total_energy_increase_in_battery)):
            self._energy_stored = self._max_capacity
            return False
        else:
            self._energy_stored += total_energy_increase_in_battery
            return True

    def deliver(self, power_required, time_interval):
        energy_required = power_required*time_interval/3600
        energy_loss = energy_required + self._energy_dischanged_in_interval(time_interval)

        if ((energy_required==0) | (energy_loss<self._energy_stored)):
            self._reduce_energy_held(energy_loss)
            return True
        else:
            self._energy_stored=0
            return False

    def _energy_dischanged_in_interval(self, time_interval):
        energy_discharged = self._self_discharge_rate * time_interval / 3600
        return energy_discharged


    def _reduce_energy_held(self, amount):
        self._energy_stored = max(0, self._energy_stored - amount)

    def _energy_increase_would_exceed_capacity(self, total_energy_increase_in_battery):
        return self._energy_stored + total_energy_increase_in_battery >= self._max_capacity