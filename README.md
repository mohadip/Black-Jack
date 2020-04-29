# Blackjack Multi-User Web App

Simple multi-user BlackJack/21 web app built in [Node.js](https://nodejs.org) and [Angular](https://angularjs.org/).

## Description 

* Allows up to 7 users to connect from different windows/browsers and play BlackJack against a dealer. If more than 7 users connect, they enter a queue and wait for a slot to be freed. In any other case, users entering a running game will be prompted to wait for the next round, in which they will immediately take part.

* All users share the same Deck and can see each other's moves/cards (except cards that are hidden - two cards per user are hidden and one card for the dealer). 

* Users can `Hit` (take additional cards) or `Stick` (take a stand). Users take turns to play and have 10 seconds to act, which if passed, the respective user will be forced to *Stick* and the next player will take turn (a red 10-seconds countdown is shown next to the user's controls). 

* Dealer auto-plays last and determines losers/winners, while showing everyone their scores. The next game starts after a brief delay (approx. 10 secs - users are prompted accordingly).

* If windows are left idle, connected users will auto-play given the timer (`Stick` on every round after the 10-seconds countdown). This is the expected behaviour, although may lead to a potential bug (see *known issues* below).