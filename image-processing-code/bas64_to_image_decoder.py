import serial
import time
import base64
import io
from PIL import Image
import binascii

fixed_base64_str = "put the Base64 text of image here"
image_bytes = base64.b64decode(fixed_base64_str)

with open("extra.png", "wb") as f:
    f.write(image_bytes)
