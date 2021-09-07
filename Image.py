from PIL import Image, ImageDraw
import base64
from io import BytesIO

class Image__:
    # bg -> background color
    # tc -> text color
    # tposx -> text position x
    def __init__(self, bg, tc, width, height, text, tposx, tposy) -> None:
        self.bg = bg
        self.tc = tc
        self.width = width
        self.height = height
        self.text = text
        self.tposx = tposx
        self.tposy = tposy
    
    def __draw(self) -> Image:
        i = Image.new("RGB", (self.width, self.height), self.bg)
        img = ImageDraw.Draw(i)
        img.text((self.tposx, self.tposy), self.text, fill=self.tc)
        return i

    # return base64 representation of the image
    def base64(self):
        img = self.__draw()
        try:
            buffer = BytesIO()
            img.save(buffer, format="JPEG")
            imgb64 = base64.b64encode(buffer.getvalue())
            return imgb64
        except Exception as e:
            print(e)
            return "error"
