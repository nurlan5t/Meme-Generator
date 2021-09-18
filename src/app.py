"""Create an application package to generate a random meme."""

import random
import os
import requests
from flask import Flask, render_template, request, abort

# Import our Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine
import random

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # ELABORATE: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme.

    Use the random python standard library class to:
    :param img - select a random image from imgs array
    :param quote - select a random quote from the quotes array
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    :param image_url - Get url of the image from html file
    :param quote_body - Get quote message from html file
    :param quote_author - Get author's name from html file
    Extract image from html through user inputs and save in
    a temporary folder. Use this temporary path,
    quote_body, quote_author as inputs to create
    a meme object. Delete the temporary folder.
    """
    image_url = request.form.get('image_url')
    quote_body = request.form.get('body')
    quote_author = request.form.get('author')

    r = requests.get(image_url)
    tmp_img = f'./{random.randint(0,10000)}_tmp.jpg'
    open(tmp_img, 'wb').write(r.content)

    path = meme.make_meme(tmp_img, quote_body, quote_author)
    os.remove(tmp_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
