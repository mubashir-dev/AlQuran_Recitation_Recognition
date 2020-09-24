# ===========================IMPORTS============================#
import time

import playsound
import speech_recognition as sr
from gtts import gTTS

from SearchFile import match_surha_ayaha, match_index_surha

#================System Variables==============================
app_name = "Al-Quran Recitation Recognition System"

# ==========================CORE METHODS=========================#
def speaK_inital(voice):
  tts = gTTS(text=voice, lang="ur")
  filename = "voice.mp3"
  tts.save(filename)
  playsound.playsound(filename)
  print(voice)

def speak(voice,mode):
  tts = gTTS(text=voice, lang="ar")
  filename = "voice.mp3"
  tts.save(filename)
  playsound.playsound(filename)
  # voice = str("سورة ") + voice
  print(voice)
  if mode == 'surah':
    return match_index_surha(voice)
  else:
    match_surha_ayaha(voice)
#=================================Surah Mode====================================#
def surha_mode():
  r = sr.Recognizer()
  m = sr.Microphone(sample_rate=44100)
  m.CHUNK = 8192
  
  try:
    print(app_name.upper())
    print("# SPEAK SURHA NAME #")
    #speaK_inital("یہ ایپلیکیشن گوگل اسپیچ انجن کے ذریعہ چل رہی ہے ، اور اب آپ سورتوں کے سرچ موڈ میں ہیں ، لہذا براہ کرم اچھے چوہوں کا استعمال کریں اور متعلقہ سورت کا نام بلند اور صاف بات کریں ، اس سے آپ کی سورت مل جائے گی اور آپ کو واپس دے دی جائے گی۔ شکریہ!")
    with m as source:
      r.adjust_for_ambient_noise(source)
      print("PLEASE RECITE ....")
      audio = r.listen(source)
      print("GOT  IT ! NOW RECOGNIZING IT...")
      # write audio to a WAV file
      with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
      try:
        startTime = time.time()
        # recognize speech using Google Speech Recognition
        surahname = r.recognize_google(audio,language="ar")
        # ayah = 'ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ'
        surah_name = "سورة الفتح"
        speak(surah_name,'surah')
        print(u"You said {}".format(surah_name).encode("utf-8"))
#        processText(value)
        elapsedTime = time.time() - startTime
        print
        "Elapsed time: " + str(elapsedTime)
      except sr.UnknownValueError:
        print("Sorry, unable to understand recitation.")
      except sr.RequestError:
        print("Sorry, couldn't request results from Google Speech Recognition service")
  except KeyboardInterrupt:
    pass
#===============================================================================#

#======================================Ayah Mode=================================#
def ayah_mode():
  r = sr.Recognizer()
  m = sr.Microphone(sample_rate=44100)
  m.CHUNK = 8192
  
  try:
    print("# QURAN RECITATION RECOGNITION #")
    print("# SPEAK AYAH  #")
    with m as source:
      r.adjust_for_ambient_noise(source)
      print("PLEASE RECITE ....")
      audio = r.listen(source)
      print("GOT  IT ! NOW RECOGNIZING IT ...")
      # write audio to a WAV file
      with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
      
      try:
        startTime = time.time()
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio, language="ar")
        # ayah = 'ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ'
        speak(value)
        # print(u"You said {}".format(value).encode("utf-8"))
        # processText(value)
        elapsedTime = time.time() - startTime
        print
        "Elapsed time: " + str(elapsedTime)
      except sr.UnknownValueError:
        print("Sorry, unable to understand recitation.")
      except sr.RequestError:
        print("Sorry, couldn't request results from Google Speech Recognition service")
  except KeyboardInterrupt:
    pass

# microphone_audio()
#ayah = 'ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ'
#speak(ayah,'ayah')
#surha_mode()