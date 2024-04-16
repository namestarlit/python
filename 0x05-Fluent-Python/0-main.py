#!/usr/bin/env python3
from random import choice

try:
    Card = __import__("0-card").Card
    FrenchDeck = __import__("0-card").FrenchDeck
except ImportError as e:
    raise e

# Create an instance of Card class
beer_card = Card("7", "diamonds")
print(beer_card)

# create an instance of FrenchDeck class
deck = FrenchDeck()
print(len(deck))  # length of the deck
print(deck[0])  # the first card
print(deck[-1])  # the last card
print(choice(deck))  # a random card from deck
print(deck[:3])  # slicing
print(deck[12::13])

# iterate through the cards
for card in deck:
    print(card)

# iterate in reverse
for card in reversed(deck):
    print(card)

# using `in` operator because `deck` is iterable
print(Card("Q", "hearts") in deck)
print(Card("7", "beasts") in deck)

# sorting the cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_values = FrenchDeck.ranks.index(card.rank)
    return rank_values * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
