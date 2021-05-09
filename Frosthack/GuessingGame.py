import random
def game():
    print("You have to guess within 5 for level 1 and 10 for level 2 and 50 for level 3 and 100 for level 4")
    a=int(input("Enter which level you want to play(1-4)"))#which level you want to play
    totchanceperlvl=[3,4,6,7]#3 chances for level 1 and similarly till level 4
    maxguess=[5,10,50,100]#maxlimit of guesses for each level
    b=0
    if a==1:
        b=random.randint(1,5)#random number generated for us to guess
    if a==2:
        b=random.randint(1,10)#random number generated for us to guess
    if a==3:
        b=random.randint(1,50)#random number generated for us to guess
    if a==4:
        b=random.randint(1,100)#random number generated for us to guess
    totchance=totchanceperlvl[a-1]#total chances available to guess
    chances=flag=0#flag determines your win or lose,chances calculates your chances taken
    score=0
    while chances<totchance:
        c=int(input("Enter your guess:"))
        if c<0 or c>maxguess[a-1]:
            print("Please Enter the number within the range")
        elif c<b:
            print("The guessed number is less than the correct answer.Try guessing a higher number")
            chances+=1
            print("You have only ",totchance-chances," left.")
        elif c>b:
            print("The guessed number is greater than the correct answer.Try guesssing a lower number")
            chances+=1
            print("You have only ",totchance-chances," left.")
        else:
            print("Hurray! You got it right")
            flag=1
            chances+=1
            score=(totchance-chances)
            break
    if flag==0:
        print("only ",totchance," chances are allowed.better luck next time!!")
        print("The actual number was ",b)
    else:
        print("You guessed it right!!")
        print("Your score is :",score)
    
    print("Do want to play Again?(y/n)")
    re = input()
    if re == "y":  
        game()
        
        
if __name__ == "__main__":
    game()