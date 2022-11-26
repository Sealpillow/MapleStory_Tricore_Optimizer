import sys
import os
from time import sleep

from classSkillList import classes


def found(setList, countList):
    count = 0
    goal = len(countList)
    # count number of skill in the setList
    for i in range(len(setList)):  # number of core in the list
        for j in range(3):  # each core 3 skills
            countList[setList[i][j]] += 1
    # check if all the skills are 2 which is optimal
    for item in countList:
        if countList[item] == 2:
            count += 1
    printprogress(count, goal, skillList)
    clearCount(countList)
    if count == goal:
        return True
    else:
        return False


def isSafe(setList, countList):

    num = len(setList)
    # the first skill must not have repeat in the setlist
    for a in range(num):
        for b in range(a+1, num):
            if setList[a][0] == setList[b][0]:  # if repeat -> False
                return False

    # count number of skill in the setList
    for i in range(num):  # number of core in the list
        for j in range(3):  # each core 3 skills
            countList[setList[i][j]] += 1

    # check if all the skills' count exceed optimal count -> countList[item] > 2 -> False
    for item in countList:
        if countList[item] > 2:
            clearCount(countList)
            return False
    clearCount(countList)
    return True

def printprogress(current,total,skillList):
    os.system('cls')
    print("Total number of unique skills: " + str(len(skillList)))
    if len(skillList) > 0:
        print(*skillList, sep=', ')
    percent = 100 * (current / float(total))
    print("Skill Found: |" + "█" * int(percent/2) + " " * int((100 - percent)/2) + "|", end="")  # '█' - hold alt and press 219 on numpad: /2 is used to reduce size
    print(str(current) + "/" + str(total))
    sleep(0.1)

def clearCount(countList):  # everytime after checking num of skill in coreList, it is called to reset to 0
    for key in countList:  # key set all key value to 0
        countList[key] = 0


def perfectcombi(nodeList, setList, countList, numCore, numNode):
    if found(setList, countList) and numCore == 4:  # assume user will use 4 core slots 6 unique skills
        print("Perfect Tri-core:")
        for i in range(len(setList)):
            print("Core " + str(i+1) + ": ", end="")
            for j in range(3):
                print(setList[i][j], end=", ")
            print()
        return True
    for x in range(numNode):   # cycle through every node in nodelist
        if isSafe(setList, countList):
            setList.append(nodeList[x])  # append node into setList
            if perfectcombi(nodeList, setList, countList, numCore+1, numNode):
                return True
            del setList[-1]  # remove node from setList
    return False


nodeList = []  # contain all the node skill inputs
skillList = []  # contain unique skills from node
setList = []  # 2d matrix contain perfect tricore combination
countList = {}  # to count num of skill in the setList -> define key to value in dictionary
finalList = []
userclass = ""
inplay = True

while inplay:
    print("Welcome to TriCore Optimizer")
    while userclass not in classes:
        userclass = input("classes: ").lower()
    print("Key: Skill")
    for key,value in classes[userclass].items():
        print(key + " : " + value)
    keylist = [i for i in classes[userclass].keys()]
    valuelist = [i for i in classes[userclass].values()]
    print("Assuming user will use 4 core slots 6 unique skills")
    print("Type in key based on respective skill")
    print("Sequence matters! After all core inputs type:end")
    print("e.g: " + valuelist[0], valuelist[1], valuelist[2])
    print("Node: " + keylist[0], keylist[1], keylist[2])
    while True:
        try:
            nodeList.append([str(classes[userclass][i]) for i in input("Node: ").lower().split()])
            if nodeList[-1][0] == "end":
                del nodeList[-1]
                break
        except Exception as e:
            print("Error")
    for node in nodeList:  # search through input nodes from user
        for skill in node:  # 3 different skill in node
            if skill not in skillList:  # unique list of skill
                skillList.append(skill)

    print("Total number of unique skills: " + str(len(skillList)))
    if len(skillList) > 0:
        print(*skillList, sep=', ')
    numNode = len(nodeList)  # number of input nodes from user
    numSkill = len(skillList)  # number of unique skills
    numCore = 0  # initialise num core to 0 as start
    for item in skillList:  # to define key to value in dictionary
        countList[item] = 0
    if not perfectcombi(nodeList, setList, countList, numCore, numNode):
        print("No Perfect Tricore found")
    if input("Try Again? y/n:") != "y":
        inplay = False
    else:
        userclass = ""
        os.system('cls')
