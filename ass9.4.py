fh = open("mbox-short.txt")
list1 = list()
sender = dict()

for line in fh:
    line = line.rstrip()
    list1 = line.split()
    if len(list1) < 1 or list1[0] != "From":
        continue
    for word in list1[1:2]:
        sender[word] = sender.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
