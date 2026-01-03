class Player:
    def info(self):
        print(f"Player Name: {self.name}, Runs: {self.runs}")

p1 = Player()
p2 = Player()

p1.name = "Dhoni"
p1.runs = 183

p2.name = "Kohli"
p2.runs = 254

p1.info()
p2.info()
