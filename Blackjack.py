import db
import random

FILENAME = "money.txt"

def create_deck(suits, ranks):
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
    return deck
    
def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    money = db.read_money()
    while True:
        while True:
            try:
                bet_amount = int(input("Bet amount (5-1000): "))
                if bet_amount < 5 or bet_amount > 1000:
                    print("Invalid bet amount, try again.")
                else:
                    break
            except ValueError:
                print("Invalid bet amount, try again.")
        deck = create_deck(suits, ranks)
        print(deck)

if __name__ == "__main__":
    main()