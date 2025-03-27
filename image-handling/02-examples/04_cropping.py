from PIL import Image
tuxIm = Image.open('tux.png')
croppedIm = tuxIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

