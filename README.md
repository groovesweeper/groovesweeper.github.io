# Overview  
This app allows you to rapidly find whether or not songs contain explicit lyrics. To use, simply configure your filter (which comes pre-equipped with not only the seven dirty words but several other common swears,) then use our search feature to hunt for a song. GrooveSweeper will then tell you what words in the lyrics violate your definition of explicit.

## Use
GrooveSweeper is simple to set up and easy to use.

* First, create an account on `https://genius.com/api-clients` and select "Create new API" in the sidebar. You can enter whatever you choose into the fields, as long as there is a valid http:// website in the App URL (`http://example.com` for instance)

* Next, find a file named `template_client_details.txt` in the directory `/groovesweepersite/groovesweeperapp/src/model`. Replace the <bracketed> information with the fields from the genius API client and save the file in the same directory as `client_details.txt`

* Next, find a file in `/groovesweepersite/groovesweepersite/` called `template_local_settings.py`. Replace the `<SECRET KEY>` in the brackets with a string randomly generated from this website `https://miniwebtool.com/django-secret-key-generator/`. Save this edited file in the same directory as `local_settings.py`

* Finally, to use GrooveSweeper you simply need to run `python ./run.py` from the `groovesweeper.github.io/groovesweepersite` directory. You may need to refresh the browser window that is opened by this script.

## Dependencies  
GrooveSweeper relies upon lyricsgenius by John Miller (https://github.com/johnwmillr/LyricsGenius). This will be automatically downloaded when you execute the run.py script for the first time. Otherwise it is available on PyPI and can be downloaded with `pip install lyricsgenius`  

## Development Information  
Original Code by Elise Kulka, Jane Li, Phillip Smith, Jack Yannes, and James Young  
Developed and Tested in Windows 10 | Version 2.0
