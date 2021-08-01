from PIL import Image

image = Image.open('<IMAGE FILE HERE>')

data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save('<NEW FILE WITH CLEANED DATA NAME HERE>')
