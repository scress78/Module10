"""
Program: customer_class.py
Author: Spencer Cress
Date: 6/30/2020

The constructor is raising the error message. display() has proper code to convert
an integer into a string.
"""


class Customer:
    def __init__(self, customer_id=12345, last_name="Douglas", first_name="Doug", phone_number="444-9999", address="856 King Road"):
        """
        :param customer_id: required: number
        :param last_name: required: string
        :param first_name: required: string
        :param phone_number: required: string
        :param address: required: string
        """
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        if isinstance(customer_id, int) is False:
            raise AttributeError
        if isinstance(last_name, str) is False:
            raise AttributeError
        if isinstance(first_name, str) is False:
            raise AttributeError
        if isinstance(phone_number, str) is False:
            raise AttributeError
        if isinstance(address, str) is False:
            raise AttributeError

    def __str__(self):
        return str("Customer ID: " + str(self.customer_id)+"Last Name: " + self.last_name + "First Name: " +
                   self.first_name + "Phone Number: " + self.phone_number + "Address: " + self.address)

    def __repr__(self):
        return str(self.customer_id+self.last_name+self.first_name+self.phone_number+self.address)

    def display(self):
        """
        :return: a string of Customer class
        """
        return str(str(self.customer_id)+self.last_name+self.first_name+self.phone_number+self.address)


if __name__ == "main":
    customer1 = Customer(123, "Moss", "Randy", "888-4444", "2 Fast St.")
    print(customer1.display())
    try:
        customer2 = Customer("123", "Moss", "Randy", "888-4444", "2 Fast St.")
    except AttributeError:
        print("Got an error, that's good!")

customer1 = Customer(123, "Moss", "Randy", "888-4444", "2 Fast St.")
print(customer1.display())
