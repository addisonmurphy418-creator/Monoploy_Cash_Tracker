
class Tracker:
    def __init__(self, player_names):
        self.player_names = player_names
        self.track_money = {}

        #All Players start with 1,500 money
        for name in player_names:
            self.track_money[name] = 1500
            print(f"{name} has been created with {self.track_money[name]} money!")

    def passGo(self, player):
        self.track_money[player] += 200

    def takeMoney(self, player, value):
        self.track_money[player] -= value

    def giveMoney(self, player, value):
        self.track_money[player] += value

    def giveTo (self, player, second_player, value):
        self.track_money[player] -= value
        self.track_money[second_player] += value