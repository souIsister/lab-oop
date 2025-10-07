class User:
    def __init__(self, first, last, follow, friends):
        self.first = first
        self.last = last
        self.follow = follow
        self.friends = friends

    def describe(self):
        print(f"Hi! I am {self.first} {self.last}")
        print(f"Profile name: {self.first} {self.last} with {self.follow} followers")
        print("Your friends are: ", end="")
        for f in self.friends:
            print(f, end=" ")
        print()
