from math import *
from classSkillList import classes

jobName=[i for i in classes.keys()]
jobtitle=[i.title() for i in jobName]
skill = []

for name in jobName:
    skill.append([str(j) for j in classes[name].values()])

for i in range(len(skill)):
    print(jobtitle[i], end =', ')  # print job name

for i in range(len(skill)):
    n = 0
    print(jobtitle[i]) # print job name
    for x in range(floor(len(skill[i])/3)):  # multiple of 3 printing
        for y in range(3):
            print(skill[i][n],end=", ")
            n+=1
        print()
    for x in range(len(skill[i])%3):  # remainder of 3 printing
        if skill[i][n] != "end":
            print(skill[i][n], end=", ")
    print()
input("To end input any key: ") 