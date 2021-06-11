print("welcome to my number guessing game!")
explain_rules = input("do you want a refresher in the rules?").lower()


while True:
    if explain_rules == "yes":
        import time
        time.sleep(1)
        print("I'm going to think of a number between 1 and 100 ")
        time.sleep(3)
        print("and you have to try and guess what number i'm thinking of.")
        time.sleep(3)
        print("Every time you guess i'll let you know if the answer is higher of lower until you get it right.")
        time.sleep(3)
        print("After you guess my number its your turn to think of a number")
        time.sleep(3)
        print("whoever guesses the others answer in the fewest turns win")
        time.sleep(3)
        print("good luck!")
        break
    if explain_rules == " yes":
        print("test")
        break
    if explain_rules == "no":
        break
    if explain_rules == " no":
        break
    else:
        print("please answer yes or no")
        explain_rules = input("do you want a refresher of the rules?").lower()

print("Time to start!")

p1 = 0
import random
n = random.randrange(0, 101)
#print(n)
guess = int(input("what number am i thinking of?"))
while True:
    if guess == n:
        print("correct!!")
        p1 += 1
        break
    if guess < n:
        print("go higher")
        guess = int(input("what number am i thinking of"))
        p1 += 1
    else:
        print("go lower")
        p1 += 1
        guess = int(input("what number am i thinking of"))
print("you guessed in "),print(p1),print("turns")

p2 = 0
p1_number = int(input("Think of a number"))
n2 = random.randrange(0, 101)
n3 = 101
n4 = 0
while True:
    if n2 == p1_number:
        import time
        time.sleep(1)
        print("your number is "),print(n2)
        p2 += 1
        break
    if n2 < p1_number:
        print("i'm guessing "), print(n2)
        print("too low")
        temp1 = n2
        n2 = random.randrange(n2, n3)
        n4 = temp1
        import time
        time.sleep(1)
        import time
        time.sleep(1)
        p2 += 1
    if n2 > p1_number:
        print("i'm guessing "), print(n2)
        print("too high")
        temp1 = n2
        n2 = random.randrange(n4, n2)
        n3 = temp1
        import time
        time.sleep(1)

        import time
        time.sleep(1)
        p2 += 1
print("I guessed in "), print(p2),print("turns")
if p1 < p2:
    print("you win")
if p1 > p2:
    print("I win")
if p1 == p2:
    print("draw")