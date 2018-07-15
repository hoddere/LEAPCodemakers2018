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
	
	# Create a list of characters in the chunk and reverse it
	chars = list(byte)
	chars.reverse()
	
	# We need to add to the decimal as we iterate
	decimal = 0
	
	# Decimal versions of hexadecimal letters
	hexRepr = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
	
	# Runs for each character in the chunk
	for char in range(len(chars)):
		
		try: 
			# Add to the decimal value 16 raised to the
			# power of the index of the character times the character
			decimal += 16 ** char * int(chars[char])
		except:
			
			# If it we get a multiplication error, we need to convert
			# the hexadecimal letter to an integer
			decimal += 16 ** char * int(hexRepr[chars[char]])
			
	# Add the finished decimal sum to our list of decimals
	decimalList.append(decimal)

# Basis for the constructed string
string = ""

# For each decimal in the list, get the ASCII character, add it to the string
for decimal in decimalList:
	string += chr(decimal)

# Print the final string
print(string)


