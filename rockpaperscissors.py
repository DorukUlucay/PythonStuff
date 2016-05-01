from random import randint


playerScore, cpuScore, draw = 0,0,0

def compare(a):
    global playerScore, cpuScore, draw
    
    for i in range(1,100):
        cpu = (randint(0,2))
        
    if(a==cpu):
        print ("draw")
        draw=draw+1
    elif(cpu == 0 and a == 2):
        print ("scissors against rock. cpu wins")
        cpuScore=cpuScore+1
    elif(cpu == 0 and a == 1):
        print ("paper against rock. " + name + " wins")
        playerScore=playerScore+1
    elif(cpu == 1 and a == 0):
        print ("rock against paper. cpu wins")
        cpuScore=cpuScore+1
    elif(cpu == 1 and a == 2):
        print ("scissors against paper." + name + " wins")
        playerScore=playerScore+1
    elif(cpu == 2 and a == 1):
        print ("paper against scissors. cpu wins")
        cpuScore=cpuScore+1
    elif(cpu == 2 and a == 0):
        print ("rock against scissors." + name + " wins")
        playerScore=playerScore+1

def process(a):
    if (a=="r"):
        a=0
    elif(a=="p"):
        a=1
    elif(a=="s"):
        a=2
    compare(a)

def showStat():
    print ("{0}: {1} CPU: {2} Draws:{3}").format(name, str(playerScore), str(cpuScore), str(draw))

name=input("welcome to rock-paper-scissors. what is your name ?")
print("welcome again, " + name + ". you can type q to quit or stat to see the score during the game.")
        
while(True):
    a = str.lower(input("(r)ock, (p)aper or (s)cissors ?"))
    if(a=="q"):
        quit()
    if(a=="stat"):
        showStat()
    if( a=="r" or a=="p" or a=="s"):
        process(a)
