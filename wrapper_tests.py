import unittest
from wrapper import SpadesWeb

class NewSpadesInstanceTest(unittest.TestCase):
    def setUp(self):
        self.game = SpadesWeb(2)
        print(self.game)


    def tearDown(self):
        pass

    def test_init_needs_num_of_users_only(self):
        num_of_users = 2
        self.assertTrue(bool(SpadesWeb(2)))

    def test_init_subfunc_deals_correct_amt_of_cards(self):
        users = 2
        cards = self.game._cards_by_users(users)
        should_be = 52 /users
        self.assertEqual(cards, should_be)

    def test_game_controller_waits_on_input(self):
        pass

if __name__ == '__main__':
        unittest.main()

