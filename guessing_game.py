import random 
def play_game ():
    number = random.randint (1, 100)
    attemp = 0
    print ("=========================")
    print("|    Number Gussing Game |")
    print("=========================")
    print("I have choice a nubers b/w 1 to 100")
    print("Try to Guss MY Number")
    while True:
     guess = int(input("Enter your Number "))
     attemp +=1
     if guess == number:
        print("Hurra! You Win the Game")
        print("number",number)
        print("attemp",attemp)
        break
     elif guess < number:
        print("Too low Try a bigger number")
     else:
        print("Too high  Try a smeller number")
play_game()
