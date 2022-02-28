import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame('poker')
        self.card_1 = Card('hearts', 1)
        self.card_2 = Card('clubs', 10)

    def test_has_ace__returns_true(self):
        self.assertEqual(True, self.game.check_for_ace(self.card_1))

    def test_get_highest_card(self):
        self.assertEqual(self.card_2, self.game.highest_card(self.card_1, self.card_2))

    def test_get_cards_total(self):
        cards = [self.card_1, self.card_2]
        self.assertEqual('You have a total of 11', self.game.cards_total(cards)) 