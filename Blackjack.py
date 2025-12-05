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

def get_point_value(hand):
    points = 0
    aces = 0
    for card in hand:
        card_value = card[2]
        points += card_value
        if card_value == 11:
            aces += 1
    while points > 21 and aces > 0:
        points -= 10
        aces -= 1
    return points

def deal_card(deck):
    hand = random.choice(deck)
    deck.remove(hand)
    return hand

def hit(hand, deck):
    dealt_card = deal_card(deck)
    hand.append(dealt_card)
    return hand

def get_bet(money):
    while True:
            try:
                print(f"\nYou currently have {money} chips.")
                bet_amount = int(input("Bet amount (5-1000): "))
                if bet_amount < 5 or bet_amount > 1000:
                    print("Invalid bet amount, try again.")
                elif bet_amount > money:
                    print("You don't have enough chips to make that bet, try again.")
                else:
                    break
            except ValueError:
                print("Invalid bet amount, try again.")
    return bet_amount

def check_win(player_value, dealer_value, player_hand, bet, money):
    amount_of_players_cards = len(player_hand)
    if player_value == dealer_value:
        print("It's a tie!")
        return money
    elif player_value > 21:
        print("You bust!")
        money -= bet
    elif player_value == 21 and amount_of_players_cards == 2:
        print("Blackjack!")
        money += bet * 1.5
    elif player_value == 21 and amount_of_players_cards >= 3:
        if dealer_value > 21 or dealer_value < player_value:
            print("You win!")
            money += bet
        else:
            print("Dealer wins!")
            money -= bet
    elif player_value < 21:
        if dealer_value > 21 or dealer_value < player_value:
            print("You win!")
            money += bet
        else:
            print("Dealer wins!")
            money -= bet
    db.write_money(money)

def if_player_cant_bet(money):
    if money < 5:
        prompt = input("You don't have enough chips to make the minimum bet of 5 chips! Would you like to buy more chips? (y/n): ")
        if prompt.lower() == "y":
            money = 100
            print("You now have 100 chips to play with! Go get 'em!")
        else:
            print("We'll top you up to 100 chips, anyways. On the house!")
    db.write_money(money)
    return money

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    while True:
        money = db.read_money()
        if money < 5:
            money = if_player_cant_bet(money)
        else:
            hit_or_stand = ""
            dealer_value = 0
            player_value = 0
            bet = get_bet(money)
            deck = create_deck(suits, ranks, values)
            player_hand = []
            dealer_hand = []
            for i in range(2):
                player_hand.append(deal_card(deck))
            for i in range(1):
                dealer_hand.append(deal_card(deck))

            #display and deal hands
            for i in dealer_hand:
                print(f"\nDealer's show card:\n{i[1]} of {i[0]}\n")
            for i in range(1):
                dealer_hand.append(deal_card(deck))
            print("Player's hand:")
            for i in player_hand:
                print(f"{i[1]} of {i[0]}")

            while hit_or_stand.lower() != "stand":
                hit_or_stand = input("\nWould you like to hit or stand? (hit/stand): ")
                if hit_or_stand.lower() == "hit":
                    hit(player_hand, deck)
                    print("Player's hand:")
                    for i in player_hand:
                        print(f"{i[1]} of {i[0]}")
                elif hit_or_stand.lower() == "stand":
                    dealer_value = get_point_value(dealer_hand)
                    while dealer_value < 17:
                        hit(dealer_hand, deck)
                        dealer_value = get_point_value(dealer_hand)
                    player_value = get_point_value(player_hand)
                    

            print("Player's hand:")
            for i in player_hand:
                print(f"{i[1]} of {i[0]}")
            print("\nDealer's cards:")
            for i in dealer_hand:
                print(f"{i[1]} of {i[0]}")
            print(f"\nPlayer's points: {player_value}")
            print(f"Dealer's points: {dealer_value}")
            check_win(player_value, dealer_value, player_hand, bet, money)
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
    print("\nSee you soon!")
        

if __name__ == "__main__":
    main()