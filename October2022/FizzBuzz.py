# 1. If number divisible by 3 return Fizz
# 2. If number by 5 return buzz
# 3. If by both return FizzBuzz
# 4. If by none, return number

'''def fizz_buzz():
    while True:
        nr = int(input("Please insert number: "))
        if nr % 3 == 0 and nr % 5 == 0: print("FizzBuzz")
        elif nr % 5 == 0: print("Buzz")
        elif nr % 3 == 0: print("Fizz")
        else: print(nr)

fizz_buzz()'''

#var2
'''
for i in range(1,101):
    output = ""
    if i % 3 == 0:
        output ="Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
'''

#var3
'''
for i in range(1, 101):
    output = "Fizz" if i % 3 == 0 else ""
    output += "Buzz" if i% 5 == 0 else ""

    print(i) if output=="" else print(output)
'''

#var4   -> one line solutions
for i in range(1,101):
    print("Fizz"*(i%3<1) +(i%5<3)*"Buzz" or i)