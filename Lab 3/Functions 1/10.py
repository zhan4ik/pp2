list = [1,2,4,0,0,7,5]
uniqueList = []

def unique(list):
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    
    print(uniqueList)
        
unique(list)
    