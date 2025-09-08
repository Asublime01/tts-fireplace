from elevenlabs.client import ElevenLabs
from elevenlabs import play, VoiceSettings
import os

elevenlabs = ElevenLabs(
    api_key="sk_f7f638ba63c8bd00b379f458c73efab16a141e535c7a60df"
)




audio_generator = elevenlabs.text_to_speech.convert(
    text="The first move is what sets everything in motion.              You must first solve the issue of the imaginary before understanding the problem of the real. ",
    voice_id="unedM75kq90FMdXjOXWf",
    model_id=None,
    output_format="mp3_44100_128",
    voice_settings=VoiceSettings(speed=0.9, style=.6)
    
)

audio_bytes = b"".join(audio_generator)

with open("output.mp3", "wb") as f:
    f.write(audio_bytes)


