import pyttsx3 as tts
import slate3k as slate
import os

def listenPdf(book):
    book_path = 'Books/'+book
    with open(book_path,'rb') as book:
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

    lis = os.listdir('Books')
    availableBooks = []
    for items in lis:
        if items.endswith('.pdf'):
            availableBooks.append(items)

    print(availableBooks)


    response = "y"
    while(response == 'y'):
        book = input("Which book do you want to listen? ")
        book = book.split(" ")
        book = '_'.join(book)
        book = book + '.pdf'
        book = book.lower()

        if book in availableBooks:
            listenPdf(book)
        else:
            print("Sorry book is not available\nPlease choose another book")

        response = input("Want to listen to more books? (y / n)")
        response = response.lower()
    