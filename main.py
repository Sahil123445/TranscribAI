import whisper

model = whisper.load_model("base")
result = model.transcribe("Audio_file.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])