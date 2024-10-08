import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

def speakout(text):
    speaker.say(text)
    speaker.runAndWait()

listener = speech.Recognizer()
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

def take_command():
    command = ""
    try:
        with speech.Microphone() as source:
            user = input("What can I call you? ")
            speakout(f'Hello {user}, what can I do for you')
            print("listening...")
            listener.adjust_for_ambient_noise(source)  # helps in noisy environments
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            
        if 'sam' in command:
            command = command.replace('sam', '').strip()
                
    except Exception as e:
        print(f"Error: {e}")
        speakout("Sorry, I couldn't understand.")
        
    return command

def run_sam():
    command = take_command()
    print(command)
    
    if 'play' in command and 'on youtube' in command:
        media = command.replace('play', '').replace('on youtube', '').strip()
        speakout(f"Playing {media}")
        print(f"Playing: {media}")
        pywhatkit.playonyt(media)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  # AM/PM format
        speakout(f"The time is {time}")
        print(time)
    elif "who is" in command:
        person = command.replace("who is", "").strip()
        info = wikipedia.summary(person, 1)
        speakout(info)
        print(info)
    elif 'joke' in command:
        speakout(pyjokes.get_joke())
    else:
        speakout("Sorry, I didn't get that.")

run_sam()
