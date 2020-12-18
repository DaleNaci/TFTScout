from player import Player


class Lobby:
    def __init__(self):
        self.players = []
        self.total_uses = {}


    def add_player(self, summoner_name):
        player_obj = Player(summoner_name)
        self.players.append(player_obj)

        for champ, uses in player_obj.champ_uses.items():
            if champ in self.total_uses:
                self.total_uses[champ] += uses
            else:
                self.total_uses[champ] = uses


    def __str__(self):
        text = "Lobby\n"

        for p in self.players:
            text += str(p)

        return text
