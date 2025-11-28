import db
import random

FILENAME = "money.txt"

def create_deck(suits, ranks, values):
    deck = []
    for suit in suits:
        for i, rank in enumerate(ranks):
            value = values[i]
            card = [suit, rank, value]
            deck.append(card)
    return deck

def deal_card(deck):
    hand = random.choice(deck)
    deck.remove(hand)
    return hand

def hit(hand):
    pass

def get_bet(money):
    while True:
            try:
                bet_amount = int(input("Bet amount (5-1000): "))
                if bet_amount < 5 or bet_amount > 1000:
                    print("Invalid bet amount, try again.")
                elif bet_amount > money:
                    print("You don't have enough money to make that bet, try again.")
                else:
                    #money -= bet_amount #disabled for testing
                    #db.write_money(money) # ^ 
                    break
            except ValueError:
                print("Invalid bet amount, try again.")
    return bet_amount

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    money = db.read_money()
    while True:
        bet = get_bet(money)
        deck = create_deck(suits, ranks, values)
        player_hand = []
        dealer_hand = []
        for i in range(0, 2):
            player_hand.append(deal_card(deck))
        for i in range(0, 2):
            dealer_hand.append(deal_card(deck))

if __name__ == "__main__":
    main()