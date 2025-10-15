# This code reads a file and extracts numbers from each line, summing them up.
fh = open("regex_sum_2304132.txt")
# Importing the regular expression module
# This module provides support for regular expressions in Python
import re
# Initialize an empty list to store numbers
list1 = list()

# Iterate through each line in the file
for line in fh:
    # Strip leading and trailing whitespace
    line = line.strip()
    # If the line is empty, skip it
    if len(line) == 0:
        continue
    # Extract numbers from each line and add to list1
    if re.search('[0-9]+', line):
        # Find all numbers in the line and convert them to integers
        numbers = re.findall('[0-9]+', line)
        for number in numbers:
            list1.append(int(number))
    else:
        # If no numbers found, append 0 to list1
        list1.append(0)
# Print the sum of numbers found so far
print(sum(list1))