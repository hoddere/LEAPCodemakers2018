import sys
# This is regex
import re

# Get the hexadecimal value given as an argument
hexa = sys.argv[1]

# Split the hexadecimal into two character chunks
hexa = re.findall("..", hexa)
print(hexa)

# This will store the decimal representation of each chunk
decimalList = []


for byte in hexa:
	# Prints the chunks
	print(byte)
	
	# Implement your algorithm to convert the hexadecimal to a string here
	

