#Import library
import random

#Loop
while True:
    t = "== ROCK,PAPER & SCISSOR GAME ==\n"
    print(t.center(60))

    print("1 - Play game")
    print("2 - Quit\n")

    choice = int(input("Enter choice(1-2): "))   #input method

    if choice == 1:
        options = ['rock','paper','scissor']        #if-else condition
        com_score = 0   #score variables
        user_score = 0
    
        com = random.choice(options)    #random module used
    
        user = input("Enter choice (Rock,Paper & Scissor): ").lower()   #input method with lower case
    
        if user not in options:      #for invalid choice 
            print("Invalid option")
            break
    
        elif user == com:
            print("== CHOICES ==")           #game draw
            print(f"Computer: {com}")
            print(f"Player: {user}\n")
            print("== Result ==")
            print("Draw\n")
    
        elif (
        (user == "rock" and com == "scissors") or     #whwn player win
        (user == "paper" and com == "rock") or
        (user == "scissors" and com == "paper")
        ):
            print("You Win\n")
            user_score =+ 1
        
    
        else:
            print("== CHOICES ==")        #when computer wins
            print(f"Computer:{com}")
            print(f"Player: {user}\n")
            print("== Result ==")
            print("Computer win\n")
            com_score += 1
            
    else:
        print(f"Computer score: {com_score}")    #score display
        print(f"Player score: {user_score}")
        print("Thanks for playing this game!")
        break