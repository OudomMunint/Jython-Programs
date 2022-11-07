#Author: Pannha Oudom Munint
#date:8/7/2019
#T1: open picture file, make file a picture and show the picture
#T2: get the data about pixels
#T3: Get the value of a pixel and return it
#T4: pick a file then call the required function

#T1
def openShowPicture():
   #select file
   file1 = pickAFile()
   #print name and location
   print (file1)
   #make selected file into picture
   pic1 = makePicture(file1)
   #Display picture
   show(pic1)
   
#T2
   #gets the pixel of the picture and shows in R,G,B
   pixel1 = getPixel(pic1, 32, 32)
   #Prints the value of the pixels
   #print pixel1
   #retuen the value of the pixels
   return(pixel1)
#T3
#get the value of a pixel and return it   
def showPixelUser(fileName, x, y):
    myPicture = makePicture(fileName)
    pixel1 = getPixel(myPicture, x, y)
    #return the value of the pixel to the calling function
    return(pixel1)
    
    
#T4
#Pick a file and call functions
def getAFile():
   file = pickAFile()
   
   #call T1: show picture
   #showPicture(file)
   
   #Call T2 = show value of pixel
   #pixelValue = showPixel(file)
   #print(pixelValue)
   
   #call T3: give the file, x and y locations
   #user enters the x and y values foe that picture
   x = requestInteger("enter x of picture")
   y = requestInteger("enter y of picture")
   pixelValue = showPixelUser(file, x, y)
   
   #get the value of the red of the pixel
   myPixelRed = getRed(pixelValue)
   #print the pixel value of the picture choosen
   print(myPixelRed)
   #print(pixelValue)
   
   setColor(pixelValue, yellow)
   myPixelRed = getRed(pixelValue)
   print(myPixelRed)
   
   


   