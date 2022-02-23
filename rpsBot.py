from __future__ import division
from math import sqrt
import random

#Ties will be counted as loss for this specific algorithm implementation

def predict():
    return random.choice(['R','P','S'])

def play(inp1,inp2):
    if inp1 == inp2:
        return "D"
    elif inp1 == 'R' and inp2 == 'S' or inp1 == 'P' and inp2 == 'R' or inp1 == 'S' and inp2 == 'P':
        return "W"
    else:
        return "L"
        
results = []

for i in range(0,1000):
    results.append(play(predict(),predict()))


Bwins = results.count("W")        
Bties = results.count("D") 
Blosses = results.count("L")     


##################################################################################### BASELINE ABOVE ########################################################################################
##-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
#####################################################################################  AI BOT BELOW  ########################################################################################

def checkGame(inp1, inp2):
    if (inp1 == '0' and inp2 == '1') or (inp1 == '1' and inp2 == '2') or (inp1 == '2' and inp2 == '0'):
        return -1
    elif inp1 == inp2:
        return 0
    else:
        return 1
# this dict covers all the possible key entries that would come from adding 'previosTwo' with the rock/paper/scissors count where it covers at maximum the last three moves in order to create a pattern and used to create the "result" and "weight" below
# in order to accurately identify various patterns
rpsTotalCount = { '000' : 3, '001' : 3, '002' : 3, '010' : 3, '011' : 3, '012' : 3, '020' : 3, '021' : 3, '022' : 3, '100' : 3, '101' : 3, '102' : 3, '110' : 3, '111' : 3, '112' : 3, '120' : 3, '121' : 3, '122' : 3, '200' : 3, '201' : 3, '202' : 3, '210' : 3, '211' : 3, '212' : 3, '220' : 3, '221' : 3, '222' : 3 }

RPS  = {'0' : 'rock', '1' : 'paper', '2' : 'scissor'}


wins, ties, losses = 0,0,0 # initialize the first start of each win/tie/loss
previosTwo = '00' #initialize the prev two to be updated

#Loops until person wants to stop playing
while(1):
    roll = input('Please type rock,paper,scissors, or quit \n')
    
    while(roll not in ['rock', 'paper', 'scissors', 'quit']):
        roll = input("You must play a valid input!!! \n")

    if roll == 'rock':
        rpsBot = '0'
    elif roll == 'paper':
        rpsBot = '1'
    elif roll == 'scissors':
        rpsBot = '2'
    elif roll == 'quit':
        quit()

    if(previosTwo[0] == '3'):
        y = str( random.randint(0,2) )
    else:
        rockCount = rpsTotalCount[previosTwo + '0']
        paperCount = rpsTotalCount[previosTwo + '1']
        scissorsCount = rpsTotalCount[previosTwo + '2']

        rpsTotal = rockCount + paperCount + scissorsCount

        pDecision = [ rockCount/rpsTotal, paperCount/rpsTotal, 1- (rockCount/rpsTotal) - (paperCount/rpsTotal) ] # list of rock total count over total games, paper/total, and 1 - the two minus each other  ## essentially keeps track of each 
        
        result = [ max(pDecision[2]-pDecision[1],0), max(pDecision[0]-pDecision[2],0), max(pDecision[1]-pDecision[0],0) ] # this is used to decide result
        weight = sqrt(result[0]*result[0] + result[1]*result[1] + result[2]*result[2])  # weight to be used to get the result
        result = [result[0]/weight, result[1]/weight, 1 - result[0]/weight - result[1]/weight] # overall result we will use to compare with the the plays to decide what to play
        

        player = random.uniform(0,1)  # value between 0-1

        # used to decide the next playing for the computer based off the calculated weight
        if player <= result[0]:
            player = '0'
        elif player <= result[0] + result[1]:
            player = '1'
        else:
            player = '2'

        #update dict
        rpsTotalCount[previosTwo+rpsBot] += 1
    #update
    previosTwo = previosTwo[1] + rpsBot

   #updates and keeps track of games won loss and tied
    if checkGame(rpsBot,player) == -1:
        losses += 1
    elif checkGame(rpsBot,player) == 0:
        ties += 1
    elif checkGame(rpsBot,player) == 1:
        wins += 1

    print( 'Wins:', wins, 'Losses:', losses, 'Ties:', ties)
    print( 'The bots score is:', (losses/(wins+losses+ties)) * 100,'%')
    print("The score that he must beat is " + str(round((Bwins)/(Bwins + Blosses) * 100,2)) + "%")
    if ((round(losses/(wins+losses+ties),2)) * 100) < round((Bwins)/(Bwins + Blosses) * 100,2):
        print('You are currently beating the bot! \n------------------------------------------------------------')
    else:
        print('The bot is beating you! Is a computer really reading your brain????\n------------------------------------------------------------')