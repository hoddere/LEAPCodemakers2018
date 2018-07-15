import sys
import os

# Link
"https://translate.google.com/translate_tts?ie=UTF-8&tl=fr&client=tw-ob&q=%22Bonjour%20tout%20le%20monde%22"

# Get text and split into words (removing excess whitespace)
text = sys.argv[1]
words = text.split()

# Reconstructs the text without whitespace
totalText = " ".join(words)

# If the text is already less than 200 characters, just speak it
if len(totalText) < 200:
	os.system('mpg123 -q "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=' + totalText + '&tl=En-uk"')
	exit()

# Otherwise, start counting characters
characters = 0
segment = []
segments = []

# Create text segments that are 200 characters or less and contain whole words
for word in words:
	if len(word) + characters + 1 <= 200:
		characters += len(word) + 1
		segment.append(word)
	else:
		segments.append(" ".join(segment))
		segment = [word]
		characters = len(word)

# Add final partial text segment (less than 200 characters) to the segments		
segments.append(" ".join(segment))

# Speak each segment
for segment in segments:
	os.system('mpg123 -q "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=' + segment + '&tl=en-uk"')

