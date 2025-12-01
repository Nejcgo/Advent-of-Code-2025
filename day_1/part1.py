startingNum = 50
curNum = startingNum
zeroCount = 0

with open("1-input.txt") as file:
    text = file.read().split("\n")
    
    for act in text:
        print(act)
        if act == "": continue
        dir = act[0]
        amount = int(str(act[1:])) % 100
        
        if dir == "R":
            curNum = (curNum + amount) % 100
            if curNum == 0:
                zeroCount += 1
                
        if dir == "L":
            curNum = (curNum - amount) % 100
            if curNum == 0:
                zeroCount += 1
            
print(zeroCount)