from PIL import Image
tuxIm = Image.open('tux.png')
tuxCopyIm = tuxIm.copy()

faceIm = tuxIm.crop((335, 345, 565, 560))
#faceIm.size
tuxCopyIm.paste(faceIm, (0, 0))
tuxCopyIm.paste(faceIm, (400, 500))
tuxCopyIm.save('pasted.png')