import random
import logging


class Card:
    def __init__(self, type, facevalue):
        self.value = str(facevalue)+'-'+type
        
    def __str__(self):
            return "% s" % (self.value)  
    
    def __repr__(self):
        return "% s" % (self.value)  

class Deck:
    _types = ["hearts", "spades", "clubs", "diamonds"]
    _specialfacevalues = ["J", "K", "Q", "A"]
    _maxdecksize = 52
    _cards = []
    
    def shuffle(self):
        r_list = random.sample(range(0,self._maxdecksize), self._maxdecksize)
        shuffled_cards = [self._cards[num] for num in r_list]
        self._cards = shuffled_cards
             
    def __init__(self, fill=True):
        self.fill = fill
        self._cards.clear
        logging.info('Init the Deck')
        if fill:
            self.createAllCards()
            self.shuffle()
            logging.info('Created the cards and shuffled it')
            
    def createAllCards(self):
        self._cards = []
        for ty in self._types:
            for num in range(2, 11):
                c = Card(ty, num)
                self._cards.append(c)
            for fc in self._specialfacevalues:
                c = Card(ty, fc)
                self._cards.append(c)

    def clearDeck(self):
        self._cards.clear()
        
    def addCardToDeck(self, card):
        self._cards.append(card)
    
    def deal(self, otherDeck):
        if len(self._cards) == 0:
            raise ValueError("No more cards")
        current_card = self._cards.pop()
        otherDeck._cards.append(current_card)
        
    
    def deal_Card(self, otherDeck):
        if len(self._cards) == 0:
            raise ValueError("No more cards to Deal")
        return self._cards.pop()

Card.__doc__ = "This is a placeholder for the facevalue of card (2 to 10, A,Q,K,J) " \
               "and type of the card i.e. Hearts, spades, diamonds and clubs"
Deck.__doc__ = "This is a placeholder for the deck, which holds a list of cards of type Card" \
               "and this has method clearDeck to clear all the cards in the list," \
               "method deal which takes a card from the current deck and puts it in another specified deck," \
               "method createCards which creates the 52 cards in the deck," \
               "method shuffle which creates 52 numbers in a random order and the corresponding cards are filled" \
               "which results in a shuffled card list"