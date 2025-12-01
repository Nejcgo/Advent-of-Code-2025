startingNum = 50
curNum = startingNum
zeroCount = 0

with open("1-input.txt") as file:
    text = file.read().split("\n")
    
    for act in text:
        #print(act)
        if act == "": continue
        dir = act[0]
        amount = int(act[1:])
        
        if dir == "R":
            zeroCount += abs((curNum + amount) // 100)
            curNum = (curNum + amount) % 100
                
        if dir == "L":
            if curNum != 0 and (curNum - amount) % 100 != 0:
                zeroCount += abs((curNum - amount) // 100)
            elif (curNum - amount) % 100 == 0:
                zeroCount += abs((curNum - amount) // 100) + 1
            else:
                zeroCount += abs((curNum - amount) // 100) - 1
            curNum = (curNum - amount) % 100
            
print(zeroCount)