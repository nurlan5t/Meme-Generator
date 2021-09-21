"""A library to generate memes."""

from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeEngine():
    """Create a meme and save it in the output folder."""

    def __init__(self, out_path: str):
        """Initialize meme object with user-defined \
        output path to save the meme."""
        self.out_path = './tmp'

    def make_meme(self, img_path: str,
                  text=None, author=None, width=500) -> str:
        """Resize the input image to a max width of 500 pixels \
        while maintaining the aspect ratio. Draw message \
        quote and author onto the meme.

        :param img_path = Path which contains the meme image
        :param text = Message quote to be written on the image
        :param author = Message's author to be written on the image
        """
        with Image.open(img_path) as img:

            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

            if text is not None and author is not None:
                complete_msg = f'{text}\n- {author}'
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('calibri.ttf', size=30)
                txt = draw.text((10, 20), complete_msg, font=font, fill='red')

            final_out_path = self.out_path +\
                f'/{randint(0,10000)}_out.jpg'
            img.save(final_out_path)
            return final_out_path
