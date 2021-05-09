while(True):
    print("Welcome to the Main Menu")
    print("Please type the code of the game that you want to play")
    print("Tic Tac Toe:       code = 1")
    print("Guessing Game:     code = 2")
    print("IPL Quiz:          code = 3")
    print("To Exit the Game   code = 4")
    n=int(input())
    if(n==1):
        print("Welcome to Tic Tac Toe")
        import TicTacToe
        exec(open('TicTacToe.py').read())
        continue
    elif(n==2):
        print("Welcome to the guessing game")
        import GuessingGame
        exec(open('GuessingGame.py').read())
        continue
    elif(n==3):
        print("Welcome to IPL Quiz")
        import QuizzingGame
        exec(open('QuizzingGame.py').read())
        continue
    elif(n==4):
        print("Do you want to exit the Game?? (y/n)")
        n1=input()
        if(n1=="y"):
            print("Thank You for playing the small Games")
            print("We Hope You get well Soon")
            break
        else:
            continue
    else:
        print("Wrong code!!!!!")
        print("Please Try Again")
        




