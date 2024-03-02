
#Corgi Alarm
big0 = """+---+ |   | |   | +   + |   | |   | +---+ """
big1 = """    +     |     |     +     |     |     + """
big2 = """+---+     |     | +---+ |     |     +---+ """
big3 = """+---+     |     | +---+     |     | +---+ """
big4 = """+   + |   | |   | +---+     |     |     + """
big5 = """+---+ |     |     +---+     |     | +---+ """
big6 = """+---+ |     |     +---+ |   | |   | +---+ """
big7 = """+---+     |     |     +     |     |     + """
big8 = """+---+ |   | |   | +---+ |   | |   | +---+ """
big9 = """+---+ |   | |   | +---+     |     |     + """
bigC = """


o

o


"""

timeList = []
curTime = ""

while True:
    timeInput = input()
    if timeInput == "end":
        break
    else:
        timeList.append(timeInput)
    # print(timeList)
# print(timeList[0])
# print(timeList[-1])
for i in range(0,len(timeList)):
    curTime = timeList[i]
    if curTime[0] == "0":
        num0 = big0
    elif curTime[0] == "1":
        num0 = big1
    elif curTime[0] == "2":
        num0 = big2
    elif curTime[0] == "3":
        num0 = big3
    elif curTime[0] == "4":
        num0 = big4
    elif curTime[0] == "5":
        num0 = big5
    elif curTime[0] == "6":
        num0 = big6
    elif curTime[0] == "7":
        num0 = big7
    elif curTime[0] == "8":
        num0 = big8
    elif curTime[0] == "9":
        num0 = big9

    if curTime[1] == "0":
        num1 = big0
    elif curTime[1] == "1":
        num1 = big1
    elif curTime[1] == "2":
        num1 = big2
    elif curTime[1] == "3":
        num1 = big3
    elif curTime[1] == "4":
        num1 = big4
    elif curTime[1] == "5":
        num1 = big5
    elif curTime[1] == "6":
        num1 = big6
    elif curTime[1] == "7":
        num1 = big7
    elif curTime[1] == "8":
        num1 = big8
    elif curTime[1] == "9":
        num1 = big9

    if curTime[3] == "0":
        num2 = big0
    elif curTime[3] == "1":
        num2 = big1
    elif curTime[3] == "2":
        num2 = big2
    elif curTime[3] == "3":
        num2 = big3
    elif curTime[3] == "4":
        num2 = big4
    elif curTime[3] == "5":
        num2 = big5
    elif curTime[3] == "6":
        num2 = big6
    elif curTime[3] == "7":
        num2 = big7
    elif curTime[3] == "8":
        num2 = big8
    elif curTime[3] == "9":
        num2 = big9

    if curTime[4] == "0":
        num3 = big0
    elif curTime[4] == "1":
        num3 = big1
    elif curTime[4] == "2":
        num3 = big2
    elif curTime[4] == "3":
        num3 = big3
    elif curTime[4] == "4":
        num3 = big4
    elif curTime[4] == "5":
        num3 = big5
    elif curTime[4] == "6":
        num3 = big6
    elif curTime[4] == "7":
        num3 = big7
    elif curTime[4] == "8":
        num3 = big8
    elif curTime[4] == "9":
        num3 = big9


    hold = ""

    for i in range(0,6):
        hold += num0[i]
    hold += " "
    for i in range(0,6):
        hold += num1[i]
    hold += " "
    hold += "   "
    for i in range(0,6):
        hold += num2[i]
    hold += " "
    for i in range(0,6):
        hold += num3[i]
    hold += " "
    print(hold)

    hold = ""
    for i in range(6,12):
        hold += num0[i]
    hold += " "
    for i in range(6,12):
        hold += num1[i]
    hold += " "
    hold += "   "
    for i in range(6,12):
        hold += num2[i]
    hold += " "
    for i in range(6,12):
        hold += num3[i]
    hold += " "
    print(hold)

    hold = ""
    for i in range(12,18):
        hold += num0[i]
    hold += " "
    for i in range(12,18):
        hold += num1[i]
    hold += " "
    hold += "o  "
    for i in range(12,18):
        hold += num2[i]
    hold += " "
    for i in range(12,18):
        hold += num3[i]
    hold += " "
    print(hold)

    hold = ""
    for i in range(18,24):
        hold += num0[i]
    hold += " "
    for i in range(18,24):
        hold += num1[i]
    hold += " "
    hold += "   "
    for i in range(18,24):
        hold += num2[i]
    hold += " "
    for i in range(18,24):
        hold += num3[i]
    hold += " "
    print(hold)

    hold = ""
    for i in range(24,30):
        hold += num0[i]
    hold += " "
    for i in range(24,30):
        hold += num1[i]
    hold += " "
    hold += "o  "
    for i in range(24,30):
        hold += num2[i]
    hold += " "
    for i in range(24,30):
        hold += num3[i]
    hold += " "
    print(hold)

    hold = ""
    for i in range(30,36):
        hold += num0[i]
    hold += " "
    for i in range(30,36):
        hold += num1[i]
    hold += " "
    hold += "   "
    for i in range(30,36):
        hold += num2[i]
    hold += " "
    for i in range(30,36):
        hold += num3[i]
    hold += " "
    print(hold)

    hold = ""
    for i in range(36,42):
        hold += num0[i]
    hold += " "
    for i in range(36,42):
        hold += num1[i]
    hold += " "
    hold += "   "
    for i in range(36,42):
        hold += num2[i]
    hold += " "
    for i in range(36,42):
        hold += num3[i]
    hold += " "
    print(hold)