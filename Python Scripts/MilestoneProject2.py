'''Blackjack Game: Player vs Dealer'''
import random
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}

class Card():
    '''Card class contains card suit, rank, value'''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def get_card(self):
        return f'{self.rank} of {self.suit}'

class Deck():
    '''Deck class holds standard 52 card deck'''
    def __init__(self):
        self.all_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_card_from_deck(self):
        return self.all_cards.pop()

class Dealer():
    '''Dealer follows conventional Blackjack rules
    to decide when to hit or stand'''
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []

    def add_card_to_hand(self, new_card):
        self.hand.append(new_card)

    def get_deal(self):
        '''Second card is dealt face down
            on initial deal to dealer'''
        return self.hand[0]

    def get_hand(self):
        return self.hand

    def decide(self, num):
        if num <= 16:
            return 'hit'
        return 'stand'

    def clear_hand(self):
        self.hand.clear()

class Player():
    '''Player contains player methods especially for bankroll'''
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = int(bankroll)
        self.hand = []

    def add_card_to_hand(self, new_card):
        self.hand.append(new_card)

    def add_to_bankroll(self, gains):
        self.bankroll += gains

    def bet(self, amt):
        self.bankroll -= amt

    def get_hand(self):
        return self.hand

    def clear_hand(self):
        self.hand.clear()

def show_hand(cards):
    hand = 'Cards are '
    for card in cards:
        hand += card.get_card() + '.'
    print(hand)
    print(f'Value of cards is {calculate_hand(cards)}')

def calculate_hand(cards):
    hand_value = 0
    aces_count = 0
    for card in cards:
        if card.rank == 'Ace':
            aces_count += 1
        hand_value += card.value
    if hand_value <= 11 and aces_count >= 1:
        hand_value += 10
    return hand_value

def is_busted(cards):
    hand_value = 0
    for card in cards:
        hand_value += card.value
    return hand_value > 21

def prompt_for_player_info():
    name = input('Enter your name: ')
    bankroll = input('Enter starting funds: ')
    while not bankroll.isdigit:
        print('Please enter valid number')
        bankroll = input('Enter starting funds: ')
    return name, int(bankroll)

def prompt_to_place_bet(player):
    bet = input('Place a bet: ')
    while not bet.isdigit or int(bet) > player.bankroll:
        print('Please enter valid number less than or equal to bankroll')
        bet = input('Place a bet: ')
    player.bet(int(bet))
    return int(bet)

def prompt_hit_or_stand(player):
    decision = input(f'Hit or stand: ')
    while decision.lower() not in ['hit', 'stand']:
        print(f"Not a valid entry. Enter 'hit' or 'stand'.")
        decision = input(f'Hit or stand: ')
    return decision.lower()

def prompt_keep_playing():
    decision = input(f'Keep playing? (Yes/No): ')
    while decision.lower() not in ['yes', 'no']:
        print(f"Not a valid entry. Enter 'Yes' or 'No'.")
        decision = input(f'Keep playing? (Yes/No): ')
    return decision.lower() == 'yes'

if __name__ == '__main__':
    print('***** Blackjack ******')
    p_name, bank = prompt_for_player_info()
    player = Player(p_name, bank)

    print(f'Hello {player.name}, you are starting with ${player.bankroll:0.2f} in chips')
    print("Let's play!")
    dealer = Dealer()
    print('Shuffling cards...')
    deck = Deck()
    deck.shuffle()

    keep_playing = True
    while keep_playing:
        #Place Bet
        print(f'Player bankroll is ${player.bankroll:0.2f}')
        bet = prompt_to_place_bet(player)
        print(f'You are betting ${bet:0.2f}')

        #Deal cards
        print(f'Dealing cards...')
        player.add_card_to_hand(deck.deal_card_from_deck())
        dealer.add_card_to_hand(deck.deal_card_from_deck())
        player.add_card_to_hand(deck.deal_card_from_deck())
        dealer.add_card_to_hand(deck.deal_card_from_deck())

        #Initial reveal of dealer hand
        print(f'The dealer is showing', end=' ')
        print(f'{dealer.get_deal()}')

        is_player_busted = False
        is_dealer_busted = False
        while (not is_player_busted and not is_dealer_busted):
            #The Play (Hit or Stand by player)
            continue_to_deal = True
            while continue_to_deal and not is_player_busted:
                print(f'Player', end=' ')
                show_hand(player.get_hand())
                decision = prompt_hit_or_stand(player)
                if decision == 'stand':
                    continue_to_deal = False
                else:
                    player.add_card_to_hand(deck.deal_card_from_deck())
                is_player_busted = is_busted(player.get_hand())

            if is_player_busted:
                print(f'Player', end=' ')
                show_hand(player.get_hand())
                print(f'Player is Bust!')
                break

            #The Dealer's Play (Hit or stand by dealer)
            '''If the total is 17 or more, it must stand.
            If the total is 16 or under, they must take a card. 
            The dealer must continue to take cards until the total is 17 or more, 
            at which point the dealer must stand. If the dealer has an ace, 
            and counting it as 11 would bring the total to 17 or more (but not over 21), 
            the dealer must count the ace as 11 and stand. '''
            continue_to_deal = True
            while continue_to_deal and not is_dealer_busted:
                print(f'Dealer', end=' ')
                show_hand(dealer.get_hand())
                decision = dealer.decide(calculate_hand(dealer.get_hand()))
                if decision == 'stand':
                    continue_to_deal = False
                else:
                    dealer.add_card_to_hand(deck.deal_card_from_deck())
                    print(f'Dealer has hit')
                is_dealer_busted = is_busted(dealer.get_hand())
            if is_dealer_busted:
                print(f'Dealer', end=' ')
                show_hand(dealer.get_hand())
                print(f'Dealer is Bust!')
                break
            if not continue_to_deal:
                break

        #Settlement
        dealer_hand_total = calculate_hand(dealer.get_hand())
        player_hand_total = calculate_hand(player.get_hand())
        if is_player_busted:
            print(f'Dealer wins ${bet:0.2f}')
        elif is_dealer_busted and not is_player_busted:
            bet *= 1.5
            print(f'Player wins ${bet:0.2f}')
            player.add_to_bankroll(bet)
        elif dealer_hand_total > player_hand_total:
            #player lost bet
            print(f'Dealer wins ${bet:0.2f}')
        elif dealer_hand_total < player_hand_total:
            #player won bet
            bet *= 1.5
            print(f'Player wins ${bet:0.2f}')
            player.add_to_bankroll(bet)
        elif dealer_hand_total == player_hand_total:
            #player drew
            print(f'Draw. Player gets back {bet:0.2f}')
            player.add_to_bankroll(bet)

        #Ask to keep playing
        keep_playing = prompt_keep_playing()
        if keep_playing:
            #reset deck and hands
            deck = Deck()
            deck.shuffle()
            player.clear_hand()
            dealer.clear_hand()
        else:
            print(f'You left with ${player.bankroll:0.2f}')
            break
        if player.bankroll < 1:
            print(f'You have ${player.bankroll:0.2f}')
            print(f'Insufficient funds. Get more chips.')
            break
