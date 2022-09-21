import pyttsx3
import speech_recognition as sr
import datetime
from time import sleep
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour<12:
        speak("good morning Sir")
        print("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("good Afternoon sir")
        print("Good Afternoon Sir")

    else:
        speak("good evening sir")
        print("Good Evening Sir")

    speak("this is your artificial intelegence james")
    speak("how can i help you sir")
r=sr.Recognizer()
mic = sr.Microphone(device_index=1)
def takecomand():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2.5)
        print("Listening.....")
        audio = r.listen(source)

    try:
        print("Recoginizing....")
        query =r.recognize_google(audio)
        print("you said that:", query)

    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecomand().lower()

        #if 'hello' in query:
         #   speak("hello sir how can i help you")
          #  print("hello sir how can i help you")

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening sir")
            print("opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("opening sir")
            print("opening google")
            webbrowser.open("https://www.google.com/")

        elif 'open gmail' in query:
            speak("opening sir")
            print("opening gmail")
            webbrowser.open("mail.google.com")

        elif 'open stackoverflow' in query:
            speak("opening sir")
            print("opening openstackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            print("opening sir")
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif 'open vedantu' in query:
            speak("opening sir")
            print("opening vedantu")
            webbrowser.open("https://www.vedantu.com/home")

        elif 'download music' in query:
            speak("opening music downloading site sir")
            print("opening music downloading site")
            webbrowser.open("https://on-my-way.mp3quack.com/")

        elif 'download movie' in query:
            speak("opening movie downloading site sir")
            print("opening movie downloading site")
            webbrowser.open("hdmoviehubz")

        elif 'open amazon' in query:
            speak("opening sir")
            print("opening amazon")
            webbrowser.open("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=58075519359&hvpone=&hvptwo=&hvadid=486462777326&hvpos=&hvnetw=g&hvrand=737930739517037881&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9299781&hvtargid=kwd-64107830&hydadcr=14452_2154371&gclid=CjwKCAjwpqCZBhAbEiwAa7pXeVAt4FZ_WIlliJ3qg1krI1maosSwoXf1iWf2I_btUkROQ8ywF2MOkRoCPhwQAvD_BwE")

        elif 'open flipkart' in query:
            speak("opening sir")
            print("opening flipkart")
            webbrowser.open("flipkart.com")

        elif 'open quora' in query:
            speak("opening sir")
            print("opening quora")
            webbrowser.open("quora.com")


        elif 'open python' in query:
            speak("opening python website sir")
            print("opening python website")
            webbrowser.open("python.org")


        elif 'open cbse' in query:
            speak("opening cbse website")
            print("opening cbse website")
            webbrowser.open("http://cbse.nic.in/newsite/index.html")

        elif 'open cbse result' in query:
            speak("opening sir")
            print("opening cbseresult websie")
            webbrowser.open("cbseresult.nic.in")

        elif 'open w3schools' in query:
            speak("opening sir")
            print("opening w3schools")
            webbrowser.open("https://www.w3schools.com/")


        elif 'download games' in query:
            speak("opening downloading site sir")
            print("opening downloading site")
            webbrowser.open("https://www.oceaningames.com/")


        elif 'play music' in query:
            speak("playing sir")
            print("playing...")
            musics_dr = 'C:\\Users\\pande\\Music'
            songs=os.listdir(musics_dr)
            print(songs)
            ms=random.choice(songs)
            os.startfile(os.path.join(musics_dr, ms))

        elif 'play songs' in query:
            speak("playing sir")
            print("playing...")
            musics_dr = 'C:\\Users\\pande\\Music'
            songs=os.listdir(musics_dr)
            print(songs)
            os.startfile(os.path.join(musics_dr, songs[0]))

        elif 'time' in query:
            speak("time is")
            speak(strTime)
            print("Time:", strTime)
            strTime= datetime.datetime.now().strftime("%H:%M:%S")

        elif 'open visual studio' in query:
            speak("opening sir")
            print("opening...")
            codepath= "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open paint' in query:
            speak("opening sir")
            print("opening...")
            codepath2="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint"
            os.startfile(codepath2)


        elif 'open calculator' in query:
            speak("opening sir")
            print("opening...")
            codepath3="C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\Calculator"
            os.startfile(codepath3)

        elif 'open wordpad' in query:
            speak("opening sir")
            print("opening...")
            codepath4="C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\\WordPad"
            os.startfile(codepath4)

        elif 'open microsoft word' in query:

            speak("opening sir")
            print("opening...")
            codepath5="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007"
            os.startfile(codepath5)

        elif 'open excel' in query:
            speak("opening sir")
            print("opening...")
            codepath6="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
            os.startfile(codepath6)

        elif 'open power point' in query:
            speak("opening sir")
            print("opening...")
            codepath7="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007"
            os.startfile(codepath7)

        elif 'open access' in query:
            speak("opening sir")
            print("opening...")
            codepath8="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Access 2007"
            os.startfile(codepath8)

        elif 'open my sql' in query:
            speak("opening sir")
            print("opening...")
            codepath9="C:\\Program Files\\MySQL\\MySQL Server 5.1\\bin\\"
            os.startfile(codepath9)

        elif 'open physics notes' in query:
            speak("opening sir")
            print("opening....")
            codepath10= "C:\\Users\\abc\\Desktop\\class 12 physics notes"
            os.startfile(codepath10)

        elif 'open maths notes' in query:
            speak("opening sir")
            print("opening...")
            codepath11= "C:\\Users\\abc\\Desktop\\class 12 maths notes"
            os.startfile(codepath11)

        elif 'open physical chemistry notes' in query:
            speak("opening sir")
            print("opening...")
            codepath12= "C:\\Users\\abc\\Desktop\\physical chemistry"
            os.startfile(codepath12)

        elif 'open organic chemistry notes' in query:
            speak("opening sir")
            print("opening...")
            codepath13= "C:\\Users\\abc\\Desktop\\organic chemistry class 12"
            os.startfile(codepath13)

        elif 'open inorganic chemistry notes' in query:
            speak("opening sir")
            print("opening...")
            codepath14= "C:\\Users\\abc\\Desktop\\inorganic chemistry class 12"
            os.startfile(codepath14)

        elif 'open maths tatva' in query:
            speak("opening sir")
            print("opening....")
            codepath15= "C:\\Users\\abc\\Desktop\\maths tatva"
            os.startfile(codepath15)

        elif 'open chemistry tatva' in query:
            speak("opening sir")
            print("opening...")
            codepath16= "C:\\Users\\abc\\Desktop\\chemistry tatva"
            os.startfile(codepath16)

        elif 'open physics tatva' in query:
            speak("opening sir")
            print("opening...")
            codepath17="C:\\Users\\abc\\Desktop\\physics tatva"
            os.startfile(codepath17)

        elif 'exit james' in query:
            speak("have a good day sir")
            print("have a good day")
            quit()

