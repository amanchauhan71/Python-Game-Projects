import random
import math

number1 = int(input("Enter the lower bound"))
number2 = int(input("Enter the Upper bound"))

print("You have only",round(math.log(number2 - number1 + 1, 2))," chances to guess the integer!\n")

x = random.randint(number1 , number2)


count=0
while count < math.log(number2 - number1 + 1, 2):
    count += 1
    guess = int(input("Guess the number"))
    if x== guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(number2 - number1 + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
