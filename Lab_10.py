def blendPic(xstart, ystart, proportion):

   file1 = pickAFile()
   pic1 = makePicture(file1)
   
   file2 = pickAFile()
   pic2 = makePicture(file2)
   
   
   for x in range(0, getWidth(pic2)):
      for y in range(0, getHeight(pic2)):
         
         pix1 = getPixel(pic1, xstart + x, ystart + y)
         pix2 = getPixel(pic2, x, y)
   
         newRed = getRed(pix1) * proportion / 100 + getRed(pix2) * (100 - proportion) / 100
         newGreen = getGreen(pix1) * proportion / 100 + getGreen(pix2) * (100 - proportion) / 100
         newBlue = getBlue(pix1) * proportion / 100 + getBlue(pix2) * (100 - proportion) / 100
         newColour = makeColor(newRed, newGreen, newBlue)
   
         setColor(pix1, newColour)
   repaint(pic1)
   
def luminance():
   file = pickAFile()
   pic = makePicture(file)
   pix = getPixel(pic, 2, 289)
   r = getRed(pix)
   g = getGreen(pix)
   b = getBlue(pix)
   newColor = (r + g + b) / 3
   setColor(pix, newColor)
   repaint(pic)
   explore(pic)
   
   
   
   
def greyScale():
   file1 = pickAFile()
   pic1 = makePicture(file1)
   myPixel = getPixels(pic1)
   for pix in myPixel:
      greyVal = (getRed(pix)) + (getGreen(pix)) + (getBlue(pix)) / 3
      setRed(pix, greyVal)
      setGreen(pix, greyVal)
      setBlue(pix, greyVal)
   
   r = getRed(pix)
   g = getGreen(pix)
   b = getBlue(pix)
   newColor = makeColor(((r + g + b) / 3))
   setColor(pix, newColor)
      
   repaint(pic1)
   explore(pic1)

    