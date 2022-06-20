import sys
import os
from jobSkillList import job
nodeList = []  # contain all the node skill inputs
skillList = []  # contain unique skills from node
setList =[]  # 2d matrix contain perfect tricore combination
countList = {}  # to count num of skill in the setList
finalList = []
userjob=""
inplay = True


def found(setList, countList):
    count = 0
    goal=len(countList)
    # count number of skill in the setList
    for i in range(len(setList)):  # number of core in the list
        for j in range(3):  # each core 3 skills
            countList[setList[i][j]]+=1
    # check if all of the skills are 2 which is optitmal
    for item in countList:
        if countList[item] == 2:
            count+=1
    if count == goal:
        return True
    else:
        return False


def isSafe(setList, countList):
    # the first skill must not have repeat in the setlist
    num = len(setList)
    for a in range(num):
        for b in range(a+1,num):
            if setList[a][0]==setList[b][0]:
                return False
    # count number of skill in the setList
    for i in range(num):  # number of core in the list
        for j in range(3):  # each core 3 skills
            countList[setList[i][j]] += 1
    # check if all of the skills are 2 which is optitmal
    for item in countList:
        if countList[item]> 2:
            clearCount(countList)
            return False
    clearCount(countList)
    return True


def clearCount(countList):
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
    for x in range(numNode):   #cycle through every node in nodelist
        if isSafe(setList, countList):
            # print(setList)
            setList.append(nodeList[x])  # append node into setList
            if perfectcombi(nodeList, setList, countList, numCore+1,numNode):
                return True
            del setList[-1]  # remove node from setList
    return False


while inplay:
    print("Welcome to TriCore Simulator")
    while userjob not in job:
        userjob = input("Job: ").lower()
    print("Key: Skill")
    for key,value in job[userjob].items():
        print(key + " : " + value)
    keylist = [i for i in job[userjob].keys()]
    valuelist = [i for i in job[userjob].values()]
    print("Assuming user will use 4 core slots 6 unique skills")
    print("Type in key based on respective skill")
    print("Sequence matters! After all core inputs type:end")
    print("e.g: " + valuelist[0], valuelist[1], valuelist[2])
    print("Node: " + keylist[0], keylist[1], keylist[2])
    while True:
        try:
            nodeList.append([str(job[userjob][i]) for i in input("Node: ").lower().split()])
            if nodeList[-1][0] == "end":
                del nodeList[-1]
                break
        except Exception as e:
            print("Error")
    for node in nodeList:
        for skill in node:
            if skill not in skillList:  # unique list of skill
                skillList.append(skill)

    print("Total number of unique skills: " + str(len(skillList)))
    if len(skillList)>0:
        print(*skillList, sep=', ')
    numNode = len(nodeList)
    numSkill = len(skillList)
    numCore = 0
    for item in skillList:  # to define key to value in dictionary
        countList[item] = 0
    if not perfectcombi(nodeList, setList, countList, numCore, numNode):
        print("No Perfect Tricore found")
    if input("Try Again? y/n:") != "y":
        inplay = False
    else:
        userjob = ""
        os.system('cls')