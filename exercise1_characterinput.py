from datetime import *
current_year = int(date.today().strftime("%Y"))
name, age = input("What is your name and age? ").split()
age = int(age)
message = f"Howdy, {name}! You will turn 100 years old in the year {current_year + 100 - age}"
print(message)
repetitions = int(input("How many times would you like to repeat the above message? "))
print((message + "\n") * repetitions)