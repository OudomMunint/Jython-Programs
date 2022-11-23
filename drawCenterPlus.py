#Use: Draws a cross in the centre of the picture, replace cross with watermark

def centrePlus():
      #Tells the user to pick a file
      file1 = pickAFile()
      #Makes the choosen file into a picture
      pic1 = makePicture(file1)
      #Gets the Width and Height of the picture and devide it by 2
      #Makes the 2 triangles cross and the middle of the picture
      midx = getWidth(pic1) / 2
      midy = getHeight(pic1) / 2
      #For loop that draws the vertical triangle in green
      for y in range(midy - 75, midy + 75):
         for x in range(midx - 10, midx + 10):
            pixel = getPixel(pic1, x, y)
            #set color of the triangle to green
            setColor(pixel, green)
      #For loop that draws the horizontal triangle in cyan      
      for x in range(midx - 75, midx + 75):
         for y in range(midy - 10, midy + 10):
            pixel = getPixel(pic1, x, y)
            #set color of the triangle to green
            setColor(pixel, cyan)
      #Repaints and show the picture      
      repaint(pic1)