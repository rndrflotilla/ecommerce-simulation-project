# chris, payton and sydney's mini-game store

def main():
    import utility as u  # import utility file

    items = u.build_dict()  # read file / build dict function

    cart = {}
    users = {'srubb':['1234', 100], 'cclaps':['123', 90], 'pgiffen':['123', 70]}
    choice = ''
    while choice != 'e':
        print('Welcome to Mini Game Store')
        choice = u.menu()
        if choice == 's':
            # search menu & functions
            search_choice = u.search_menu()
            if search_choice == 'n':
                # search by name
                print('List of Available Games by Name\n-------------------------')
                for k, v in items.items():
                    print(k, v)
                print('-------------------------')
                item_name = input('Enter the name of the game you would like to purchase: ')
                item_quantity = int(input('Enter the quantity: '))
                if u.item_by_name(item_name, item_quantity, cart, items):
                    print('{} of {} added to your cart'.format(item_quantity, item_name))
                else:
                    print('{} was not found'.format(item_name))
            elif search_choice == 'g':
                # search by genre
                print('Available Genres\n--------------------')
                genre_list = []
                for k in items:
                    if items[k][0] in genre_list:
                        continue
                    else:
                        genre_list.append(items[k][0])
                for x in genre_list:
                    print(x)
                print('--------------------')
                item_genre = input('Enter the genre for games to display: ')
                print('Games available for {} genre:'.format(item_genre))
                if u.item_by_genre(item_genre, items):
                    item_name = input('Enter the name of the game you would like to purchase: ')
                    item_quantity = int(input('Enter the quantity: '))
                    if u.item_by_name(item_name, item_quantity, cart, items):
                        print('{} of {} added to cart'.format(item_quantity, item_name))
                    else:
                        print('{} not found'.format(item_name))
                else:
                    print('No games for that genre are available.')
            elif search_choice == 'c':
                # search by cost
                min_price = float(input('Enter min price: '))
                max_price = float(input('Enter max price: '))
                # display items by price range
                if u.item_by_cost(min_price, max_price, items):
                    item_name = input('Enter the name of the game you would like to purchase: ')
                    item_quantity = int(input('Enter the quantity: '))
                    if u.item_by_name(item_name, item_quantity, cart, items):
                        print('{} of {} added to your cart'.format(item_quantity, item_name))
                    else:
                        print('{} not found'.format(item_name))
                else:
                    print('No item found within the price range.')
            elif search_choice == 'p':
                # search by platform
                print('Available Platforms\n--------------------')
                platform_list = []
                for k in items:
                    if items[k][2] in platform_list:
                        continue
                    else:
                        platform_list.append(items[k][2])
                for x in platform_list:
                    print(x)
                print('--------------------')
                item_platform = input('Enter the platform for games to display: ')
                print('Games available for {} platform:'.format(item_platform))
                if u.item_by_platform(item_platform, items):
                    item_name = input('\nEnter the name of the game: ')
                    item_quantity = int(input('Enter the quantity: '))
                    if u.item_by_name(item_name, item_quantity, cart, items):
                        print('{} of {} added to your cart'.format(item_quantity, item_name))
                    else:
                        print('{} was not found'.format(item_name))
                else:
                    print('No games for that platform are available.')
            elif search_choice == 'c':
                # cancel
                break
            else:
                print('Invalid choice.')
        elif choice == 'd':
            # featured game
            u.featured_game(items, cart)
        elif choice == 'c':
            # checkout
            print('Please log in to check out')
            if u.login(users):
                total = u.checkout(cart)
                u.reward_points(cart, total)
            else:
                u.login(users)
        elif choice == 'e':
            print('Thank you for visiting Mini Game Store!')
        else:
            print('Invalid choice.')


main()

