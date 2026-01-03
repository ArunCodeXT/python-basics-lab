class vehicle:
    def start(self):
        return "vehicle started"
class car(vehicle):
    def start(self):
        return "car started"
ch=car()
print(ch.start())