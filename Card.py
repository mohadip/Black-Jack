class Card:
  def __init__(self, suit, rank):
    if (suit in SUITS) and (rank in RANKS):
      self.suit = suit
      self.rank = rank
    else:
      self.suit = None
      self.rank = None
      print "Invalid card: ", suit, rank

  def __str__(self):
    return self.suit + self.rank

  def get_suit(self):
    return self.suit

  def get_rank(self):
    return self.rank