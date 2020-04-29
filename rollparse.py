from random import randint
OPS = ["+", "-", "*", "/"]



######################################
##
######################################
def parse(input):
    try:
        diceSplit = (input).split("d")
        numDice = int(diceSplit[0])
        workStr = diceSplit[1]
        sideParse = getSides(workStr)
        numSides = sideParse[0]
        strInd = int(sideParse[1])

        totalArr = roll(numDice, numSides)
        total = totalArr[0]
        dispStr = "/r " + str(numDice) + "d" + str(numSides) + " = (" + totalArr[1] + ")"
        curNum = ""
        curOp = ""

        if strInd != len(workStr):
            for i in range(strInd, len(workStr)):
                print("in for loop: workStr[" + str(i) + "] = " + workStr[i])
                if workStr[i] in OPS:
                    if i != strInd:
                        total = math(total, int(curNum), curOp)
                        dispStr = dispStr + " " + curOp + " " + curNum
                        curNum = ""
                        curOp = workStr[i]
                else:
                    curNum = curNum + workStr[i]
            
            total = math(total, int(curNum), curOp)
            dispStr = dispStr + " " + curOp + " " + curNum + " = " + "**" + str(total) + "**"
        else:
            dispStr = dispStr + " = **" + str(total) + "**"

        return dispStr

    except Exception as e:
        print(e)
        return

            



######################################
##
######################################
def getSides(input):
    ind = 0
    intStr = ""

    for x in range(0, len(input)):
        if (input[x] not in OPS):
            intStr =  intStr + input[x]
            ind = x
        else:
            break

    ind = ind + 1
    result = [int(intStr), ind]
    return result




######################################
##
######################################
def math(tot, newVal, op):
    result = ""

    if op == '+':
        result = tot + newVal
    elif op == '-':
        result = tot - newVal
    elif op == '*':
        result = tot * newVal
    elif op == '/':
        result = tot / newVal
    
    return result


######################################
## Roll specified number of dice
######################################
def roll(numDice, numSides):
    total = 0
    rollStr = ""

    for x in range (0, numDice):
        r = randint(1, numSides)
        if x == 0:
            rollStr = str(r)
        else:
            rollStr = rollStr + "+" + str(r)
        total += r
    return [total, rollStr]