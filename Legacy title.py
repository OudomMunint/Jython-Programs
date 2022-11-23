#adds text to image
def text():
   newPic = makeEmptyPicture(400, 400, red)
   newPic2 = makeEmptyPicture(200, 200, white) 
   textColor = pickAColor()
   addText(newPic2,90,90,"Dom", textColor)
   xstart = 150
   ystart = 50
   
   for x in range(0, getWidth(newPic2)):
      for y in range(0, getHeight(newPic2)):
         pix1 = getPixel(newPic, xstart + x, ystart + y)
         pix2 = getPixel(newPic2, x, y)
        
         pix1Color = getColor(pix1)
         pix2Color = getColor(pix2)
         
   if pix2Color == white:
      setColor(pix1,pix1Color)
          
   else:
      setColor(pix1,textColor)
   show(newPic)
