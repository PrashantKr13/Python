import random
n=random.randint(1,30)
i=5
print(f"You have {i} number of guesses")
print("The number lies between 1 and 30")
while(1):
    i -= 1
    num=int(input("Guess the number:\n"))
    if(num>n):
        print("Your number is greater than the correct number")
        print(f"You have {i} guesses left")
    elif(num<n):
        print("Your number is less than the correct number")
        print(f"You have {i} guesses left")
    elif(num==n):
        print("congratulations!! You have guessed the correct number")
        print(f"You have used {5-i} number of guesses")
        break
    if(i==0):
        print("Game Over: You have no guess left")
        print(f"The nummber was {n}")
        break
end=input()
