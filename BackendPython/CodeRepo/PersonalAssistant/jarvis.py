import speech_recognition as sr

# obtain audio from the microphone
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
      print("Listening...")
        # pass the source to the recognizer
      voice = listener.listen(source)
        # recognize speech using Google Speech Recognition
      command = listener.recognize_google(voice)

except:
    pass
