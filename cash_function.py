
class Tracker:
    def __init__(self, player_names):
        self.player_names = player_names
        self.track_money = {}

        #All Players start with 1,500 money
        for name in player_names:
            self.track_money[name] = 1500
            print(f"{name} has been created with {self.track_money[name]} money!")

        self.track_money["Bob"] -= 200

    def take_money(self, player):
        pass