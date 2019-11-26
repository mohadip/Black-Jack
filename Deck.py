class Deck:
  def __init__(self):
    self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
    self.shuffle()

  def shuffle(self):
    # shuffle the deck 
    random.shuffle(self.cards)    # use random.shuffle()

  def deal_card(self):
    return self.cards.pop(0)    # deal a card object from the deck
  
  def __str__(self):
    s=''    # return a string representing the deck
    for card in self.cards:
      s = s + str(card) + ' '
    return s