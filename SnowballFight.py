''' 
    Name: Snowball-Mania
    Author: Oliver Rutberg
    Date: 12.3.24
    Class: AP Computer Science Principles
    Python: SNAKES?! Where?!?! (3.11.5)
'''
import random
from colorama import Fore
import time
def main():
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name?  ")
    opponent = input("Great to have you here, " + name + "! Who do you want to play against? ")
    print (name + " vs. " + opponent)

    score = []
    score.append(0)
    score.append(0)
    players = []
    players.append (name)
    players.append(opponent)
    print(score,players)

    nextPlayer = ""

    while (nextPlayer!= "DONE"):
        nextPlayer = input("Are there any more opponents? If so, type them on at a time (or DONE) and press 'Enter'. ")
        players.append(nextPlayer)
        score.append(0)
    players.remove("DONE")
    score = score[:-1] #removes last item in the list
    print(score,players)

    choice = input("Do you want to choose who you throw the snowball at, or do you want it to be random? (Type yes or no) ")

    gameplay(name, players, choice, score)

     
    # randomly choose one person to thrown a snowball at the other
    
    

def gameplay(name, players, manual, score):
    while(len(players) > 1):
        thrower = random.choice(players)
        if(thrower==name):
            if(manual == "yes"): #manual mode
                target = input("You are up! Who do you want to throw your snowball at? \n")
            else:                #auto mode
                #print(thrower)
                target = random.choice (players)
                while (target == thrower):
                    target = random.choice (players)
                # print(target)
        else:           #thrower is not us, so pick someone randomly
                #print(thrower)                
                target = random.choice (players)
                while (target == thrower):
                    target = random.choice (players)
                # print(target)
        print(thrower + " is throwing a snowball at " + target + "!\n")
        #generate a random number to use as the hitNum
        hitNum = random.randint(1,5)
        success = hitResult(hitNum)
        if (success == True):
            print("It's a hit! " + target+ " is down!")
            i= players.index(thrower)
            score [i] = score [i] + 1 
            r = players.index(target)
            players.remove(target)
            del score [r]
            print (players,score)
        else: 
            print(Fore.GREEN + thrower + Fore.RESET+ Fore.RED + " , you suck." + Fore.RESET)

        time.sleep (2)

    print(Fore.YELLOW + players[0] + Fore.RESET + " Congratulations! Your final score was \n" + Fore.RED + str(score) + Fore.RESET )




def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum == 3):
        return True
    return False
main()
