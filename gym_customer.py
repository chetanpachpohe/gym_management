class GymCustomer:

    def __init__(self, name, age, gender, mobile_number, email_id, bmi, membership, regimen):
        self._name = name
        self._age = age
        self._gender = gender
        self._mobile_number = mobile_number
        self._email_id = email_id
        self._bmi = bmi
        self._membership = membership
        self._regimen = regimen

    def get_mobile_number(self):
        return self._mobile_number

    def get_membership_duration(self):
        return self._membership

    def get_regimen(self):
        return self._regimen

    def set_membership_duration(self, membership_duration):
        self._membership = membership_duration
        return self

    def get_display_obj(self):
        print(f'Name: {self._name}\nAge: {self._age}\nMobile Number: {self._mobile_number}\nBMI: {self._bmi}\n'
              f'Membership Duration: {self._membership}')


