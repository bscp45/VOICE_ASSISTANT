import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=acb157f271124e8982062dd620194465" ,#Enter Your OWN API ,
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=acb157f271124e8982062dd620194465",#Enter Your OWN API ,
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=acb157f271124e8982062dd620194465",#Enter Your OWN API,
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=acb157f271124e8982062dd620194465",#Enter Your OWN API,
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=acb157f271124e8982062dd620194465",#Enter Your OWN API,
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=acb157f271124e8982062dd620194465",#Enter Your OWN API
            "politics" :"https://newsapi.org/v2/top-headlines?country=in&apiKey=acb157f271124e8982062dd620194465",#Enter Your OWN API
            "International" :"https://newsapi.org/v2/everything?q=tesla&from=2023-03-20&sortBy=publishedAt&apiKey=acb157f271124e8982062dd620194465"#Enter Your OWN API
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science], [politics], [international]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

