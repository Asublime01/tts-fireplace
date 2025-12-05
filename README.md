# 🔥 TTS Fireplace

A Raspberry Pi-powered text-to-speech system that plays spoken audio messages when triggered by external events (e.g., puzzles in an escape room). Messages are generated on demand using TTS and can also be replayed using a physical button.

This project can be adapted for **escape rooms**, **interactive art installations**, **smart-home effects**, or anyone who wants to trigger TTS audio from Python scripts.

---

## 💡 How It Works

This system listens for short text messages sent from another device (such as a puzzle controller). When a message arrives:

1. The message is passed to a Python script (`pi_code.py`) via a command-line argument.  
2. `pi_code.py` converts the text to audio using Text-to-Speech (TTS).  
3. The audio file is saved locally on the Raspberry Pi.  
4. The file plays automatically through a connected speaker.  
5. A physical button on the fireplace can replay the most recent message at any time.

The result is a dynamic “talking fireplace” that speaks different lines depending on puzzle progress or triggers you define.

---

## 📝 Changing the Spoken Message

If you're integrating this into an escape room or other system, you can trigger the fireplace to speak any text you choose.

Inside **`lockButtons.py`**, look for a line containing:

```python
os.system("python3 pi_code.py <your message here>")
```
