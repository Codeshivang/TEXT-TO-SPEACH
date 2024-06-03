#created by coderation
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
   while True:
    text = input("Enter the text you want the robo speaker to say: ")
    if text=="q":
       break
    speak(text)
