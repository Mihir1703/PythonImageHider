import PIL.Image
import io
filename = "extracted.png"
origin_file = "india.jpg"

with open(origin_file,'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset+2)

    new_img = PIL.Image.open(io.BytesIO(f.read()))
    new_img.save(filename)