import pyttsx3 as tts
import slate3k as slate

def listenPdf(book):
    book_name = book+'.pdf'
    with open(book_name,'rb') as book:
        text = slate.PDF(book)
    listenMore = "y"
    while(listenMore == "y"):

        pageToListen = int(input("Which page do you want to listen to? "))
        print(text[pageToListen])

        speaker = tts.init()

        speaker.say(text[pageToListen])

        speaker.runAndWait()
        
        listenMore = input("Want to listen more? (y / n) ")

if __name__ == '__main__':
    book = input("Which book do you want to listen? ")
    
    listenPdf(book)
    