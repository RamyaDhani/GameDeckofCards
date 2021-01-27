import unittest
from src.Deck import Card

class CardTest(unittest.TestCase):
    def test_card(self):
        card = Card("2", "Hearts")
        self.assertEqual(card.value, "Hearts-2")
