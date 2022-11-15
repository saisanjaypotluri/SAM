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
    try:
        with speech.Microphone() as source:
            user = input("What can I call you? ")
            speaker.say(f'Hello {user}, what can I do for you')
            speaker.runAndWait()
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            # print(command)
        if 'SAM' or 'Sam' or 'sam' in command:
                command = command.replace('sam', '')
                # print(command)

    except:
        pass
    return command

def run_sam():
    command = take_command()
    print(command)
    if 'Play' and 'on youtube' in command:
        media = command.replace('play', '')
        speakout(f" Playing {media}")
        print(f"Playing: {media}")
        pywhatkit.playonyt(media)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p') #Use strftime("%I: %M %p") for am or pm format
        # or use strftime("%H: %M") for 24h format
        speakout(f"The time's {time}")
        print(time)
    elif "who is" in command:
        person = command.replace("Who is", "")
        info = wikipedia.summary(person, 1)
        speakout(info)
        print(info)
    elif 'joke' in command:
        speakout(pyjokes.get_joke())

run_sam()