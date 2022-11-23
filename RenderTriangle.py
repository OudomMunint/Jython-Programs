#Paints triangle on picture then explore

#get file > make pic
def getFile():
   #Pick a file and make the file into a picture then returns it
   file = pickAFile()
   pic = makePicture(file)
   return(pic)

#The rectangle will start and end with the following coordinates: 25,80,150,95         
def bigRectangle(pic):
   #Starting and ending coordinates
   startX = 25 
   startY = 80
   endX = 150
   endY = 95
   #Lets user pick a color
   color = pickAColor()
   
   #For loop that draws the rectangle on the picture   
   for x in range(startX, endX):
      for y in range(startY, endY):
         pix = getPixel(pic, x, y)
         setColor(pix, color)
   #Repaints the original picture      
   repaint(pic)
    
def runProgramme(pic):
   #Calling task 1
   task1 = getFile()
   #Calling task 2
   task2 = bigRectangle(task1)
   #repaints task 1
   repaint(task1)
   #Explore the picture
   explore(task1)
   
#Is longer but is better for user interaction   
def makeShape2():
   #pick a file then make it a picture 
   file = pickAFile()
   pic = makePicture(file)
   
   #request inpute from user for coordinates
   startX = requestInteger("enter sth")
   startY = requestInteger("enter sth")
   endX = requestInteger("enter sth")
   endY = requestInteger("enter sth")
   #request color from user
   color = pickAColor()
   
   #Repaints the picture using user selected color and user entered coordinates
   for x in range(startX, endX):
      for y in range(startY, endY):
         pix = getPixel(pic, x, y)
         setColor(pix, color)     
   repaint(pic)
   
#Another way of doing it
#Shorter, more efficient but does not have a user interface, less desireable for user interaction   
def makeShape3(pic, startX, endX, startY, endY, colour):
   #Pick a file and make the file into a picture
   file = pickAFile()
   pic = makePicture(file)
   #For loop that draws the rectangle with user entered coordinates and user picked colors
   for x in range(startX, endX):
      for y in range(startY, endY):
         pix = getPixel(pic, x, y)
         setColor(pix, colour)
   repaint(pic)
   
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

   
  
         
         
   
   

