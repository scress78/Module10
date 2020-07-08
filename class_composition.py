"""
Program: class_composition.py
Author: Spencer Cress
Date: 6/30/2020

Class composition assignment
Possible to return to this assignment and add validation for GPA. think about re-submitting
"""
import datetime


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'+str(self.address)


class Student:
    def __init__(self, person, major, start_date, gpa):
        """
        :param person: str information about a person
        :param major: str a student's major
        :param start_date: datetime a date
        :param gpa: float, a GPA
        """
        self.person = person
        self.major = major
        self.start_date = start_date
        self.gpa = gpa
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not name_characters.issuperset(major):
            raise ValueError
        if isinstance(major, str) is False:
            raise AttributeError
        if isinstance(gpa, float) is False:
            raise AttributeError

    def change_major(self):
        """Updates Major to 'Being Awesome'"""
        self.major = 'Being Awesome'

    def update_gpa(self):
        """Updates GPA to 3.0"""
        self.gpa = 3.0

    def display(self):
        """Displays student info"""
        return str(self.person.display()) + "\nMajor: " + self.major + "\nStart Date: " + self.start_date.strftime("%m")+"/"+self.start_date.strftime("%d")\
               + "/" + self.start_date.strftime("%Y")+"\nGPA: " + str(self.gpa)

#Driver
person1 = Person("Cress", "Spencer", "The Moon")
student1 = Student(person1, "Computer Science", datetime.datetime.now(), 4.0)
print(student1.display())
student1.change_major()
student1.update_gpa()
print(student1.display())
