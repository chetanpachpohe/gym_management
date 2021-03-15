class GymManagement:
    _customers = {}

    def __init__(self):
        pass

    def add_customer(self, customer):
        self._customers[customer.get_mobile_number()] = customer

    def get_customer_by_mobile_number(self, mobile_number):
        return self._customers.get(mobile_number, None)

    def delete_customer(self, mobile_number):
        del self._customers[mobile_number]


class Regimen:

    _regimens = {}

    def __init__(self, monday='rest', tuesday='rest', wednesday='rest', thursday='rest', friday='rest', saturday='rest', sunday='rest'):
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday

    def add_regimen(self, name):
        self._regimens[name] = self

    def delete_regimen(self, name):
        del self._regimens[name]

    def get_regimen_by_name(self, name):
        return self._regimens.get(name, None)

    def get_display_obj(self):
        print(f'Monday: {self.monday}\nTuesday: {self.tuesday}\nWednesday: {self.wednesday}\n'
              f'Thursday: {self.thursday}\n'
              f'Friday: {self.friday}\nSaturday: {self.saturday}\nSunday: {self.sunday}')
