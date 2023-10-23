from random import shuffle
class Card:

   def __init__(self, suit, value):
      self.suit = suit
      self.value = value

   def __repr__(self):
      return f"{self.value} of {self.suit}"
   
class Deck:

   def __init__(self):
      values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
      suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
      self.cards = []
      for suit in suits:
         for val in values:
            self.cards.append(Card(val, suit))
      # print(self.cards)

   def __repr__(self):
      return f"Deck of {self.count()} cards"

   def count(self):
      return len(self.cards)
   
   def _deal(self, num):
      count = self.count()
      actual = min([count, num])
      print(f"Going to remove {actual} cards")
      if count == 0:
         raise ValueError("All cards have been dealt")
      cards = self.cards[-actual:]
      self.cards = self.cards[:-actual]
      return cards

   def deal_card(self):
      return self._deal(1)[0]
   
   def deal_hand(self, hand_size):
      return self._deal(hand_size)
   
   def shuffle(self):
      if self.count() < 52:
         raise ValueError("Only full decks can be shuffled")
      shuffle(self.cards)
      return self

d = Deck()
print(d.shuffle())
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(hand)
print(d.cards)
card2 = d.deal_card()