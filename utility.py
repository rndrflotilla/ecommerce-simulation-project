def menu():
    print('\nMENU\n'.ljust(40, '-'), '\n[s]Search\n[d]Featured game of the day\n[c]Checkout\n[e]Exit')
    choice = input('Make a selection: ').lower()
    return choice


def search_menu():
    print('\nSEARCH\n'.ljust(40, '-'), '\n[n]By name\n[g]By genre\n[c]By cost\n[p]By platform\n[c]Cancel')
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
    num = random.randint(0, len(games)-1)
    print("\nToday's featured game is {}!".format(games[num]))

    for k in items.keys():
        if games[num] == k:
            x = k
            print(k, items[k])

    choice = input('\nAdd {} to cart? (y/n) '.format(games[num])).lower()
    if choice == 'y':
        quantity = int(input('Enter quantity: '))
        cart[x] = items[x]
        cart[x].append(int(quantity))
        print('\n{} of {} added to your cart.\nReturning to menu...'.format(quantity, x))
        return cart


def checkout(cart):
    """ This function calculates the total price of all purchased games.
        parameters: cart
        returns: total """
    total = 0
    for k in cart:
        total += float(cart[k][1]) * cart[k][-1]
    print('\nItems in cart:')

    for k in cart:
        print(k)
    print('\nYour total is: {:.2f}'.format(total))

    return total


def login(users):
    """ Login menu for users to create a new account or login. While loop restricts user
        from exiting login menu until they are successfully logged in. """
    found = False
    while not found:
        print('\nLOGIN MENU\n'.ljust(40, '-'), '\nLogin [l]\nAdd New Account [a]')
        selection = input('Make a selection: ')
        if selection == 'l':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if username in users:
                if password == users[username][0]:
                    print('\nYou have successfully logged in. \n Total reward points: ', str(round(users[username][-1])))
                    return True, username
                else:
                    print('\nIncorrect password, please try again.')

            else:
                print('\nIncorrect username, please try again.')

        elif selection == 'a':
            username = input('\nEnter new username: ')
            if username in users:
                print('Username taken, please enter alternate username.')
            else:
                points = 0
                password = input('Enter new password: ')
                users[username] = [password, points]
                print('Account "{}" created.'.format(username))
        else:
            print('Invalid Selection. Please try again.')


def reward_points(username, users, cart, total):
    """ Function calculates the number of reward points by multiplying each item in cart by 5.
        If user opts to apply points, subtracts point value from item total."""
    points = users[username][1]
    for item in cart:
        points += cart[item][-1] * 5
    if points > 0 and total > 0:
        user_input = input("Would you like to apply reward points to this purchase? (y/n) ")
        if user_input == 'y':
            print("Your total rewards value is: " + str(points) + '\n')
            if total-(points * .01) <= .1:
                max_points = total * .01
                points -= max_points
                users[username][-1] = points
                total = 0
                print("Your new total is: " + str(round(total, 2)) + '\n')
                choice = input('Submit transaction? (y/n) ')
                if choice == 'y':
                    print("Transaction submitted. Thanks for shopping with us.")
                    print("Your remaining points are: {:.2f}".format(users[username][-1]))
                    quit()
        else:
            total = total - (points * .01)
            points = 0
            users[username][-1] = points
            choice = input('Submit transaction? (y/n) ')
            if choice == 'y':
                print("Transaction submitted. Thanks for shopping with us.")
                print("Your remaining points are: {:.2f}".format(users[username][-1]))
                quit()
            return total
    return total
