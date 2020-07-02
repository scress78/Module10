"""
Program: student.py
Author: Spencer Cress
Date: 7/1/2020

Student class for Unit Test for a class assignment
"""

class Student:
    """Student class"""
    def __init__(self, lname='', fname='', major='', gpa=0.0):
        """
        :param lname: string, a student's last name
        :param fname: string, a student's first name
        :param major: string, a student's major
        :param gpa: float, a number between 0 and 5 that is the student's gpa
        """
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if lname == '':
            raise ValueError
        if fname == '':
            raise ValueError
        if major == '':
            raise ValueError
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and
                name_characters.issuperset(major)):
            raise ValueError
        if isinstance(gpa, float) is False:
            raise ValueError
        if gpa < 0 or gpa > 5:
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
