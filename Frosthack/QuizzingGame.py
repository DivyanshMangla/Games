import random


def Level1():
    l=[]
    correct=0
    while(len(l)<5):
        r=random.randint(1, 10)
        if(r in l):
            continue
        else:
            l.append(r)
            if(r==1):
                print("Which player is the oldest to win an Purple Cap")
                print("code: a -Imran Tahir")
                print("code: b -Lasith Malinga")
                print("code: c -Ashish Nehra")
                print("code: d -Ravichandran Ashwin")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        correct+=1
                        print("Yes, It is the correct answer")
                        print("The South African leg-spinner, aged 40, claimed 26 wickets in the 2019 season.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Imran Tahir")
                        print("The South African leg-spinner, aged 40, claimed 26 wickets in the 2019 season.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Imran Tahir")
                        print("The South African leg-spinner, aged 40, claimed 26 wickets in the 2019 season.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Imran Tahir")
                        print("The South African leg-spinner, aged 40, claimed 26 wickets in the 2019 season.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==2):
                print("Which player has the highest number of Orange Caps")
                print("code: a -Chris Gayle")
                print("code: b -Sachin Tendulkar")
                print("code: c -David Warner")
                print("code: d -Mahendra Singh Dhoni")
                answer=input()
                while(True):
                    if(answer=="a"):
                        print("No, The correct answer is David Warner")
                        print("He has won the orange cap in 2015, 2017 and 2019")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is David Warner")
                        print("He has won the orange cap in 2015, 2017 and 2019")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("Yes, The correct answer is David Warner")
                        print("He has won the orange cap in 2015, 2017 and 2019")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is David Warner")
                        print("He has won the orange cap in 2015, 2017 and 2019")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==3):
                print("Who scored first 100 in IPL final?")
                print("code: a -Wriddhiman Saha")
                print("code: b -Shane Watson")
                print("code: c -Brendon Mccullum")
                print("code: d -Micheal Hussey")
                answer=input()
                while(True):
                    if(answer=="a"):
                        correct+=1
                        print("Yes, The correct answer is Wriddhiman Saha")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Wriddhiman Saha")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Wriddhiman Saha")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Wriddhiman Saha")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==4):
                print("Which team has never made the finals???")
                print("code: a - Kolkata Knight Riders")
                print("code: b - Royal Challengers Bangalore")
                print("code: c - Kings XI Punjab")
                print("code: d - Delhi Capitals")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Delhi Capitals")
                        print("Delhi Capitals has never managed to reach an IPL final in 12 seasons")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Delhi Capitals")
                        print("Delhi Capitals has never managed to reach an IPL final in 12 seasons")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Delhi Capitals")
                        print("Delhi Capitals has never managed to reach an IPL final in 12 seasons")
                        break
                    elif(answer=="d"):
                        correct+=1
                        print("Yes, The correct answer is Delhi Capitals")
                        print("Delhi Capitals has never managed to reach an IPL final in 12 seasons")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==5):
                print("Who has the highest all-time batting average??")
                print("code: a -Chris Gayle")
                print("code: b -Mahendra Singh Dhoni")
                print("code: c -Kannur Lokesh Rahul")
                print("code: d -Ravindra Jadeja")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Kannur Lokesh Rahul")
                        print("He had a batting average of 44.86 in 81 matches")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Kannur Lokesh Rahul")
                        print("He had a batting average of 44.86 in 81 matches")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("Yes, The correct answer is Kannur Lokesh Rahul")
                        print("He had a batting average of 44.86 in 81 matches")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Kannur Lokesh Rahul")
                        print("He had a batting average of 44.86 in 81 matches")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==6):
                print("Which player has most centuries in IPL")
                print("code: a -Virat Kohli")
                print("code: b -Chris Gayle")
                print("code: c -David Warner")
                print("code: d -Aaron Finch")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Chris Gayle")
                        print("He has 6-7 centuries so far")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is Chris Gayle")
                        print("He has 6-7 centuries so far")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Chris Gayle")
                        print("He has 6-7 centuries so far")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Chris Gayle")
                        print("He has 6-7 centuries so far")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==7):
                print("What is the highest individual score in IPL so far??")
                print("code: a -170*")
                print("code: b -175*")
                print("code: c -169")
                print("code: d -158*")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is 175*")
                        print("It was scored by Chris Gayle")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is 175*")
                        print("It was scored by Chris Gayle")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is 175*")
                        print("It was scored by Chris Gayle")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is 175*")
                        print("It was scored by Chris Gayle")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==8):
                print("Which cricketer scored 4 hundreds in 2016 IPL")
                print("code: a -Jacques Kallis")
                print("code: b -Suresh Raina")
                print("code: c -Virat Kohli")
                print("code: d -Yuvraj Singh")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Virat Kohli")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Virat Kohli")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("No, The correct answer is Virat Kohli")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Virat Kohli")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==9):
                print("How many overseas captain have won the IPL??")
                print("code: a -  4")
                print("code: b -  3")
                print("code: c -  0")
                print("code: d -  1")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is 3")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is 3")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is 3")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is 3")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==10):
                print("Who has made the fastest fifty in IPL??")
                print("code: a -Kannur Lokesh Rahul")
                print("code: b -Nicholas Pooran")
                print("code: c -Chris Gayle")
                print("code: d -Yuvraj SIngh")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        correct+=1
                        print("Yes, The correct answer is Kannur Lokesh Rahul")
                        print("He made the 50 in just 14 balls")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Kannur Lokesh Rahul")
                        print("He made the 50 in just 14 balls")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Kannur Lokesh Rahul")
                        print("He made the 50 in just 14 balls")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Kannur Lokesh Rahul")
                        print("He made the 50 in just 14 balls")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
    return correct

def Level2():
    l=[]
    correct=0
    while(len(l)<4):
        r=random.randint(1, 10)
        if(r in l):
            continue
        else:
            l.append(r)
            if(r==1):
                print("Who was the first overseas player to captain Delhi Daredevils?")
                print("code: a -James Hopes")
                print("code: b -Mahela Jayawardene")
                print("code: c -Kevin Pietersen")
                print("code: d -Michael Clarke")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        correct+=1
                        print("Yes, The correct answer is James Hopes")
                        print("James Hopes was handed the captaincy after Virender Sehwag was ruled out with a shoulder injury.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is James Hopes")
                        print("James Hopes was handed the captaincy after Virender Sehwag was ruled out with a shoulder injury.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is James Hopes")
                        print("James Hopes was handed the captaincy after Virender Sehwag was ruled out with a shoulder injury.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is James Hopes")
                        print("James Hopes was handed the captaincy after Virender Sehwag was ruled out with a shoulder injury.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==2):
                print("Who is the only bowler to have picked up a five-wicket haul twice against the same team in the same season of the IPL?")
                print("code: a -Sohail Tanvir")
                print("code: b -James Faulkner")
                print("code: c -Lasith Malinga")
                print("code: d -Cheteshwar Pujara")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is James Faulkner")
                        print("Faulkner (Rajasthan Royals) bagged fifers twice against Sunrisers Hyderabad in IPL 2013.")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is James Faulkner")
                        print("Faulkner (Rajasthan Royals) bagged fifers twice against Sunrisers Hyderabad in IPL 2013.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is James Faulkner")
                        print("Faulkner (Rajasthan Royals) bagged fifers twice against Sunrisers Hyderabad in IPL 2013.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is James Faulkner")
                        print("Faulkner (Rajasthan Royals) bagged fifers twice against Sunrisers Hyderabad in IPL 2013.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==3):
                print("Which pacer has bowled the highest number of dot balls in the IPL?")
                print("code: a -Ravichandran Ashwin")
                print("code: b -Umesh Yadav")
                print("code: c -Lasith Malinga")
                print("code: d -Bhuvneshwar Kumar")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Bhuvneshwar Kumar")
                        print("Bhuvneshwar has bowled a total of 1,164 dots.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Bhuvneshwar Kumar")
                        print("Bhuvneshwar has bowled a total of 1,164 dots.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Bhuvneshwar Kumar")
                        print("Bhuvneshwar has bowled a total of 1,164 dots.")
                        break
                    elif(answer=="d"):
                        correct+=1
                        print("Yes, The correct answer is Bhuvneshwar Kumar")
                        print("Bhuvneshwar has bowled a total of 1,164 dots.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==4):
                print("How many English bowlers have taken a five-wicket haul in the IPL?")
                print("code: a -3")
                print("code: b -4")
                print("code: c -1")
                print("code: d -2")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is 1")
                        print("Dimitri Mascarenhas claimed a five-wicket haul for Kings XI Punjab against Pune Warriors India in 2012.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is 1")
                        print("Dimitri Mascarenhas claimed a five-wicket haul for Kings XI Punjab against Pune Warriors India in 2012.")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("Yes, The correct answer is 1")
                        print("Dimitri Mascarenhas claimed a five-wicket haul for Kings XI Punjab against Pune Warriors India in 2012.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is 1")
                        print("Dimitri Mascarenhas claimed a five-wicket haul for Kings XI Punjab against Pune Warriors India in 2012.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==5):
                print("Which venue hosted the IPL 2014 final?")
                print("code: a -Sheikh Zayed Stadium, Abu Dhabi")
                print("code: b -Wankhede Stadium, Mumbai")
                print("code: c -M. Chinnaswamy Stadium, Bengaluru")
                print("code: d -Wankhede Stadium")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is M. Chinnaswamy Stadium, Bengaluru")
                        print("The final which was played between the Kolkata Knight Riders and Kings XI Punjab saw the Knights inflict a three-wicket defeat on Punjab.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is M. Chinnaswamy Stadium, Bengaluru")
                        print("The final which was played between the Kolkata Knight Riders and Kings XI Punjab saw the Knights inflict a three-wicket defeat on Punjab.")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("Yes, The correct answer is M. Chinnaswamy Stadium, Bengaluru")
                        print("The final which was played between the Kolkata Knight Riders and Kings XI Punjab saw the Knights inflict a three-wicket defeat on Punjab.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is M. Chinnaswamy Stadium, Bengaluru")
                        print("The final which was played between the Kolkata Knight Riders and Kings XI Punjab saw the Knights inflict a three-wicket defeat on Punjab.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==6):
                print("Which team has played in the most IPL finals after Chennai Super Kings?")
                print("code: a -Mumbai Indians")
                print("code: b -Royal Challengers Bangalore")
                print("code: c Kolkata Knight Riders-")
                print("code: d -Sunrisers Hyderabad")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        correct+=1
                        print("Yes, The correct answer is Mumbai Indians")
                        print("Mumbai Indians made it to the finals in six editions of the IPL: 2010, 2013, 2015, 2017, 2019 and 2020.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Mumbai Indians")
                        print("Mumbai Indians made it to the finals in six editions of the IPL: 2010, 2013, 2015, 2017, 2019 and 2020.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Mumbai Indians")
                        print("Mumbai Indians made it to the finals in six editions of the IPL: 2010, 2013, 2015, 2017, 2019 and 2020.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Mumbai Indians")
                        print("Mumbai Indians made it to the finals in six editions of the IPL: 2010, 2013, 2015, 2017, 2019 and 2020.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==7):
                print("Against which team were the most centuries scored in IPL 2018?")
                print("code: a -Mumbai Indians")
                print("code: b -Rajasthan Royals")
                print("code: c -Sunrisers Hyderabad")
                print("code: d -Kings XI Punjab")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Sunrisers Hyderabad")
                        print("Four centuries were scored against Sunrisers Hyderabad in IPL 2018.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Sunrisers Hyderabad")
                        print("Four centuries were scored against Sunrisers Hyderabad in IPL 2018.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Sunrisers Hyderabad")
                        print("Four centuries were scored against Sunrisers Hyderabad in IPL 2018.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Sunrisers Hyderabad")
                        print("Four centuries were scored against Sunrisers Hyderabad in IPL 2018.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==8):
                print("Who has bowled the most number of maiden overs in the IPL?")
                print("code: a -Praveen Kumar")
                print("code: b -Lasith Malinga")
                print("code: c -Irfan Pathan")
                print("code: d -Jasprit Bumrah")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Kumar has bowled 14 maiden overs.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Kumar has bowled 14 maiden overs.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Kumar has bowled 14 maiden overs.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Kumar has bowled 14 maiden overs.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            
    return correct

def Level3():
    l=[]
    correct=0
    while(len(l)<3):
        r=random.randint(1, 5)
        if(r in l):
            continue
        else:
            l.append(r)
            if(r==1):
                print("Which Ipl franchise yuvraj didn't play for?")
                print("code: a -Royal Challengers Bangalore")
                print("code: b -Kolkata Knight Riders")
                print("code: c -Kings XI Punjab")
                print("code: d -Mumbai Indians")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Kolkata Knight Riders")
                        print("Yuvraj Singh did not play for KKR.")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is Kolkata Knight Riders")
                        print("Yuvraj Singh did not play for KKR.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Kolkata Knight Riders")
                        print("Yuvraj Singh did not play for KKR.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Kolkata Knight Riders")
                        print("Yuvraj Singh did not play for KKR.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==2):
                print("Who bowled the first ball in IPL history?")
                print("code: a -Sohail Tanvir")
                print("code: b -Zaheer Khan")
                print("code: c -Lakshmipathy Balaji")
                print("code: d -Praveen Kumar")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Praveen Kumar bowled the first ball.")

                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Praveen Kumar bowled the first ball.")

                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Praveen Kumar")
                        print("Praveen Kumar bowled the first ball.")

                        break
                    elif(answer=="d"):
                        correct+=1
                        print("Yes, The correct answer is Praveen Kumar")
                        print("Praveen Kumar bowled the first ball.")

                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==3):
                print("When did rohit sharma get his first title?")
                print(" code: a- 2014")
                print(" code: b- 2017")
                print(" code: c- 2009")
                print(" code: d- 2015")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is 2009")
                        print("Hitman won with Deccan Chargers in 2009.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is 2009")
                        print("Hitman won with Deccan Chargers in 2009.")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("Yes, The correct answer is 2009")
                        print("Hitman won with Deccan Chargers in 2009.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is 2009")
                        print("Hitman won with Deccan Chargers in 2009.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==4):
                print("How many teams had their captain as a bowler in 2019?")
                print(" code: a- 1")
                print(" code: b- 2")
                print(" code: c- 3")
                print(" code: d- 0")
                answer=input()
                while(True):
                    if(answer=="a"):
                        correct+=1
                        print("Yes, The correct answer is 1")
                        print("R Ashwin captained KX1P.")
                    elif(answer=="b"):
                        print("No, The correct answer is 1")
                        print("R Ashwin captained KX1P.")
                    elif(answer=="c"):
                        print("No, The correct answer is 1")
                        print("R Ashwin captained KX1P.")
                    elif(answer=="d"):
                        print("No, The correct answer is 1")
                        print("R Ashwin captained KX1P.")
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==5):
                print("How many times did CSK enter the finals?")
                print(" code: a- 4")
                print(" code: b- 6")
                print(" code: c- 8")
                print(" code: d- 7")
                answer=input()
                while(True):
                    if(answer=="a"):
                        print("No, The correct answer is 7")
                        print("CSK entered finals 7 times.")
                    elif(answer=="b"):
                        print("No, The correct answer is 7")
                        print("CSK entered finals 7 times.")
                    elif(answer=="c"):
                        print("No, The correct answer is 7")
                        print("CSK entered finals 7 times.")
                    elif(answer=="d"):
                        correct+=1
                        print("Yes, The correct answer is 7")
                        print("CSK entered finals 7 times.")
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            
    return correct

def Level4():
    l=[]
    correct=0
    while(len(l)<2):
        r=random.randint(1, 4)
        if(r in l):
            continue
        else:
            l.append(r)
            if(r==1):
                print("Which player got more than 30 wickets in a single season?")
                print(" code: a- Bhuvneshwar Kumar")
                print(" code: b- D J Bravo")
                print(" code: c- Lasith Malinga")
                print(" code: d- Imran Tahir")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is D J Bravo")
                        print("He took 32 wickets in 2013.")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is D J Bravo")
                        print("He took 32 wickets in 2013.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is D J Bravo")
                        print("He took 32 wickets in 2013.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is D J Bravo")
                        print("He took 32 wickets in 2013.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==2):
                print("How many times did CSK win the Fair Play Award?")
                print(" code: a- 3")
                print(" code: b- 4")
                print(" code: c- 5")
                print(" code: d- 6")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is 6")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is 6")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is 6")
                        break
                    elif(answer=="d"):
                        correct+=1
                        print("Yes, The correct answer is 6")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==3):
                print("Which player hit the longest 6 in IPL history?")
                print(" code: a- Albie Morkel")
                print(" code: b- Chris Gayle")
                print(" code: c- Robin Uttappa")
                print(" code: d- Kieron Pollard")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        correct+=1
                        print("Yes, The correct answer is Albie Morkel")
                        print("He hit the longest 6(125m)")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Albie Morkel")
                        print("He hit the longest 6(125m)")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Albie Morkel")
                        print("He hit the longest 6(125m)")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Albie Morkel")
                        print("He hit the longest 6(125m)")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==4):
                print("Which player has more Half centuries?")
                print(" code: a- David Warner")
                print(" code: b- Virat Kohli")
                print(" code: c- Rohit Sharma")
                print(" code: d- Kane Williamson")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is David Warner")
                        print("David Warner has 54 Half centuries and is the highest.")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is David Warner")
                        print("David Warner has 54 Half centuries and is the highest.")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is David Warner")
                        print("David Warner has 54 Half centuries and is the highest.")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is David Warner")
                        print("David Warner has 54 Half centuries and is the highest.")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
    return correct

def Level5():
    l=[]
    correct=0
    while(len(l)<2):
        r=random.randint(1, 3)
        if(r in l):
            continue
        else:
            l.append(r)
            if(r==1):
                print("In the arc outta the park- refers whom?")
                print(" code: a- Sam Curran")
                print(" code: b- Kieron Pollard")
                print(" code: c- David Miller")
                print(" code: d- Hardik Pandya")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is David Miller")
                        print("Known for his comeback against RCB")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is David Miller")
                        print("Known for his comeback against RCB")
                        break
                    elif(answer=="c"):
                        correct+=1
                        print("Yes, The correct answer is David Miller")
                        print("Known for his comeback against RCB")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is David Miller")
                        print("Known for his comeback against RCB")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==2):
                print("Who captained Kochi Tuskers Kerala?")
                print(" code: a- Ravindra Jadeja")
                print(" code: b- Brendon Mccullum")
                print(" code: c- Brad Hogg")
                print(" code: d- Mahela Jayawardene")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Mahela Jayawardene")
                        print("He captained the Kochi Tuskers")
                        break
                    elif(answer=="b"):
                        print("No, The correct answer is Mahela Jayawardene")
                        print("He captained the Kochi Tuskers")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Mahela Jayawardene")
                        print("He captained the Kochi Tuskers")
                        break
                    elif(answer=="d"):
                        correct+=1
                        print("Yes, The correct answer is Mahela Jayawardene")
                        print("He captained the Kochi Tuskers")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            elif(r==3):
                print("Who has most Hat-tricks in IPL?")
                print(" code: a- Ravindra Jadeja")
                print(" code: b- Amit Mishra")
                print(" code: c- Ravichandran Ashwin")
                print(" code: d- Yuvraj Singh")
                while(True):
                    answer=input()
                    if(answer=="a"):
                        print("No, The correct answer is Amit Mishra")
                        print("Amit Mishra has 3 hat-tricks")
                        break
                    elif(answer=="b"):
                        correct+=1
                        print("Yes, The correct answer is Amit Mishra")
                        print("Amit Mishra has 3 hat-tricks")
                        break
                    elif(answer=="c"):
                        print("No, The correct answer is Amit Mishra")
                        print("Amit Mishra has 3 hat-tricks")
                        break
                    elif(answer=="d"):
                        print("No, The correct answer is Amit Mishra")
                        print("Amit Mishra has 3 hat-tricks")
                        break
                    else:
                        print("Wrong code for the answer")
                        print("Please try again")
            
    return correct

def game() :
    print("Level 1")
    print("This will contain 5 random questions which will test your knowledge about IPL")
    print("You have to answer all the questionsto go to the next level ")
    c1=Level1()
    if(c1==5):
        c2=Level2()
        print("Level 2")
        print("This will contain 4 random questions which will test your knowledge about IPL")
        print("You have to answer all the questionsto go to the next level ")
        if(c2==4):
            print("Level 3")
            print("This will contain 3 random questions which will test your knowledge about IPL")
            print("You have to answer all the questionsto go to the next level ")
            c3=Level3
            if(c3==3):
                print("Level 4")
                print("This will contain 2 random questions which will test your knowledge about IPL")
                print("You have to answer all the questionsto go to the next level ")
                c4=Level4
                if(c4==2):
                    print("Level 5")
                    print("This will be our hardest level")
                    print("If you answer this correctly, then you can become our new CHAMPION")
                    print("You have to answer all the questionsto go to the next level ")
                    c5=Level5()
                    if(c5==2):
                        print("Congratulations!!!!!!")
                        print("You are the new CHAMPION")
                    else:
                        print("Awww!!!! So close yet so far")
                else:
                    print("The level you reached is also an acievement")
                    print("Just a little more push and you can become our CHAMPION")
            else:
                print("Just use the time you have to learn more about IPL")
        else:
            print("You can do better than this")
    else:
        print("Better Luck Next Time")
        
    print("Do want to play Again?(y/n)")
    re = input()
    if re == "y":  
        game()
  
if __name__ == "__main__":
    game()          
                
