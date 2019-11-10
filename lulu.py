from gtts import gTTS
from googletrans import Translator
translator = Translator()
import os   
def transi(s):
      translated = translator.translate(s, src='en', dest='bn') 
      return translated.text


translated = translator.translate('kemon achho', src='bn', dest='en')  
print(translated.text)
from playsound import playsound


globalStore='k'
#code begins here

import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib
import goslate

gs = goslate.Goslate()

#choice the voice for sara


#sara will speak here

def speak(ps):
    global globalStore
    gss=transi(ps)
    globalStore+='k'
    tts=gTTS(gss,lang='bn')
    tts.save(globalStore+'.mp3')
    playsound(globalStore+'.mp3')
    os.remove(globalStore+'.mp3')      

#this will make every text from bangla to english
def trans(s):
      translated = translator.translate(s, src='bn', dest='en') 
      return translated.text

#making wish me function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning")
    elif(hour>=12 and hour <18):
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!")
    speak("I am sara , how can i help you")        

# this function will take the commands by microphone and act like that
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1 
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-bn')
        print("User Said ",query)    
    except Exception as e:
        print(e)
        print("Say that again....")
        return "None"
    return query




#send email funtion
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #print("AISE")
    server.login('zubairahmedrafi37@gmail.com','zunaidahmedzaki')
    server.sendmail('zubairahmedrafi37@gmail.com',to,content)
    server.close()


# main function starts here
if __name__ == "__main__":
    wishMe()
    #Varibale For mp3
    store='a'
    while True:
        query = takeCommand().lower()
        
        #transfer command into Bangla
        bangla=trans(query)
        print(bangla)
    

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2 )
            speak("according to wikipedia")
            ss=transi(results)
            store+='a'
            tts=gTTS(ss,lang='bn')
            tts.save(store+'.mp3')
            playsound(store+'.mp3')
            os.remove(store+'.mp3')
            #speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        elif 'open google' in query:
            webbrowser.open("google.com")  
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play movies' in query:
            mov_dir='F:\\AVENGER SERies'
            movies=os.listdir(mov_dir)
            print(movies)
            os.startfile(os.path.join(mov_dir,movies[3]))      
        elif 'exit' in query:
            ss=transi("Bye Sir, Have a nice Day")
            store+='a'
            tts=gTTS(ss,lang='bn')
            tts.save(store+'.mp3')
            playsound(store+'.mp3')
            os.remove(store+'.mp3')           
            
            #speak("Bye sir, Have a nice day")
            sys.exit(0)   
        elif 'the time' in query:
            strt= datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"sir the time is {strt}")
        elif 'send email' in query:
            try:
                 ss=transi("What Should I Say")
                 store+='a'
                 tts=gTTS(ss,lang='bn')
                 tts.save(store+'.mp3')
                 playsound(store+'.mp3')
                 os.remove(store+'.mp3')
                 content = takeCommand()
                 to ="zubairahmedrafi37@gmail.com"
                 sendEmail(to,content)
            except Exception as e:
                 print(e)
                 ss=transi("Cant Send It")
                 store+='a'
                 tts=gTTS(ss,lang='bn')
                 tts.save(store+'.mp3')
                 playsound(store+'.mp3')
                 os.remove(store+'.mp3')    