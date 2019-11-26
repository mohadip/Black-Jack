class Hand:
  def __init__(self):
    self.playerHand = []

  def __str__(self):
    s=''    # return a string representation of a hand
    for card in self.playerHand:
      s = s + str(card) + ' '
    return s

  def add_card(self, card):
    self.playerHand.append(card)    # add a card object to a hand

  def get_value(self):
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    # compute the value of the hand, see Blackjack video
    v=0
    for card in self.playerHand:
      rank = card.get_rank()
      v += VALUES[rank]
    for card in self.playerHand:
      rank = card.get_rank()
      if rank == 'A' and v <= 11:
        v += 10
    return v