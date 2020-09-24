# ===========================IMPORTS============================#
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

from SearchFile import match_surha_ayaha, match_index_surha

# ================System Variables==============================
app_name = "Al-Quran Recitation Recognition System"


# ==========================CORE METHODS=========================#
# def speaK_inital(voice):
#   tts = gTTS(text=voice, lang="ur")
#   filename = "voice.mp3"
#   tts.save(filename)
#   playsound.playsound(filename)
#   print(voice)


def speak(voice):
  tts = gTTS(text=voice, lang="ar")
  filename = "surah_wav_files/سورة الفاتحة.wav"
  tts.save(filename)
  playsound.playsound(filename)
  # voice = str("سورة ") + voice
  print(voice)

# speak('سورة الفاتحة')
r = sr.Recognizer()

PATH =  "surah_wav_files/سورة الفاتحة.wav"

with sr.AudioFile(PATH) as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s.encode("utf-8"))
except Exception as e:
    print("Exception: "+str(e))
