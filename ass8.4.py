fh = open("romeo.txt")
list1 = list()
for line in fh:
    word = line.split()
    for w in word:
        if w in list1:
            continue
        else:
            list1.append(w)
list1.sort()
print(list1)