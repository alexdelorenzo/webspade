from Spades import Spades


class Play(object):

    def __init__(self):
        
        self._loadPlayers(self._getPlayers())

    def _getPlayers(self):
        players = int((raw_input('Number of human players: ')))
        return players

    def _loadPlayers(self, players=None):
        if players is None:
            players = 2
        #players += 1
        cards = 52 / (players + 1)
        self.spades = Spades(players, cards)

    def beginGameConsole(self):
        self.spades.new_game()


def main():
    console = Play()
    console.beginGameConsole()

if __name__ == "__main__":
    main()