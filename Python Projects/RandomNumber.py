import random
num = input("Enetr a Number: ")

if num.isdigit():
    num = int(num)

    if num <=0:
        print("Enter a number larger than Zero, Did you understood?")
        quit()
else:
    print("Please Enter a Number next time.")   
    quit() 

randomNumber = random.randint(0, num)
count =0

while True:
    count += 1
    guess = input("Guess your random number: ")
    if guess.isdigit():
        guess = int(guess)

    else:
        print("Please Enter a Number next time.")   
        quit() 

    if guess == num:
        print("you got it!!")
        quit()
    elif guess > num:
        print("you were above the random number")

    else: 
        print("you were below the random number")    

print("you guessed", count, "times")        

