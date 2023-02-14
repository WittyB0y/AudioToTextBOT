import speech_recognition as sr
from pydub import AudioSegment


def audio_to_text(file):
    r = sr.Recognizer()
    sound = AudioSegment.from_ogg(file)
    res = sound.export(f'{file.replace(".oga", ".wav")}', format="wav")
    with sr.AudioFile(f"{res.name}") as source:
        audio_text = r.record(source)
    return r.recognize_google(audio_text, language="ru-RU")
