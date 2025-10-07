from main import User

def test_user():
    users = []
    people = 0

    while True:
        again = input("Insert a record? [y/n]: ")
        if again.lower() == 'y':
            a = input("First name: ")
            b = input("Last name: ")
            c = int(input("Followers: "))

            num_friends = int(input("How many friends do you have? "))
            friends_list = []
            for i in range(num_friends):
                friend = input(f"Enter friend {i+1}: ")
                friends_list.append(friend)

            users.append(User(a, b, c, friends_list))
            people += 1
        else:
            break

    print("\nHere are the Records....\n")
    for u in users:
        u.describe()
        print("\n")

    print(f"\nThere are currently {people} Members in the Social Media page")

if __name__ == "__main__":
    test_user()
