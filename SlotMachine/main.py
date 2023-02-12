import random

#Global variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines

#generates random slot symbols in machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    #iterate through symbol_count dictionary and append them to symbol list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns_in_slot_machine = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns_in_slot_machine.append(column)
    return columns_in_slot_machine

#printing the slot machine
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

#allow user to deposit money
def deposit():
    while True:
        amount = input("How much amount would you like to deposit? $")
        
        #validating user input is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount to deposit.")
    return amount

#get number of lines to bet on
def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1-" + str(MAX_LINES) + ".")
        else:
            print("Please enter a valid number of lines to bet on.")
    return lines

#get user bets
def get_bet():
    while True:
        amount = input("How much amount would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount of bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid amount to bet.")
    return amount

def spin(balance):
    lines = get_num_of_lines()

    while True:    
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. \nCurrent balance: ${balance}\nCurrent bet amount: ${total_bet}")
        else: 
            break

    if lines == MIN_BET:
        print(f"You are betting ${bet} on {lines} line. Your total bet is equal to: ${total_bet}")
    else: 
        print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    if winnings > 0:
        print(f"Congratualations, you won ${winnings}!")
        print(f"You won on lines:", *winning_lines)
    else:
        print(f"You lost ${total_bet}!")

    return winnings - total_bet

#main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        if balance <= 0:
            deposit_more_money = input("You now have $0, would you like to deposit more money? (y/n).")
            if deposit_more_money == "y":
                balance = deposit()
            elif deposit_more_money == "n":
                break

        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

    
main()