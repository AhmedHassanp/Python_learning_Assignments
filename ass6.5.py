text = "X-DSPAM-Confidence:    0.8475"
# find the position of the colon
pos = text.find(':')
print(pos)
# slice from just after the colon to the end, and strip spaces
number_str = text[pos+1:].strip()
print (number_str)
# convert to float
number = float(number_str)
print(number)