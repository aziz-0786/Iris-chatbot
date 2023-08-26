import speech_recognition as sr
import os
import webbrowser
import openai
# import winsound
import datetime
# import subprocess
# import random
# import numpy as np
from config import apikey
from utils import say


chatStr = ""


def chat(query):
    global chatStr
    print(chatStr)

    try:
        openai.api_key = apikey
        chatStr += f"Aziz: {query}\n Chatbot: "
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        print(f"Chat function failed: {e}")


def generate_openai_response(prompt):
    try:
        openai.api_key = apikey
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
        text += response["choices"][0]["text"]
        save_response(text, prompt)

    except Exception as e:
        print(f"OpenAI API error: {e}")


def save_response(text, prompt):
    directory = "openai_responses"
    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(f"{directory}/{prompt}.txt", "w") as f:
        f.write(text)


if __name__ == '__main__':
    prompt = "How much is 2+2?"
    generate_openai_response(prompt)


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured. Sorry"

if __name__ == '__main__':
    print('Welcome to desktop assistant')
    say("hellooo i am Iris")
    while True:
        print("Listening..")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],["my github", "https://github.com/aziz-0786/projects"],
                 ["map", "https://www.google.com/maps/@30.7557869,76.5834984,15z?entry=ttu"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "play song" in query:
            musicPath = r"C:\Users\abdul aziz\PycharmProjects\Ai-chatbot\Cheques.mp3"
            os.system(f'start "" "{musicPath}"')

        elif "the time" in query:

            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours {min} minutes")


        def open_chrome():
            os.system('start "Chrome" "C:\Program Files\Google\Chrome\Application\chrome.exe"')

        def open_git():
            os.system('start "version control" "C:\Program Files\Git\git-cmd.exe"')

        def open_browser():
            os.system('start "browser" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')


        if "chrome".lower() in query.lower():
            open_chrome()
        elif "version control".lower() in query.lower():
            open_git()
        elif "browser".lower() in query.lower():
            open_browser()
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Quit ".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        #say(query)

