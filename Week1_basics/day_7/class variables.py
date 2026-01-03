class Phone:
    # Class attribute (common for all phones)
    charger_type = "C-TYPE"

    # Constructor (runs when object is created)
    def __init__(self, brand, price):
        self.brand = brand       
        self.price = price  

    # Method to display data
    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Charger Type:", Phone.charger_type)
        print("----------------------")


# Creating objects (instances)
samsung = Phone("Samsung", 10000)
redmi = Phone("Redmi", 5000)
google = Phone("Pixel", 30000)

# Displaying details
samsung.display()
redmi.display()
google.display()
