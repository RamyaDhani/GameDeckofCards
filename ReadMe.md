**Problem Statement:**

Designing a card deck: These are poker-style playing cards (fifty-two cards in four suits: hearts, spade, clubs,
and diamonds, with a face value of Ace, 2-10, Jack, Queen and King).

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


