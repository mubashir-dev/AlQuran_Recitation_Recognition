
#===========================IMPORTS============================#
import time

import playsound
import speech_recognition as sr
from gtts import gTTS

from SearchFile import match_index_surha


#===============================================================#


#==========================CORE METHODS=========================#
def speak(voice):
  tts = gTTS(text = voice,lang = "ar")
  filename = "voice.mp3"
  tts.save(filename)
  playsound.playsound(filename)
  voice = str("سورة ") + voice
  print(voice)
  print(match_index_surha(voice))

    

  
def microphone_audio():
  r = sr.Recognizer()
  m = sr.Microphone(sample_rate=44100)
  m.CHUNK = 8192
  
  try:
    print("# QURAN RECITATION RECOGNITION #")
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
        value = r.recognize_google(audio, language="ar-SA")
        # ayah = 'ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ'
        
        speak(value)
        #print(u"You said {}".format(value).encode("utf-8"))
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

microphone_audio()
#speak("سورة الفتح")