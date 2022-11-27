def menu():
    print('***MENU***\n[s]Search\n[d]Featured game of the day\n[c]Checkout\n[e]Exit')
    choice = input('Make a selection: ').lower()
    return choice


def search_menu():
    print('***SEARCH***\n[n]By name\n[g]By genre\n[c]By cost\n[p]By platform\n[c]Cancel')
    choice = input('Choose how you would like to search: ').lower()
    return choice


def build_dict():
    """ Interprets input.txt, returning the dictionary 'items' from the file. """
    items = {}
    with open("items.txt", "r") as f:  # opens "input.txt" in read mode, assigns variable f.
        lines = f.readlines()
        f.close()  # function reads the lines of the file and assigns those lines to "lines" variable.
        for line in lines:
            item_name, item_genre, item_price, item_platform, item_id = line.strip('\n').split(', ')
            items[item_name] = [item_genre, item_price, item_platform]
        return items  # split file into useful data, create dictionary with key [item_id].


def display_all_items(items):
    """ Display a dictionary key and value. """
    print('\nItem name-Genre-Price-Platform\n')
    print('------------------------------')
    for k in items.keys():
        print('{}-{}'.format(k, '-'.join(items[k])))
    print('-------------------------------')


def item_by_name(item_name, item_quantity, cart, items):
    """ Add an item to cart if item_name exists. Returns True if added, otherwise returns False. """
    if item_name in items:
        cart[item_name] = items[item_name]
        cart[item_name].append(int(item_quantity))
        return True
    else:
        return False


def item_by_genre(item_genre, items):
    """
    Displays genres to search by, takes user input then displays games in matching genre.
    Returns T if genre exists in items, false otherwise.
    """
    found = False
    for x in items:
        if item_genre in items[x][0]:
            print('{}-{}'.format(x, '-'.join(items[x])))
            found = True
    return found


def item_by_cost(min_price, max_price, items):
    """ Returns True if item found within the range and prints them. Otherwise, returns False. """
    found = False  # found changes to True when found a matching item
    # check if item price within the min and max range
    # item price can be obtained from value list index of -1
    for x, y in items.items():
        if min_price <= float(items[x][1]) <= max_price:
            # print matched items
            print(x, "-", y)
            # found set to True since item were found
            found = True
    return found


def item_by_platform(item_platform, items):
    """ Loops through key values for matching platform based on user input, returns True.
        If matching platform is found, and lists games available. """
    found = False
    # loop through key values
    for x in items:
        if item_platform in items[x][2]:
            # print matched items
            print('{}-{}'.format(x, '-'.join(items[x])))
            # found set to True since item were found
            found = True
    return found


def featured_game(items, cart):
    """ Puts keys into list and picks random number, displays index number of game.
        This game is the game of the day """
    import random
    games = []
    for k in items:
        games.append(k)
    num = random.randint(0, len(games))
    print("Today's featured game is {}!".format(games[num]))

    for k in items.keys():
        if games[num] == k:
            x = k
            print(k, items[k])

    choice = input('Add {} to cart? (y/n)'.format(games[num])).lower()
    if choice == 'y':
        quantity = int(input('Enter quantity: '))
        cart[x] = items[x]
        cart[x].append(int(quantity))
        print('{} of {} added to your cart'.format(quantity, x))
        return cart


def checkout(cart):
    """ This function calculates the total price of all purchased games.
        parameters: cart
        returns: total """
    total = 0
    for k in cart:
        total += float(cart[k][1]) * cart[k][-1]

    print('Games purchased:')
    for k in cart:
        print(cart[k][0])

    print('Your total is: {:.2f}'.format(total))

    return total


def login(users):
    """ Login menu for users to create a new account or login. While loop restricts user
        from exiting login menu until they are successfully logged in. """
    found = False
    while not found:
        print('***LOGIN MENU***\nLogin [l]\nAdd New Account [a]')
        selection = input('Make a selection: ')
        if selection == 'l':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if username in users:
                if password == users[username][0]:
                    print('You have successfully logged in, Your point total is', users[username][1])
                    return True
                else:
                    print('Incorrect password, please try again')

            else:
                print('Incorrect username, please try again')

        elif selection == 'a':
            username = input('Enter new username: ')
            if username in users:
                print('Username already taken, please enter different username')

            else:
                points = 0
                password = input('Enter new password: ')
                users[username] = [password, points]
                print('Account for {} created, please login'.format(username))

        else:
            print('Invalid Selection.')


def reward_points(cart, total):
    """ Function calculates the number of reward points by multiplying each item in cart by 5.
        If user opts to apply points, subtracts point value from item total."""
    i = ''
    for i in cart:
        i = len(cart) * 5
    user_input = ''
    while user_input != 'n':
        user_input = input("Would you like to apply reward points to this purchase? (y/n) ")
        if user_input == 'y':
            if i <= int(1):
                print("Your total rewards value is: " + str(i) + '\n')
                point_value = float(i * float(.5))
                total = total - (point_value*.1)
                print("Your new total is: " + str(total) + '\n')
            else:
                print("Your total rewards value is 0. ")
        return total
