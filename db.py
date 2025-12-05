FILENAME = "money.txt"

def read_money():
    try:
        with open(FILENAME, "r") as infile:
            money = infile.readlines()
            return float(money[0])
    except FileNotFoundError:
        print("Couldn't find money file! creating new one with 100 dollars.")
        money = 100
        return float(money)
    
def write_money(money_amount):
    with open(FILENAME, "w", newline="") as outfile:
        outfile.write(str(money_amount))

def main():
    money_amount = read_money()
    print(money_amount)
    money_amount -= 10
    write_money(money_amount)

if __name__ == "__main__":
    main()