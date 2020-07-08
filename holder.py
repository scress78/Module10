class SalariedEmployee:
    def __init__(self, _last_name, _first_name, _address, _phone_number, start_date, salary):
        """
        :param _last_name: string, employee's last name
        :param _first_name: string, employee's first name
        :param _address: string, employee's address
        :param _phone_number: string, employee's phone number
        :param start_date: datetime, employee's start date
        :param salary: double, employee's salary
        """
        self.last_name = _last_name
        self.first_name = _first_name
        self.address = _address
        self.phone_number = _phone_number
        self.start_date = start_date
        self.salary = salary



class HourlyEmployee(Person):
    def __init__(self, _last_name, _first_name, _address, _phone_number, start_date, hourly_pay):
        """
        :param _last_name: string, employee's last name
        :param _first_name: string, employee's first name
        :param _address: string, employee's address
        :param _phone_number: string, employee's phone number
        :param start_date: datetime, employee's start date
        :param hourly_pay: double, employee's hourly pay
        """
        self.last_name = _last_name
        self.first_name = _first_name
        self.address = _address
        self.phone_number = _phone_number
        self.start_date = start_date
        self.hourly_pay = hourly_pay


    def display(self):
        pass

    def give_raise(self):
        pass
