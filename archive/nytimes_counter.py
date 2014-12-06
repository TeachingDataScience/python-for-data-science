## Download the file into ~/Downloads
## run: python nytimes_counter.py < ~/Downloads/nyt1.csv
# Import required libraries
import sys

# Start a counter and store the textfile in memory
gender = 0
signins = 0
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
  gender = gender + int(line.strip().split(',')[1])

for line in lines:
  signins = signins + int(line.strip().split(',')[4])

gender_0 = len(lines) - gender
signins_0 = len(lines) - signins

print "Gender 0: ", gender_0
print "Gender 1: ", gender_1
print "Signin 0: ", signins_0
print "Signin 1: ", signins_1