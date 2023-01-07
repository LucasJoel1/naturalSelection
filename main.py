import math
import random
import time

x = 400
y = 400
botsNum = 400

genes = [
    "N",
    "E",
    "S",
    "W"
]

map = []
bots = []
botLocations = [[], []]

class agent:
    def __init__(self, x, y, id, genes):
        self.alive = True
        self.x = random.randint(0, x - 1)
        self.y = random.randint(0, y - 1)
        self.id = id
        # if the location is already taken, find a new one
        if [self.x, self.y] in botLocations:
            self.__init__(x, y, genes)
        else:
            botLocations[0].append(self.x)
            botLocations[1].append(self.y)
        self.gene = random.choice(genes)

    def death(self):
        self.alive = False

    def move(self, x, y):
        if(self.gene == "N" and self.y > 0):
            self.y -= 1
        elif(self.gene == "E" and self.x < x - 1):
            self.x += 1
        elif(self.gene == "S" and self.y < y - 1):
            self.y += 1
        elif(self.gene == "W" and self.x > 0):
            self.x -= 1
        else:
            pass

    def resetLocation(self):
        self.x = random.randint(0, x - 1)
        self.y = random.randint(0, y - 1)
        if [self.x, self.y] in botLocations:
            self.resetLocation()
        else:
            botLocations[0][self.id] = self.x
            botLocations[1][self.id] = self.y

for i in range(botsNum):
    bots.append(agent(x, y, i, genes))

# create the map using tkinter

def getGeneAmount(gene):
    number = 0
    for i in range(len(bots)):
        if bots[i].gene == gene:
            number += 1
    return number
generation = 0
percentAliveN = 0
percentAliveE = 0
percentAliveS = 0
percentAliveW = 0
botsAliveN = getGeneAmount("N")
botsAliveE = getGeneAmount("E")
botsAliveS = getGeneAmount("S")
botsAliveW = getGeneAmount("W")
print("Generation: " + str(generation) + " N: " + str(botsAliveN) + " E: " + str(botsAliveE) + " S: " + str(botsAliveS) + " W: " + str(botsAliveW))
botsToRemove = []
while True:
    generation += 1
    percentAliveN = 0
    percentAliveE = 0
    percentAliveS = 0
    percentAliveW = 0
    botsAliveN = 0
    botsAliveE = 0
    botsAliveS = 0
    botsAliveW = 0
    botsToRemove = []
    for i in range(0, 24):
        print(i)
        for i in range(len(bots)):
            bots[i].move(x, y)
            botLocations[0][i] = bots[i].x
            botLocations[1][i] = bots[i].y
    for i in range(len(bots)):
        if bots[i].y < 1:
            bots[i].death()
    for i in range(len(bots)-1):
        try:
            if bots[i].alive:
                botsToRemove.append(i)
        except:
            print(IndexError)
    botsToRemove.reverse()
    for i in range(len(botsToRemove)):
        bots.pop(botsToRemove[i])
    percentAliveN = getGeneAmount("N") / len(bots)
    percentAliveE = getGeneAmount("E") / len(bots)
    percentAliveS = getGeneAmount("S") / len(bots)
    percentAliveW = getGeneAmount("W") / len(bots)
    # get the bots alive in each gene by number by using the percentage
    botsAliveN = math.floor(botsNum * percentAliveN)
    botsAliveE = math.floor(botsNum * percentAliveE)
    botsAliveS = math.floor(botsNum * percentAliveS)
    botsAliveW = math.floor(botsNum * percentAliveW)
    # reset the bots
    bots = []
    for i in range(botsAliveN):
        bots.append(agent(x, y, i, "N"))
    for i in range(botsAliveE):
        bots.append(agent(x, y, i, "E"))
    for i in range(botsAliveS):
        bots.append(agent(x, y, i, "S"))
    for i in range(botsAliveW):
        bots.append(agent(x, y, i, "W"))
    for i in range(len(bots)):
        bots[i].resetLocation()
    print("Generation: " + str(generation) + " N: " + str(botsAliveN) + " E: " + str(botsAliveE) + " S: " + str(botsAliveS) + " W: " + str(botsAliveW))