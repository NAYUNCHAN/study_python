'''
#Data Type

#Subscipting
print("Hello"[-1])

#String
print("123"+"456")

#Integer
print(123 + 456)

#Large Integers
print(123_123_123_123) # _는 무시 (즉 사람들이 보기 편하도록 _로 구분지어 작성)

#Float
print(3.141592)

#Boolean
print(True)
print(False)

#Data Quiz
# 3/3 all correct

#Use type function
print(type(123))
print(type(1.23))
print(type("123"))
print(type(True))
'''
'''
age=int(input("Your Age: "))
print(age + 1)
'''

#TypeError, Checking and Conversion
# Q1: print("Number of letters in your name: " + len(input("Enter Your name")) 
#Answer
print("Number of letters in your name: " + str(len(input("Enter Your name "))))
