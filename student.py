class Student:
    """Student class"""
    def __init__(self, lname='', fname='', major='', gpa=0.0):
        if lname == '':
            raise ValueError
        if fname == '':
            raise ValueError

        if lname is None:
            raise ValueError

        try:
            self.last_name = lname
        except TypeError:
            raise ValueError
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
