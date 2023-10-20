class Card:

   def __init__(self, suit, value):
      self.suit = suit
      self.value = value

   def __repr__(self):
      return f"Card {self.suit} {self.value}"
   
class Deck:

   def __init__(self, cards):
      self.cards = cards

   def __repr__(self):
      return f"Deck of {self.cards} cards"
   
card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

card = [val for val in card_values]