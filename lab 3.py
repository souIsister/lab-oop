games = []

while True:
    print("[ MENU OPTIONS ]")
    print("1 - Add a game")
    print("2 - Search for a game")
    print("3 - Remove a game")
    print("4 - View all games (Sorted)")
    print("0 - Exit Program")

    choice = input("Enter your choice: ")
    if choice == "0":
        break

    elif choice == "1":
        while True:  # fixed (lowercase w)
            game = input("Enter a game to add (press 'x' to stop): ")  # fixed parenthesis
            if game.lower() == "x":
                break
            games.append(game)  # fixed indentation
            print(f"{game} added successfully")

    elif choice == "2":
        search_game = input("Enter a game to search: ")
        count = 0
        for g in games:
            if g == search_game:
                count += 1
        if count > 0:
            print(f"{search_game} found in {count} occurrence(s) in the list.")
            print()
        else:
            print("No games found with that name.")
            print()

    elif choice == "3":
        remove_game = input("Enter a game to remove: ")
        if remove_game in games:
            games.remove(remove_game)
            print(f"{remove_game} removed successfully.")
            print()
        else:
            print("No games found with that name.")
            print()

    elif choice == "4":
        if len(games) > 0:
            games.sort()
            print("\nGames List (Sorted):")
            for g in games:
                print(f"- {g}")
        else:
            print("No games in the list yet.")
            print()

    else:
        print("Invalid input. Try again.")
        print()
