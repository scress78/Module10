"""
Program: invoice_class.py
Author: Spencer Cress
Date: 6/30/2020

"""


class Invoice:
    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price={}):
        """
        :param invoice_id: required: number
        :param customer_id: required: number
        :param last_name: required: string
        :param first_name: required: string
        :param phone_number: required: string
        :param address: required: string
        :param items_with_price: dictionary, optional
        """
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = items_with_price
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

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        tax_rate = .06
        subtotal = 0
        for items, prices in invoice.items_with_price.items():
            subtotal += prices
            #print(subtotal)
        tax = round(subtotal * tax_rate)
        #print(tax)
        total = tax + subtotal
        #print(total)
        if isinstance(tax, int) is True:
            tax = str(tax) + ".00"
        for items, prices in invoice.items_with_price.items():
            print(items+"...."+str(prices))
        print("Tax........" + tax)
        print("Total......"+str(total))

    def display(self):
        """
        :return: a string of Customer class
        """
        return str(str(self.customer_id)+self.last_name+self.first_name+self.phone_number+self.address+"\n"
                   + str(self.items_with_price))


"""if __name__ == "main":
    customer1 = Customer(123, "Moss", "Randy", "888-4444", "2 Fast St.")
    print(customer1.display())
    try:
        customer2 = Customer("123", "Moss", "Randy", "888-4444", "2 Fast St.")
    except AttributeError:
        print("Got an error, that's good!")"""


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()


"""customer1 = Invoice(123, 123, "Randy", "888-4444", "2 Fast St.", "Real Address", {'iPad': 799.99})
#print(customer1.display())
customer1.add_item({'Surface': 999.99})
#print(customer1.display())
print(customer1.create_invoice())"""
"""tax_rate = .06
subtotal = 0
for items, prices in customer1.items_with_price.items():
    subtotal += prices
    print(subtotal)
tax = round(subtotal * tax_rate)
print(tax)
total = tax + subtotal
print(total)
if isinstance(tax, int) is True:
    tax = str(tax) + ".00"

for items, prices in customer1.items_with_price.items():
    print(items+"...."+str(prices))
print("Tax........" + tax)
print("Total......"+str(total))"""
