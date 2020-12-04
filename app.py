#author : saranbsoman

#begins here...

print("Welcome to my game !!")


name = input("Whats your name? >>> ")

print("Hey", name)

age = int(input(f"{name}.. whats your age? >>> "))

if age > 18:
    print("You're old enough to play")
    print(f"welcome {name}")
    q = input("Shall we start (yes/no) >>> ")
    if q.lower() == "no":
        print(f"goodbye {name}")

    else:
        print("Let's play !!")
        q = input("left or right ? >>> ")
        if q.lower() == "left":
            print("you lost")

        elif q.lower() == "right":
            print(f"{name}, you took right and reached a lake ...")
            q = input("Do you wanna take a boat or swim ? (boat/swim) >>> ")
            if q.lower() == "boat":
                print("You crossed the river. Mission accomplished!!!")
                print(f"{name}.. you have won!")

            elif q.lower() == "swim":
                print("You were eaten by a alligator and died, Mission failed")
                print(f"{name}.. you have lost!")

            else:
                print("wrong command")


        else:
            print("Wrong command")

else:
    print("you're not old enough to play this game")