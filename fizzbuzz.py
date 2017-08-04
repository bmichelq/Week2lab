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

"""
while True: #never ending game
    i = int(input("Please enter a number: "))
    fizzbuzz(i)
"""

def hundredfizz():
    for i in range (101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
i = 1
hundredfizz()
