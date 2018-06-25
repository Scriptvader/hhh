# Word Crawler Server

*This is a simple web crawler searches multiple web pages for string occurrences.*

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/boxpositron/word_crawler)

## Installation

Be sure to install the requirements for this project located in the **requirements.txt** file.

You can run the following command to perform the installation with *pip*

    pip install -r requirements.txt

## Starting the application

    Windows
    set FLASK_APP=main.py

    Unix
    export FLASK_APP=main.py

Then run the command below to start the application

    flask run

## Performing a search

After initializing the application, open your browser and go to the address provided on in your terminal.

### Testing the server

By default the address is

    http://localhost:5000/

The response after opening this url should be

    {
        "message": "Application running",
        "status": "success"
    }

If this does not show up , please check your installation.

### Query syntax

In order to perform a search, you must specify the following parameters

    term
    url

The term is the string you are searching for and the url is the website you want to run the crawler on


### Example


    http://localhost:5000/search?term=google&url=http://google.com


Running this should give the following response format

    {
        "action": "search",
        "result": [
            {
                "frequency": 40,
                "url": "http://google.com"
            }
        ],
        "status": "success"
    }