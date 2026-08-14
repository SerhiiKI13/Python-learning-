import random

def guess_game():

    number = random.randint(1,100)
    print(number)
    count = 0
    while True:
        num = int(input("Enter number: "))
        count+=1
        result = check_game(num,number)
        print(result)
        if result == "Correct!":
            print("Attempts: ",count)
            break

def check_game(guess,secret):
    if guess < secret:
        return "Too low"
    elif guess > secret:
        return "Too high"
    else: 
        return "Correct!"
        
guess_game()