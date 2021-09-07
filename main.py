"""
    draw an image with given background color, text color etc.
    uses Python Image Library (PIL) to draw images, and 
    bottle as the web server.

    TODO
        font selection
        shapes
        background images
        ...
"""
from PIL import ImageColor
from bottle import run, get, post, template, request, HTTPResponse
from Image import Image__

@get("/")
@post("/")
def index():
    if request.method == "POST":
        try:
            bg = hex_to_rgb(request.forms.get("bg"))
            text_color = hex_to_rgb(request.forms.get("tc"))
        except Exception as e:
            body = template("error.html", error=e, status_code=400)
            return HTTPResponse(body=body, status=400)
        try:
            width = int(request.forms.get("width"))
            height = int(request.forms.get("height"))
            tposx = int(request.forms.get("tposx"))
            tposy = int(request.forms.get("tposy"))
        except Exception as e:
            body = template("error.html", error="check your inputs", status_code=400)
            return HTTPResponse(body=body, status=400)

        text = request.forms.get("text")
        base64 = draw_image(bg, text_color, width, height, text, tposx, tposy)
        print(base64)
        return template("success.html", imgb64=base64)

    return template("index.html")

def draw_image(bg, tc, w, h, text, tposx, tposy) -> str:
    image = Image__(bg, tc, w, h, text, tposx, tposy)
    return image.base64()

def hex_to_rgb(hex) -> str:
    if hex[0] != "#":
        raise Exception("invalid hex")
    return ImageColor.getcolor(hex, "RGB")

def main():
    run(host="localhost", port=8000)

if __name__ == "__main__":
    main()