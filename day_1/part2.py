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
            for i in range(amount):
                curNum = (curNum + 1) % 100
                zeroCount += len(str(curNum == 0)) == 4
                
        if dir == "L":
            for i in range(amount):
                curNum = (curNum - 1) % 100
                zeroCount += len(str(curNum != 0)) == 5
            
print(zeroCount)