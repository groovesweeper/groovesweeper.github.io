'''
This is the script that runs the server and performs first-time
set up and hosts the server
'''

import os
import webbrowser

webbrowser.open_new("http://localhost:8000")
#os.system("python3 ./manage.py flush")
os.system("python ./manage.py runserver")
