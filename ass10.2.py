fh = open("mbox-short.txt")
list1 = list()
time = list()
hour = dict()

for line in fh:
    line = line.rstrip()
    list1 = line.split()
    if len(list1) < 1 or list1[0] != "From":
        continue
    for word in list1[5:6]:
        time = word.split(':')
        for word in time[0:1]:
            hour[word] = hour.get(word, 0) + 1

hour = list(hour.items())
hour.sort(reverse=False)
for word, count in hour:
    print(word, count)
