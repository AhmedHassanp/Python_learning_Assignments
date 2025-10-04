fh = open("mbox-short.txt")
count = 0
list1 = list()
for line in fh:
    line = line.rstrip()
    list1 = line.split()
    if len(list1) < 1 or list1[0] != "From":
        continue
    print(list1[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
