import unittest
from src.Deck import Deck

class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck1 = Deck(fill=True)
        self.deck2 = Deck(fill=True)
        self.deck3 = Deck(fill=False)

    def test_shuffle(self):
        self.assertNotEqual(self.deck1._cards.__getitem__(0), self.deck2._cards.__getitem__(0))

    def test_createCards(self):
        self.assertEqual(len(self.deck1._cards), 52)

    def test_clearDeck(self):
        self.deck1.clearDeck()
        self.assertEqual(len(self.deck1._cards), 0)

    def test_emptyDeck(self):
        self.assertEqual(len(self.deck3._cards), 0)
        with self.assertRaises(Exception) as context:
            self.deck3.deal_Card(self.deck1)
        self.assertTrue('No more cards to Deal' in str(context.exception))
