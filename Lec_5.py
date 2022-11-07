#Author: Dom 
#date: 22/07/2019
#Task:
#T1:getFile(): Get a file, make picture then return picture
#T2:makeShape(Pic): Draw a rectangle with a colour that is selected by a user
#Location 150,80,25,95
#T3: Call task 1 and the task 2 and repaint picture and explore picture
#T4: This calls makeShape(picture, startX, endX, startY, endY, colour)

#T1
#This task Lets you pick a file and make the file into a picture
#Then returns the picture
def getFile():
   #Pick a file and make the file into a picture then returns it
   file = pickAFile()
   pic = makePicture(file)
   return(pic)
         
#T2
#This task draws a rectangle with a user selected color on the picture
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
   
#T3
#This task runs task 1 and task 2 in conjunction with only 1 function   
def runProgramme(pic):
   #Calling task 1
   task1 = getFile()
   #Calling task 2
   task2 = bigRectangle(task1)
   #repaints task 1
   repaint(task1)
   #Explore the picture
   explore(task1)
   
   
#T4
#This is one way of doing task for.
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
   
#This is another way of doing task 4
#Shorter, more efficient but does not have a user interface
#less desireable for user interaction   
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
   
   

   
  
         
         
   
   

