#Author:Dom
#Date:29/07/19
#Task:

def mirror(picture):
   pic = makePicture(pickAFile())
   width = getWidth(pic)
   height = getHeight(pic)
   print(width)
   print(height)
   mirrorPoint = width / 2
   for y in range(0, getHeight(pic)):
      for x in range(0, mirrorPoint):
         left = getPixel(pic, x, y)
         right = getPixel(pic, width - x - 1, y)
         setColor(right, getColor(left))
   repaint(pic)
   

def blendPic(pic1, pic2, startX, startY, proportion):
   pic1 = makePicture(pickAFile())
   pic2 = makePicture(pickAFile())
   for x in range(0, getWidth(pic2)):
      for y in range(0, getHeight(pic2)):
         pix1 = getPixel(pic1, startX + x, startY + y)
         pix2 = getPixel(pic2, x, y)
         
         newRed = getRed(pix1) * proportion / 100 + getRed(pix2) * (100 - proportion) / 100
         newGreen = getGreen(pix1) * proportion / 100 + getGreen(pix2) * (100 - proportion) / 100
         newBlue = getBlue(pix2) * proportion / 100 + getBlue(pix2) * (100 - proportion) / 100
         newColor = makeColor(newRed, newGreen, newBlue)
         setColor(pix1, newColor)
   repaint(pic1)