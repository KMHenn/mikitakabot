from random import randint
OPS = ["+", "-", "*", "/"]



######################################
##
######################################
def parse(input):#input, numDice):
    try:
        #input = (input.content)[2:].replace(" ", "")
        diceSplit = (input).split("d")
        numDice = int(diceSplit[0])
        print("\n\nnumDice : " + str(numDice) + "\tdiceSplit[1]: " + diceSplit[1])
        workStr = diceSplit[1]
        sideParse = getSides(workStr)
        print("exited getSides")
        numSides = sideParse[0]
        strInd = int(sideParse[1])
        print("numSides: " + str(numSides) + "\tstrInd: " + str(strInd))

        totalArr = roll(numDice, numSides)
        print("exited roll")
        total = totalArr[0]
        print("total: " + str(total))
        dispStr = "/r " + str(numDice) + "d" + str(numSides) + " = (" + totalArr[1] + ") " 
        print("dispStr: " + dispStr)
        curNum = ""
        curOp = ""

        for i in range(strInd, len(workStr)):
            print("in for loop: workStr[" + str(i) + "] = " + workStr[i])
            if workStr[i] in OPS:
                curOp = workStr[i]
                if i != strInd:
                    total = math(total, int(curNum), curOp)
                    dispStr = dispStr + " " + curOp + " " + curNum
                    curNum = ""
                    curOp = workStr[i]
            else:
                curNum = curNum + workStr[i]
        
        total = math(total, int(curNum), curOp)
        dispStr = dispStr + " " + curOp + " " + curNum + " = " + "**" + str(total) + "**"
        return dispStr
    except Exception as e:
        print(e)
        return

            



######################################
##
######################################
def getSides(input):
    print("In getSides")
    ind = 0
    intStr = ""

    for x in range(0, len(input)):
        if (input[x] not in OPS):
            print("\t while loop: input[x] = " + input[x])
            intStr =  intStr + input[x]
            print("\t intStr = " + intStr)
            ind = x
            print("\t x = " + str(x))
        else:
            break

    ind = ind + 1
    print("ind = " + str(ind) + "\tintStr = " + intStr)
    result = [int(intStr), ind]
    return result




######################################
##
######################################
def math(tot, newVal, op):
    print("In math")
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
    print("In roll")
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