import PIL.Image
import PIL.ExifTags


img = PIL.Image.open('<IMAGE FILE HERE>')
""" exif_data = img._getexif() """
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

print(exif)
