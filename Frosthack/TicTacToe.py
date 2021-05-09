game_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

move_space = []

for key in game_board:
    move_space.append(key)



def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():
    
    player1=input("Enter the first player's name")
    player2=input("Enter the second player's name")

    turn = 'O'
    count = 0


    for i in range(10):
        if(turn=='O'):
            player=player1
        else:
            player=player2
        printBoard(game_board)
        print("It's your turn," + player + " which place do you want ?")

        move = input()        

        if game_board[move] == ' ':
            game_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nTry again")
            continue
         
        if count > 4:
            if game_board['7'] == game_board['8'] == game_board['9'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")                
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ': 
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break 
            elif game_board['7'] == game_board['5'] == game_board['3'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] != ' ':
                printBoard(game_board)
                print("\nGame Over.\n")                
                print(" **** " +player + " won. ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            

        if turn =='O':
            turn = 'X'
        else:
            turn = 'O'        
    
    print("Do want to play Again?(y/n)")
    re = input()
    if re == "y":  
        for key in move_space:
            game_board[key] = " "
        game()


if __name__ == "__main__":
    game()