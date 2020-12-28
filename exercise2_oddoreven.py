number = int(input("Enter a number! "))
if number % 4 == 0:
    print("That number can go into four!")
if number % 2 == 0:
    print("That number is even!")
else:
    print("That number is odd!")
num = int(input("Enter a number to be checked! "))
check = int(input("Enter the checker! "))
if num % check == 0:
    print("Check goes into num evenly!")
else:
    print("Check does not go into num evenly!")