#Pick a file then make a picture then colors a rectangle red in the picture

def getFile():
   file = pickAFile()
   pic = makePicture(file)
   show(pic)

def bigRectangle():
   file2 = pickAFile()
   pic2 = makePicture(file2)
   startX = 100 
   startY = 100
   endX = 200
   endY = 200     
   for x in range(startX, endX):
      for y in range(startY, endY):
            pixel = getPixel(pic2, x, y)
            setColor(pixel, red)
   repaint(pic2)