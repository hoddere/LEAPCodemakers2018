#!/bin/bash
# Raspberry Reader

# This is a Bash variable called name
# We're getting the name from an argument passed to the script
NAME=$1

# Cleaning up previous files (if they exist)
# The -f flag in rm removes files forcefully (won't complain if nonexistent)
rm -f test.jpg text.txt

# Turn the volume up
VOLUME=100%
echo "Changing the volume to $VOLUME"
sudo amixer -q sset PCM,0 ${VOLUME}

# Greeting using espeak. Sounds a bit robotic... Can we improve?
echo "Hello, $NAME. This is the Raspberry Reader!"

# Takes a photo using raspistill and flips it the right way
echo "Taking photo"
raspistill -cfx 128:128 --awb auto -rot 180 -t 500 -o test.jpg

# Use OCR to recognize text

# Speak recognized text aloud

# Finish
echo "That's all the text I recognized. Have a good day, $NAME."

