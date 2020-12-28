a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [i for i in a if i <= 5]
print(b)
user_num = int(input("Enter a number! "))
c = [i for i in a if i < user_num]
print(c)