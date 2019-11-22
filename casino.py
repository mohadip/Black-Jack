# Used for card shuffle

import random

# accessory class Color to differentiate player's card
# and dealer's card in different colors
class Color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

# print player's cards in Red
def redStr(hand):
  return Color.RED + hand.__str__() + Color.END

# print dealer's cards in Green
def greenStr(hand):
  return Color.GREEN + hand.__str__() + Color.END


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
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

        
# define hand class
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

 
        
# define deck class 
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


#define deal process
def deal():
  global chips
  print 'Now you have %d chips' %chips
  deck = Deck()
  while True:
    try:
      bet = int(raw_input('How much do you bet? '))
      if bet < 1 or bet > chips:
        print 'You bet is either less than 1 or more than what you have'
      else:
        break
    except ValueError:
      print 'Not a valid integer!'

  player = Hand()
  dealer = Hand()
 
 # deal two cards for each
  card1 = deck.deal_card()
  player.add_card(card1)
  shownCard = deck.deal_card()
  dealer.add_card(shownCard)
  card2 = deck.deal_card()
  player.add_card(card2)
  dealer.add_card(deck.deal_card())
  print "Your hands: " + redStr(player) 
  print "Dealer's shown card: " + greenStr(shownCard)

  if VALUES[card1.get_rank()] == VALUES[card2.get_rank()]: # check if need to split
    while True:
      flag = raw_input('Do you want to split(y/n)? ')
      if flag == 'y':
        if 2*bet > chips:
          print 'You can not split, because you do not have enough chips'
        else:
          print 'Split it into two hands. Now it is hand 1'
          player = Hand()
          player.add_card(card1)
          player.add_card(deck.deal_card())
          print "Your hands: " + redStr(player) 
          print "Dealer's shown card: " + greenStr(shownCard)
          dealNoSplit(player,dealer,deck,bet)

          # only allowed to play hand 2 if the player 
          # has enough chips
          if chips >= bet:
            print 'Let us move to hand 2'
            player = Hand()
            dealer = Hand()
            player.add_card(card2)
            shownCard = deck.deal_card()
            dealer.add_card(shownCard)
            player.add_card(deck.deal_card())
            dealer.add_card(deck.deal_card())
            print "Your hands: " + redStr(player) 
            print "Dealer's shown card: " + greenStr(shownCard)
            dealNoSplit(player,dealer,deck,bet)
          else:
            print 'Not enough chips to play hand 2\n'+\
                'The bet is %d, you only have %d chips left' %(bet, chips)
          break
      elif flag =='n':
        dealNoSplit(player,dealer,deck,bet)
        break
      else:
        print 'Wrong input, Please choose y/n'
  else:
    dealNoSplit(player,dealer,deck,bet)

# deal such that player cannot split hands again
# player only have options Hit, Stand, Surrender, Double down
def dealNoSplit(player,dealer,deck,bet):
  global chips

  # wait for player's decision
  while True:
    if player.get_value() == 21: # blackjack!
      break
    
    option = raw_input('Hit(h),Stand(s),Surrender(sr),Double(d)? ')
    if option == 'h': # Hit
      player.add_card(deck.deal_card())
      print "Your hands: " + redStr(player) 
      if player.get_value() > 21:
        break
    elif option == 'd': # Double down
      if 2*bet > chips :
        print 'You do not have enough chips to double down'
      else:
        player.add_card(deck.deal_card())
        print "Your hands: " + redStr(player) 
        bet *= 2
        print 'bet doubled, now it is %f' %bet
        if player.get_value() > 21:
          break
    elif option == 'sr': # Surrender
      bet *= 0.5
      print 'bet half, now it is %f' %bet
      break
    elif option == 's': # Stand
      break
    else:
      print 'Wrong input! Please type those letters shown in the brackets'
  
  # deal cards to dealer
  while dealer.get_value() < 17:
    dealer.add_card(deck.deal_card())

  #compare values and print final results
  pv = player.get_value()
  dv = dealer.get_value()
  print "Dealer's hands: " + greenStr(dealer)
  if pv > 21:
    print 'You get %s busted, dealer win!' %pv
    chips -= bet
    print 'Now you have %s chips' %chips
  elif dv > 21:
    print 'Dealer gets %s busted, you win!' %dv
    chips += bet
    print 'Now you have %s chips' %chips
  elif pv > dv:
    print 'You get %s, dealer gets %s, you win!' %(pv, dv)
    chips += bet
    print 'Now you have %s chips' %chips
  elif pv == dv:
    print 'You get %s, dealer gets %s, a push!' %(pv, dv)
  else:
    print 'You get %s, dealer gets %s, dealer win!' %(pv, dv)
    chips -= bet
    print 'Now you have %s chips' %chips


    
# main function 
if __name__ == '__main__':
  chips = 100  # total chips
  
  while True:
    deal() # main engine
    if chips > 0: # players can keep playing when they have chips  
      flag = raw_input('Quit(q)? or press Any key to continue ')
      if flag == 'q':
        break
    else:
      print 'I am sorry Sir/Madam, you go bankcrupcy\n' +\
            'You cannot play unless you buy more chips\n' +\
            'Gambling destroys familities, STOP'
      break