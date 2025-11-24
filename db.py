FILENAME = "money.txt"

def read_money():
    with open(FILENAME, "r") as infile:
        money = infile.readlines()
        return int(money[0])
    
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