"""Create a library that loads data from Docx files.

A 'DocxIngestor' class will parse the Docx file and extract
message body and author, using them to return a collection of
concrete class objects.
"""

from .IngestorInterface import IngestorInterface
from typing import List
import docx
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Loads and parses data from Docx files.

    :param allowed_extensions - Look for file extension 'docx'.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the data from Docx file and return \
        a collection of 'Quotes' class objects.

        :param path: Directory of the input file
        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                meme_msg = QuoteModel(str(parse[0]), str(parse[1]))
                quotes.append(meme_msg)

        return quotes
