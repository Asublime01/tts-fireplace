from flask import Flask, request, jsonify
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from playsound import playsound

# Initialize ElevenLabs client
elevenlabs = ElevenLabs(
    api_key="sk_f7f638ba63c8bd00b379f458c73efab16a141e535c7a60df"
)

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    print(f"Received data: {data}")

    if 'message' not in data:
        return jsonify({"error": "No message field"}), 400

    message = data['message']

    # Generate speech
    audio_generator = elevenlabs.text_to_speech.convert(
        text=message,
        voice_id="unedM75kq90FMdXjOXWf",
        model_id=None,
        output_format="mp3_44100_128",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.7
        )
    )

    audio_bytes = b"".join(audio_generator)

    with open("output.mp3", "wb") as f:
        f.write(audio_bytes)

    # Play the audio
    playsound('output.mp3')

    return jsonify({"status": "success", "message": message})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
