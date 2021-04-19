import os
import webbrowser

def firstTimeSetup():
    print("Doing first time setup\n.\n.\n.")
    f = open("./dist/first_time.txt", "w")
    try:
        import django
    except:
        print("Django not installed-- Installing Now\n.\n.\n.")
        os.system("pip install django")
    try:
        import lyricsgenius
    except:
        print("Lyricsgenius not installed-- Installing Now\n.\n.\n.")
        os.system("pip install lyricsgenius")




if __name__ == "__main__":
    if (os.path.exists("./dist/first_time.txt") == False):
        firstTimeSetup()
    webbrowser.open_new("http://localhost:8000")
    #os.system("python3 ./manage.py flush")
    os.system("python3 ./manage.py runserver")
