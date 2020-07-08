"""
Program: derived_class.py
Author: Spencer Cress
Date: 6/30/2020

derived class assignment
"""
import datetime


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        """
        :param lname: str last name
        :param fname: str first name
        :param addy: str address
        """
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + ":" + str(self.address)


class Student(Person):
    def __init__(self, student_id, lname, fname, major="Computer Science", gpa='0.0'):
        """
        :param lname: str last name
        :param fname: str first name
        :param addy: str address
        :param major: str major
        :param gpa: float gpa
        """
        self.student_id = student_id
        self.major = major
        self.last_name = lname
        self.first_name = fname
        self.gpa = gpa
    #first_name = Person.fname
    #last_name = Person.lname
    def display(self):
        """Displays student info"""
        return str(self.last_name)+", "+self.first_name+":("+str(self.student_id)+") "+self.major+" gpa: "+str(self.gpa)


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
