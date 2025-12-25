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
print("Welcome to Treasure Island. Your mission is to find the treasure")
turn=input("Left or Right? ")
if turn == "Right" or "right" and 'R' or 'r':
    print("Game Over")
elif turn == "Left" or "left" and 'L' or 'l':
    print("Yes")
