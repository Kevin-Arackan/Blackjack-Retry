import art

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand):
    """
    Deals a card to the user
    Returns the updated hand
    """
    hand.append(random.choice(cards))
    return hand


def display_hands(player_hand, dealer_hand):
    """
    Displays the user and dealer hand
    """
    print(f"\nYour hand: {player_hand}\nDealer's first card: {dealer_hand[0]}")


def start_round():
    """
    Initializes the hands of both the player and the dealer.
    Returns the user and dealer hands
    """
    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player_hand = deal_card(player_hand)
    for _ in range(2):
        dealer_hand = deal_card(dealer_hand)
    
    return player_hand, dealer_hand


def adjust_hand(hand):
    """
    Look for any situation where we can reduce the sum of the deck by replacing an 11 with a 1
    Returns the adjusted hand
    """
    if 11 in hand:
        index = hand.index(11)
        hand[index] = 1
    
    return hand


def score(hand):
    """
    Obtains the score for a hand
    Returns an integer score for the hand
    """
    sum = 0
    for card in hand:
        sum += card
    return sum


def bust(hand):
    """
    Returns True if the score of the hand is over 21, False otherwise.
    """
    return score(hand) > 21


def blackjack(hand):
    """Returns True if the hand is a blackjack, False otherwise."""
    return score(hand) == 21 and len(hand) == 2


def hit():
    """
    Checks if the user wants to hit or stay their hand
    """
    valid_inputs = ['Hit', 'hit', 'Stay', 'stay']
    while True:
        user_input = input("Hit or stay? ")
        if user_input in valid_inputs:
            break
        print("Please type a valid input.")
    if user_input == 'Hit' or user_input == 'hit':
        return True
    return False
        

def player_play(player_hand, dealer_hand):
    """
    Play a round of Blackjack from the player's perspective.
    Returns the final hand of the player
    """
    display_hands(player_hand, dealer_hand)
    if not blackjack(player_hand):
        while hit():
            player_hand = deal_card(player_hand)
            if bust(player_hand):
                player_hand = adjust_hand(player_hand)
            display_hands(player_hand, dealer_hand)
            if bust(player_hand):
                return player_hand
    return player_hand
        

def dealer_play(hand):
    """
    Play a round of Blackjack from the dealer's perspective.
    Returns the final hand of the dealer
    """
    if not blackjack(hand):
        while score(hand) < 17:
            hand = deal_card(hand)
            if bust(hand):
                hand = adjust_hand(hand)
            if bust(hand):
                return hand
    return hand


def determine_score(player_hand, dealer_hand):
    """
    Determines whether or not the player won, lost, or tied.
    """
    print(f"\nYour final hand: {player_hand}\nDealer's final hand: {dealer_hand}")
    player_bust = bust(player_hand)
    dealer_bust = bust(dealer_hand)
    player_blackjack = blackjack(player_hand)
    dealer_blackjack = blackjack(dealer_hand)
    player_score = score(player_hand)
    dealer_score = score(dealer_hand)
    if player_bust:
        print("Bust! You lose!")
    elif dealer_bust:
        print("Dealer has bust! You win!")
    elif player_blackjack or dealer_blackjack:
        if player_blackjack and dealer_blackjack:
            print("Tie with Blackjack.")
        elif player_blackjack:
            print("Blackjack! You win!")
        else:
            print("Dealer has Blackjack! You lose!")
    elif player_score == dealer_score:
        print("Tie.")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")


def play_round():
    """
    Play a round of Blackjack
    """
    print("\n" * 100)
    print(art.logo)
    player_hand, dealer_hand = start_round()
    player_hand = player_play(player_hand, dealer_hand)
    dealer_hand = dealer_play(dealer_hand)
    determine_score(player_hand, dealer_hand)
    

def main():
    while True:
        play_blackjack = input("Would you like to play a round of Blackjack? y or n: ")
        if play_blackjack == 'y':
            play_round()
        else:
            break
        
        
if __name__ == "__main__":
    main()