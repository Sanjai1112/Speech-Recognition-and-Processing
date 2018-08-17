from gtts import gTTS
import speech_recognition as sr
# import datetime
import pygame
import time   
# class msgs:
#     def __init__(self,speech):
#         self.time = datetime.datetime.now()
#         self.message = speech
def function():
    tts=gTTS(text="What problem do you have",lang="en")
    tts.save("question.mp3")
        #os.system("both.mp3")
    pygame.mixer.music.load("question.mp3")
    pygame.mixer.music.play()
    time.sleep(4)
    print("Listening your disease")
    with m as source:
        audio=r.listen(source)
    try:
        disease=r.recognize_google(audio)
        diseaseList.append(disease)
        value = "you have "+disease
        print(value) 
        # userSpeech.append(msgs(value))
        tts=gTTS(text=value,lang="en")
        tts.save("disease.mp3")
        #os.system("both.mp3")
        pygame.mixer.music.load("disease.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        return disease
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        print("No data given")
    pass
# for i in userSpeech:
#     print(str(i.time) + ": " + i.message)
nameList=[]
diseaseList=[]
myDiseaseDict={'fever':'you can go to ward 1','hepatitis':'you can go to ward 2','fracture':'you can go to ward 3','tuberclosis':'you can go to ward 4'}
pygame.init()
r=sr.Recognizer()
m=sr.Microphone()
tts=gTTS(text="Hi Hello,i am your assistant,Tell me What is your name",lang="en")
tts.save("welcome.mp3")
pygame.mixer.music.load("welcome.mp3")
pygame.mixer.music.play()
time.sleep(4)
print("Listening your name")
# userSpeech = []
while True:
    with m as source:
        audio=r.listen(source)
        #print(id(audio))
    try:
        name=r.recognize_google(audio)
        nameList.append(name)
        value = "your name is "+name
        print(value) 
        # userSpeech.append(msgs(value))
        tts=gTTS(text=value,lang="en")
        tts.save("name.mp3")
        #os.system("both.mp3")
        pygame.mixer.music.load("name.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        disease = function()
        print(disease)
        place=myDiseaseDict[disease]
        tts=gTTS(text=place,lang="en")
        tts.save("place.mp3")
        pygame.mixer.music.load("place.mp3")
        pygame.mixer.music.play()
        time.sleep(4)

        # print("Carry on")
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        break
    except sr.UnknownValueError:
        break