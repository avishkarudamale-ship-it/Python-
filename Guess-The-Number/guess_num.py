secret = 15
atm = 1
guess = int(input("enter your guess between (1-20) : "))
if secret == guess :
    print("Great ,got it on very 1st attempt ")

else :
    while guess != secret :
        difr = secret - guess
        if difr in range(0,4) or difr in range(0,-3,-1) :
            print("close")
        elif difr in range(4,14) :
            print("too low")
        elif guess >= 20 or guess <= 1:
            print("out of limit")
        else :
            print("too high")
        guess = int(input("enter your guess between (1-20) : "))
        atm += 1
    print(f"Correct! You took {atm} attempts.")
