def fizzbuzz(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# this is a comment
"""
This is also a comment
on different lines
"""
while True: #never ending game
    i = int(input("Please enter a number: "))
    fizzbuzz(i)
