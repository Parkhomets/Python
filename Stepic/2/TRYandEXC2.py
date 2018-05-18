count = int(input())
box = {}
for i in range(count):
    sous = input()
    if ":" in sous:
        sous = sous.split(" ")
        sous.remove(":")
        box.update({sous[0]: sous[1::]})
    else:
        box.update({sous: []})

count = int(input())
seq = []
for i in range(count):
    seq.append(input())

def find_parent(class1, class2):
    if class1 == class2:
        return True
    try:
        if len(box.get(class2)) != 0:
            if class1 in box.get(class2):
                return True
            else:
                for i in box.get(class2):
                    if i in box.keys():
                        if len(box.get(i)) != 0:
                            if find_parent(class1, i):
                                return True
                    else:
                        return
    except:
        pass
    return False

print(box)
print(seq)
er = []
i = len(seq) - 1
while i >= 0:
    j = 0
    while j < i:
        if find_parent(seq[j], seq[i]):
            er.append(seq[i])
            break
        j += 1
    i -= 1

er = er[::-1]
for i in er:
    print(i)
