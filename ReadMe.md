**Problem Statement:**

Code in an object-oriented programming language a collection of classes to model a deck of
cards. These are poker-style playing cards (fifty-two cards in four suits: hearts, spade, clubs,
and diamonds, with a face value of Ace, 2-10, Jack, Queen and King).

One of your classes should contain a shuffle method and a deal_card method.

**shuffle()**

Shuffle returns no value, but results in the cards in the deck being randomly permuted. Do not
use a library-provided shuffle function. You may use library-provided random number
generators.

**deal_card()**

This function should return one card from the deck to the caller.
A call to shuffle followed by 52 calls to deal_card will result in the caller being provided 52
cards of the deck in random order. If the caller makes a 53rd call to deal_card, no card is
dealt.

**Solution:**

**Main Driver Application: DealTheCards.py**

The orchestrator "DealTheCards" calls the FrontEndApp to initialize the UI, which in turn calls the
backend for dealing the cards from a deck to another(Dealt)

**UI: FrontEndApp.py**

This consists of the simple display of two sections: "Deck of Cards" and "Dealt Cards" with
two options to the user - Deal or Quit

**Configurations: ConfigParserUtility.py**

The UI needs configurations such as Canvas size, button configurations, etc which are specified 
in the config.ini file and these are read using the python ConfigParser module


**Backend: Deck.py and Card.py**

This has two components: Card which consists of the type and facevalue of a given card in the deck of cards
and Deck which is a placeholder to hold a list of cards and consists of shuffle, deal and clearDeck
features


**Tests:**

The folder "tests" consists of tests for the Backend functionalities

**Libraries Required**

tkinter, random, os, configParser

**How to run the application**

_python DealTheCards.py_

Please find attached the demo recording where:

1. A user starts the application

2. Deals all the cards by clicking on "Deal" button

3. Resets the deck when user gets to 53rd card

4. Quits the application



