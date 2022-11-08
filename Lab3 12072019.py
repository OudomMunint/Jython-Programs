def greyScale():
   file1 = pickAFile()
   pic1 = makePicture(file1)
   myColor = pickAColor()
   print(myColor)
   myPixel = getPixel(pic1, 212, 83)
   setColor(myPixel, myColor)
   explore(pic1)
   
def negetivePic():
   file1 = pickAFile()
   pic1 = makePicture(file1)
   pixels = getPixels(pic1)
   for pix in pixels:
      setRed(pix, 255 - getRed(pix))
      setGreen(pix, 255 - getGreen(pix))
      setBlue(pix, 255 - getBlue(pix))
   show(pic1)
   
def changePixel():
   file1 = pickAFile()
   pic1 = makePicture(file1)
   myRed = getRed(pix)
   newColour = makeColor(myRed, myGreen, myBlue)
   setColor(pix, myColor)
