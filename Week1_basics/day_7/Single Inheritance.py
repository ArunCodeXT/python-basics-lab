class Father:
    def money(self):
        print("Has 5 lakh rupees")

class Son(Father):
    def bike(self):
        print("Owns a KTM")

s = Son()
s.money()   # from Father
s.bike()    # from Son
