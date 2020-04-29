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
        print("numDice : " + str(numDice) + "\tdiceSplit[1]: " + diceSplit[1])

        sideParse = getSides(diceSplit[1])
        print("exited getSides")
        numSides = sideParse[0]
        print("numSides : " + str(numSides))
        strInd = sideParse[1]

        totalArr = roll(numDice, numSides)
        total = totalArr[0]
        dispStr = "/r " + str(numDice) + "d" + str(numSides) + " = (" + totalArr[1] + ") " 
        curNum = ""
        curOp = ""

        for i in range(strInd, len(input)):
            if input[i] in OPS:
                curOp = input[i]
                if i != strInd:
                    total = math(total, int(curNum), curOp)
                    dispStr = dispStr + " " + curOp + " " + curNum
                    curNum = ""
                    curOp = input[i]
            else:
                curNum = curNum + input[i]
        
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

    while input[ind] not in OPS:
        print("\t while loop: input[ind] = " + input[ind])
        intStr =  intStr + input[ind]
        print("\t intStr = " + intStr)
        ind = ind + 1
        print("\t ind = " + str(ind))
    
    print("ind = " + ind + "\tintStr = " + intStr)
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