Meme_generator
Udacity Intermediate Python Nanodegree Project

In this project, we will build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. There are a variety of quotes saved in different file types, we will create a generic solution using Python to load quotes from each file.

Overview
At a high level, the application which will be built will perform the following:

Interact with a variety of complex filetypes.
Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
Load, manipulate, and save images.
Accept dynamic user input through a command-line tool and a web service.
This project will extensively revolve around the concepts of importing modules, abstract classes, inheritances, usage of Python packages, command line interface (CLI) & Flask App.

Description of Datasets
This repo includes many folders which are described as below:

_data: Has 2 sub-folders - SimpleLines & DogQuotes. They contain a variety of files of different formats(csv,docx,pdf,txt). Each of these files contain a bunch of quotes along with their author names. We need to extract each quote line-by-line from these files.
templates: Contains HTML template files which will be used as web service interaction
Description of Modules
QuoteEngine: This module is responsible for ingesting many types of files that contain quotes. This contains an abstract base class, IngestorInterface, which is realized by separate strategic objects (aka helper classes) for each file type. A final Ingestor class that realizes this abstract base class & encapsulates all our helper classes. It also contains a QuoteModel class which stores the "message body or quote" & its corresponding "message author" once the quotes are parsed/extracted from different file types using our helper classes. Helper classes include : CSVIngestor,TXTIngestor,PDFIngestor,DocxIngestor .
MemeEngine: This module is responsible for manipulating and drawing text onto images. This contains a MemeEngine class which will load an image, resize it to a width of 500 pixels atmost, while maintaining the aspect ratio. It will add the quote body & quote author on top of the image. The final manipulated image will be a meme which will be saved in an output folder
Each of the above modules will also contain an "init.py" file which allows interaction between submodules within the main module.

Package our Application
meme.py
Create a CLI tool that is invoked by "meme.py" script. The script returns a path to a generated image that is generated using Quote Engine & Meme Engine modules.
If any argument is not defined, a random selection is used from the default dataset folder i.e _data.
The script must take three optional CLI arguments:
--body : a string quote body
--author : a string quote author
--path : an image path
app.py
Create a Flask app that interacts with the web service.
The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.
It also fetches an image from a user submitted URL, with the help of requests package in Python
Output Folders
Sample output images or memes were generated after running the scripts - "app.py" & "meme.py" , and were stored in below folders.

tmp: Will store the output images aka memes from CLI terminal when "meme.py" script is run
static: Will store the output images aka memes generated from web service when "app.py" script is run
Requirements.txt
This file contains the complete list of python dependencies used throughout this project