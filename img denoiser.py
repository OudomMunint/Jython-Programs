#Dev: Pannha Oudom Munint, L1 SWE
#Opens a picture file, makes file a picture then showing the picture, gets the data about pixels, gets the value of a pixel and return it.
#Use: pick a file then call the required function


def openShowPicture():
   #select file
   file1 = pickAFile()
   #print name and location
   print (file1)
   #make selected file into picture
   pic1 = makePicture(file1)
   #Display picture
   show(pic1)
   

   #gets the pixel of the picture and shows in R,G,B
   pixel1 = getPixel(pic1, 32, 32)
   #Prints the value of the pixels
   #print pixel1
   #retuen the value of the pixels
   return(pixel1)

#get the value of a pixel and return it   
def showPixelUser(fileName, x, y):
    myPicture = makePicture(fileName)
    pixel1 = getPixel(myPicture, x, y)
    #return the value of the pixel to the calling function
    return(pixel1)
    
    

#Pick a file and call functions
def getAFile():
   file = pickAFile()
   
   #call: show picture
   #showPicture(file)
   
   #Call = show value of pixel
   #pixelValue = showPixel(file)
   #print(pixelValue)
   
   #call: give the file, x and y locations
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
   
   


   