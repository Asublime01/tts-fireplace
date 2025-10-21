# Fireplace-Documentation


This piece of hardware / software uses Text-to-Speech (TTS) software, which can
take written text and turn it into spoken audio. The fireplace is connected to a speaker so
players hear the voice out loud. When another puzzle in the escape room is solved, the
computer running that puzzle sends a short message to the fireplace’s computer. The fireplace
software takes this message, converts it into an audio file using TTS, and then plays the audio
file over the speaker for the contestants to hear. This audio message is then stored on the Raspberry Pi and can be replayed if the button is pressed.


## How to Change the Message
1. In **lockButtons.py** locate the line of code that has *"os.system("")"* mentioned
2. This line contains a command similar or the same as ```python3 pi_code.py [insert new message here]```
3. The pi_code.py program takes a command line argument to change the puzzle completion message to something else, so all you have to do is insert your own message in the ```[insert new message here] ``` location.
4. The os.system function can be called anywhere in the *lockButtons.py* script to make the fireplace say something or give a hint. **All you have to do is change the message**

## How To Run
Unplug and plug in the fireplace raspberry pi (It's code runs on startup over and over again until it looses power)
Run ```os.system("python3 pi_code.py insert_message_here")``` anywhere you would like to change the message in **lockButtons.py** 
