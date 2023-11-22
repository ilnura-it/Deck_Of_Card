import random

card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
class Card:

   def __init__(self, suit, value):
      self.suit = suit
      self.value = value

   def __repr__(self):
      return f"{self.value} of {self.suit}"
   
class Deck:

   def __init__(self):
      self.cards = []
      self.cards = [Card(suit, value) for suit in card_suits for value in card_values]
      
   def __repr__(self):
      return f"Deck of {self.count()} cards"
   
   def _deal(self, num):
      count = self.count()
      if count == 0:
         raise ValueError("All cards have been dealt")
         
      new_deck = self.cards[-num:]
      self.cards = self.cards[:-num]
      return new_deck
   
   def count(self):
      return len(self.cards)
   
   def shuffle(self):
      if len(self.cards) == 52:
         return random.shuffle(self.cards)
      elif len(self.cards) < 53:
         raise ValueError("Only full decks can be shuffled")
   
   def deal_card(self):
      return self._deal(1)[0]

   def deal_hand(self, num):
      hand = [self.cards.pop(0) for _ in range(num)]
      return hand

my_deck = Deck()
# print(my_deck)
print(my_deck.deal_hand(5))