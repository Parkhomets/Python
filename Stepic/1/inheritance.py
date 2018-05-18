count = int(input())

box = {}

#filling
for i in range(count):
    sous = input()
    sous = sous.split(" ")
    try:
        sous.remove(":")
    except:
        pass
    var = sous[0]
    var1 = sous[1::]
    if var in box:
        box.get(var).extend(var1)
    else:
        temp = {var: var1}
    box.update(temp)

count = int(input())
#print(box)
def find_parent(class1, class2):
    #print(class1, " ", box.get(class2))
    if class1 == class2:
        #print("Yes")
        return True


    try:
        if len(box.get(class2)) != 0:
            if class1 in box.get(class2):
                return True
            else:
                for i in box.get(class2):
                    #print(i)
                    if i in box.keys():
                        if len(box.get(i)) != 0:
                            if find_parent(class1, i):
                                return True
                    else:
                        return
    except:
        pass
        #print("LLL")
    return False



for i in range(count):
    sous = input().split(" ")
    if find_parent(sous[0], sous[1]):
        print("Yes")
    else:
        print("No")


