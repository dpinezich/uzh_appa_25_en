from PIL import Image
tuxIm = Image.open('tux.png')
tuxIm.rotate(90).save('rotated90.png')
tuxIm.rotate(180).save('rotated180.png')
tuxIm.rotate(270).save('rotated270.png')

tuxIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
tuxIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')