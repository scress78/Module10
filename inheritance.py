"""
Program: employee.py
Author: Spencer Cress
Date: 6/30/2020


"""
import datetime



class Person:
    def __init__(self, _last_name, _first_name, _address, _phone_number):
        """
        :param _last_name: string, employee's last name
        :param _first_name: string, employee's first name
        :param _address: string, employee's address
        :param _phone_number: string, employee's phone number
        """
        self.last_name = _last_name
        self.first_name = _first_name
        self.address = _address
        self.phone_number = _phone_number
        #year = _start_date.strftime("%Y")
        #month = _start_date.strftime("%m")
        #day = _start_date.strftime("%d")

    def __str__(self):
        return "First name: " + str(self.first_name) + "\n" + "Last name: " + str(self.last_name) + "\n"\
               + "Address: " + str(self.address) + "\n" + "Phone Number: " + str(self.phone_number) + "\n"

    def __repr__(self):
        print(str(self.first_name))
        print(str(self.last_name))
        print(str(self.address))
        print(str(self.phone_number))

    def display(self):
        """
        :return: a string
        """
        return str(self.first_name + " " + self.last_name + "\n" + self.address + "\n")


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
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_characters.issuperset(_last_name) and not name_characters.issuperset(_first_name):
            raise ValueError
        if isinstance(_last_name, str) is False:
            raise AttributeError
        if isinstance(_first_name, str) is False:
            raise AttributeError
        if isinstance(_address, str) is False:
            raise AttributeError
        if isinstance(_phone_number, str) is False:
            raise AttributeError
        if isinstance(salary, int) is False:
            raise AttributeError

    def give_raise(self):
        """Sets Salaried Employee's salary to 45k"""
        self.salary = 45000

    def display(self):
        """Returns string of Salaried Employee"""
        return str((self.last_name + ", " + self.first_name+": " + self.phone_number + "\n" + self.address + "\nStart Date: " +
                    self.start_date.strftime("%m") + "/" + self.start_date.strftime("%d") +
                   "/" + self.start_date.strftime("%Y")+"\nSalary: $" + str(self.salary)))


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
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_characters.issuperset(_last_name) and not name_characters.issuperset(_first_name):
            raise ValueError
        if isinstance(_last_name, str) is False:
            raise AttributeError
        if isinstance(_first_name, str) is False:
            raise AttributeError
        if isinstance(_address, str) is False:
            raise AttributeError
        if isinstance(_phone_number, str) is False:
            raise AttributeError
        if isinstance(hourly_pay, float) is False:
            raise AttributeError

    def give_raise(self):
        """Sets Employee's hourly rate to $12/hr, yay??"""
        self.hourly_pay = 12.00

    def display(self):
        """Returns string Hourly employee"""
        return str((self.last_name + ", " + self.first_name+": " + self.phone_number + "\n" + self.address + "\nStart Date: " +
                    self.start_date.strftime("%m") + "/" + self.start_date.strftime("%d") +
                   "/" + self.start_date.strftime("%Y")+"\nHourly Pay $" + str('%.2f' % self.hourly_pay)))


# driver
me = SalariedEmployee("Spencer", "Cress", "moon", "319-888-8888", datetime.datetime.now(), 40000)
print(me.display())
me.give_raise()
print(me.display())
me2 = HourlyEmployee("Spencer", "Cress", "moon", "319-888-8888", datetime.datetime.now(), 10.00)
print(me2.display())
me2.give_raise()
print(me2.display())
