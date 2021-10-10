import PIL.Image
import io
toHide = 'hd.png'

img = PIL.Image.open(toHide)
byte_arr = io.BytesIO()
img.save(byte_arr,format=toHide.split('.')[1].capitalize())

with open('india.jpg','ab') as f:
    f.write(byte_arr.getvalue())