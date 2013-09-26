from Spades import Spades


class Play(object):

    def __init__(self):
        self._load_players(self._get_players())

    def _get_players(self):
        players = int((raw_input('Number of human players: ')))
        return players

    def _load_players(self, players=None):
        if players is None:
            players = 2
        #players += 1
        cards = 52 / (players + 1)
        self.spades = Spades(players, cards)

    def begin_game_console(self):
        self.spades.new_game()


def main():
    console = Play()
    console.begin_game_console()

if __name__ == "__main__":
    main()