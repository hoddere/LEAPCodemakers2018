#!/bin/bash
# TEST RASPI 


NAME=$1


# CLEANUP
rm -f test.jpg test.txt


# ADJUST AUDIO VOLUME
# Change VOLUME to increase/decrease 0-100%
VOLUME=100%
echo "Setting volume to $VOLUME"
sudo amixer -q sset PCM,0 ${VOLUME}


# PLAY SPEECH 
echo "playing TTS"
./speech3.sh "Hi, $NAME! This is the Raspberry  Reader. I can read your documents aloud to you. Please place a document with a good contrast between the text and background on my surface, and when you're ready press the button to start."

# WAIT FOR BUTTON
sudo python3 button.py
# TEST CAMERA
echo "taking photo"
./speech3.sh "I'm taking a photo of your document now."
raspistill -cfx 128:128 --awb auto -rot 180 -t 500 -o test.jpg
ls -l test.jpg

# OCR test
echo "Converting to Text, standby..."
./speech3.sh "Just a minute, $NAME. I have to analyze what I see."
tesseract test.jpg test
cat test.txt

# SPEAK TEXT
textstring=`cat test.txt`
./speech3.sh $textstring

# FINISH
./speech3.sh "That's all the text that I could see. Have a good day, $NAME!"

# Run a web server to view photo
IP=`hostname -I`
IP=${IP%?}
echo "To see photo, browse to http://$IP:8080/test.jpg"
echo "Press Ctrl-C to exit"
python -m SimpleHTTPServer 8080

