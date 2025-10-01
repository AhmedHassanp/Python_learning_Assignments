text = "X-DSPAM-Confidence:    0.8475"

# find the position of the colon
pos = text.find(':')

# slice from just after the colon to the end, and strip spaces
number_str = text[pos+1:].strip()

# convert to float
print(float(number_str))