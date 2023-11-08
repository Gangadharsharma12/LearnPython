water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def check_resource(rw, rm, rcb, rdc, water, milk, coffee_beans, disposable_cups):
    req_list = [rw, rm, rcb, rdc]
    mac_list = [water, milk, coffee_beans, disposable_cups]
    global string
    string = ''
    global can_make
    can_make = False
    for i in range(4):
        if req_list[i] <= mac_list[i]:
            string = 'I have enough resources, making you a coffee!'
            can_make = True
            return string, can_make
        else:
            if i == 0:
                short_ = 'water'
            elif i == 1:
                short_ = 'milk'
            elif i == 2:
                short_ = 'coffee_beans'
            elif i == 3:
                short_ = 'disposable_cups'
            string = f'Sorry, not enough {short_}!'
            return string, can_make


def buy(water_, milk_, coffee_beans_, disposable_cups_, money_):
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if choice == '1':
        check_resource(250, 0, 16, 1, water_, milk_, coffee_beans_, disposable_cups_)
        if can_make:
            print(string)
            water -= 250
            milk -= 0
            coffee_beans -= 16
            disposable_cups -= 1
            money += 4
        else:
            print(string)
    if choice == "2":
        check_resource(350, 75, 20, 1, water_, milk_,coffee_beans_,disposable_cups)
        if can_make:
            print(string)
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            money += 7
        else:
            print(string)
    if choice == "3":
        check_resource(200, 100, 12, 1, water_, milk_, coffee_beans_, disposable_cups)
        if can_make:
            print(string)
            water -= 200
            milk -= 100
            coffee_beans -= 12
            disposable_cups -= 1
            money += 6
        else:
            print(string)
    if choice == "back":
        action_()
    else:
        action_()


def remaining(water_, milk_, coffee_beans_, disposable_cups_, money_):
    print(
        f'''The coffee machine has:
{water_} ml of water
{milk_} ml of milk
{coffee_beans_} g of coffee beans
{disposable_cups_} disposable cups
${money_} of money''')
    action_()

def fill(water_, milk_, coffee_beans_, disposable_cups_):
    global water
    global milk
    global coffee_beans
    global disposable_cups
    global money

    water_added = int(input("Write how many ml of water you want to add:"))
    milk_added = int(input("Write how many ml of milk you want to add:"))
    coffee_beans_added = int(input("Write how many grams of coffee beans you want to add:"))
    disposable_cups_added = int(input("Write how many disposable cups you want to add:"))
    water = water_ + water_added
    milk = milk_ + milk_added
    coffee_beans = coffee_beans_ + coffee_beans_added
    disposable_cups = disposable_cups_ + disposable_cups_added
    action_()


def take(m):
    global money
    print(f"I gave you ${m}")
    money -= money
    action_()


def action_():
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        buy(water, milk, coffee_beans, disposable_cups, money)
    elif action == 'take':
        take(money)
    elif action == 'remaining':
        remaining(water, milk, coffee_beans, disposable_cups, money)
    elif action == 'fill':
        fill(water, milk, coffee_beans, disposable_cups)
    elif action == 'exit':
        pass


action_()
