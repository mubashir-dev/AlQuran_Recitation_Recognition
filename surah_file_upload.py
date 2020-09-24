import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from SearchFile import match_surha_ayaha

file = 'microphone-results.wav'

def file_surah_recog(file_url):
  r = sr.Recognizer()
  try:
    with sr.AudioFile(file) as source:
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
      try:
        startTime = time.time()
        value = r.recognize_google(audio, language="ar")
        print(value)
        print(match_surha_ayaha(value))
      except sr.UnknownValueError:
        print("Sorry, unable to understand recitation.")
      except sr.RequestError:
        print("Sorry, couldn't request results from Google Speech Recognition service")
  except KeyboardInterrupt:
    print("Sorry, couldn't request results from Google Speech Recognition service")

if __name__ == "__main__":
    import sys
  