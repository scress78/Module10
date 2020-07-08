"""
Program: employee.py
Author: Spencer Cress
Date: 6/30/2020


"""
import datetime


class Person:
    def __init__(self, _last_name, _first_name, _address, _phone_number, _salaried, _salary, _start_date):
        """
        :param _last_name: string, employee's last name
        :param _first_name: string, employee's first name
        :param _address: string, employee's address
        :param _phone_number: string, employee's phone number
        :param _salaried: boolean, True, False is employee salaried
        :param _salary: double, employee's salary, either yearly or hourly
        :param _start_date: datetime, employee's start date
        """
        self.last_name = _last_name
        self.first_name = _first_name
        self.address = _address
        self.phone_number = _phone_number
        self.salaried = _salaried
        self.salary = _salary
        self.start_date = _start_date
        if _salaried is True:
            self.salary_statement = "Salaried Employee: $"+str(+_salary)+"/year"
        elif _salaried is False:
            self.salary_statement = "Hourly Employee: $"+str(_salary)+"/hour"
        #year = _start_date.strftime("%Y")
        #month = _start_date.strftime("%m")
        #day = _start_date.strftime("%d")

    def __str__(self):
        return "First name: " + str(self.first_name) + "\n" + "Last name: " + str(self.last_name) + "\n"\
               + "Address: " + str(self.address) + "\n" + "Phone Number: " + str(self.phone_number) + "\n" + "Salary: "\
               + str(self.salary) + "\n" + "Start Date: " + str(self.start_date) + "\n"

    def __repr__(self):
        print(str(self.first_name))
        print(str(self.last_name))
        print(str(self.address))
        print(str(self.phone_number))
        print(str(self.salary))
        print(str(self.start_date))

    def display(self):
        """
        :return: a string
        """
        return str(self.first_name + " " + self.last_name + "\n" + self.address + "\n" + self.salary_statement +
                   "\n" + "Start date: " + self.start_date.strftime("%m") + "-" + self.start_date.strftime("%d") +
                   "-" + self.start_date.strftime("%Y"))


if __name__ == "__main__":
    emp = Person('Hall', 'Jackie', '555 5th Street \nMaxwell, Iowa',
                     '865-1344', False, 9.85, datetime.datetime.now())
    print(emp.display())
    del emp


