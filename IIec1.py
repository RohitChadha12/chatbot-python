import os
import pyttsx3
print("welcome to project")
pyttsx3.speak("welcome to project")
while True:
    pyttsx3.speak("what you want to do:")
    s=input("what you want to do:")
    pyttsx3.speak(s)
#For a notepad
    if(("run" in s or "start" in s or "execute" in s or "open" in s) and ("notepad" in s or "editor" in s)):
        os.system("notepad")
        pyttsx3.speak("starting a notepad")
#For a Chrome
    elif(("run" in s or "start" in s or "execute" in s or "open" in s) and("chrome" in s or "google" in s or "browser" in s)):
        os.system("start chrome")
        pyttsx3.speak("starting a chrome your default browser")
# for a window media player
    elif(("run" in s or "start" in s or "execute" in s or "open" in s) and ("media" in s or "player" in s )):
        os.system(wmplayer)
        pyttsx3.speak("opening a window media player")
#for a vlc player
    elif(("run" in s or "start" in s or "execute" in s or "open" in s) and ("vlc" in s)):
        os.system(vlc)
        pyttsx3.speak("starting a vlc")
#for to create a directory or folder
    elif(("make" in s or "create" in s) and ("directory" in s or "folder" in s)):
        os.mkdir("demo")
        pyttsx3.speak("folder is created")
#for to start firefox
    elif(("run" in s or "start" in s or "execute" in s or "open" in s) and("firefox" in s )):
        os.system("start firefox")
        pyttsx3.speak("firefox is opened")
#For to open jupyter notebook
    elif(("run" in s or "start" in s or "execute" in s or "open" in s) and("jupyter" in s or "notebook" in s )):
        os.system("start jupyter notebook")
        pyttsx3.speak("jupyter notebook is opened")
#For to open command prompt
    elif(("run" in s or "start" in s or "execute" in s or "open" in s) and("cmd" in s or "command prompt" in s )):
        os.system("start cmd")
        pyttsx3.speak("command prompt is started")
#display computer specific property
    elif(("show" in s or "display" in s or "open" in s) and ("computer specific properties" in s or "computer specific configuration" in s)):
        os.system("systeminfo")
        pyttsx3.speak("see your system configuration")
#copy 1 file to another
    elif(("copy" in s) and ("a.py" in s) and ("to b.py" in s)):
        os.system("copy a.py b.py")
        pyttsx3.speak("file a is copied to another file b")
    else:
        print("could not found")