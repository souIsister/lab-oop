#Problem #1:
import time
ans = input("Start the timer[y/n]? ")
while ans == "y":
    my_time = int(input("Enter the time in seconds: "))
    for t in range(my_time, 0, -1):
        hours = t // 3600
        minutes = t % 3600 // 60
        seconds = t % 60
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIMES UP!")
    ans = input("Try again? ")
print("Bye!!! Thanks for using the program")

#Problem #2:
row = int(input("How many rows: "))
col = int(input("How many cols: "))
print("                  Multiplication Table:")
for i in range(1, row+1):
    for j in range(1, col+1):
        print("\t", i * j, end='')
    print("\n")
