#Day 3

#The Number is Odd or Even?
# num=int(input("number: "))

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")


#Pizza Delivery Program
# print("Welcome to PiZza wOrld")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill=0

# if size == 'S':
#     bill +=15
#     if pepperoni == 'Y':
#         bill+=2
#     if extra_cheese == 'Y':
#         bill+=1
# elif size == 'M':
#     bill +=20
#     if pepperoni == 'Y':
#         bill+=3
#     if extra_cheese == 'Y':
#         bill+=1
# else:
#     bill +=25
#     if pepperoni == 'Y':
#         bill+=3
#     if extra_cheese == 'Y':
#         bill+=1

# print(f"Your final bill is ${bill}")

#Trasure Game
print("Welcome to Treasure Island.")
print(" Your mission is to find the treasure")
choice1=input("left or right? ").lower()
if choice1 == "left":
    print("good job")
    choice2=input("swim or wait ").lower()
    if choice2 == "wait":
        print("good job")
        choice3=input("Which door? Red? blue? or Yellow ").lower()
        if choice3=="yellow":
            print("You Win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")
