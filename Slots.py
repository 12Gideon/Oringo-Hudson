import random


def spin_row():
    symbols = ["❤️", "🍋", "🍉", "👨‍🎓", "🤑"]

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("|".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "❤️":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 2
        elif row[0] == "👨‍🎓":
            return bet * 10
        elif row[0] == "🤑":
            return bet * 30
    return 0


def main():
    balance = 10000
    print("Welcome to slots game!")

    print("Symbols:❤️🍋🍉👨‍🎓🤑  ")

    while balance > 0:
        print(f"Current balance: Ksh{balance}")

        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter a valid amount: ")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Invalid bet amount, minimum amount is Ksh:10 ")
            continue

        balance -= bet

        row = spin_row()
        print(row)
        print("spinning...........\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won Ksh{payout}")
        else:
            print("Sorry you lost !")

        balance += payout

        play_again = input("To spin again (N/Y): ").upper()

        if play_again != "Y":
            break
    print(f"Game  is finished your account balance is Ksh {balance}")


if __name__ == "__main__":
    main()