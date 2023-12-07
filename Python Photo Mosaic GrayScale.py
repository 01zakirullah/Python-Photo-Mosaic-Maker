
import Image


##################Variables#################################################

#size of  image array OR number of pictures in the collection folder
size= 100

#size of cropped image and the size of the collection images after loading
cropSize=10

#a certain threshold is kept while comparing the luminances
thresh=18

# Initializing Arrays
collection = [Image]*size
averages = [0.0]*size



###################Utility Functions###########################################


# gets the lumosity(luminance) of the average color
def getLumosity(image):
    (width,height)=image.size
    lum=0.0
    counter =0
    for x in range (height-1):
        for y in range (width-1):
            lum= image.getpixel((y,x))
            counter = counter+1
    return lum;

  
# compares the given color with collection images and returns the index of the collection
def compareColor( col, threshold ):
    for x in range (size):
        if (abs(averages[x]-col)<threshold):
            #print col,"  was not found so we sorted this  ",avg[x]
            return x




###########################Loading Collection Images and Storing their Averages############################



# opening and loading the collection images in an array
for x in range (size):
    collection[x] = Image.open("./Collection/collection (%d).jpg" %x)
    collection[x] = collection[x].convert("L")#converts to gray scale
    averages[x] = getLumosity(collection[x])#stores the average lumosity
    collection[x].thumbnail((cropSize,cropSize), Image.NEAREST)#shrinks the size of every collection image after storing its average luminance
    
averages.sort()
#makes it simpler to find a stored average while comparing the average luminance
print  "Averages Array = ",averages



################################### Loading Input Image###########################################


inputimg = Image.open("./InputOutput/input.jpg")
#fimg.thumbnail((400,400), Image.NEAREST)#you can shrink the size of the input image
#
inputimg.show()#shows input image after loading it.
inputimg=inputimg.convert("L")
inputimg.show()#shows input image after converting to Gray Scale
#
(width,height) = inputimg.size
print "Final imge's dimensions",width,"  ",height




#######################Main Function###########################


#####Function that builds the Mosaic
def createMosaic():
    for x in range((height)/cropSize):
       for y in range((width)/cropSize):
            box= ((y)*cropSize,   (x)*cropSize,    (y+1)*cropSize,    (x+1)*cropSize)
            #print box
            offset= (y*cropSize,  x*cropSize)
            i= inputimg.crop(box)
            i.save("i2.jpg")
            (cwidth,cheight) = i.size
            #print "CropImageWidth",cwidth,"  CropImageHeight",cheight
            cColor = getLumosity(i)
            index=compareColor(cColor,thresh)
            inputimg.paste(collection[index],offset)
            

##### Calling the function
createMosaic()

inputimg.show()
inputimg.save("InputOutput/Final Image.jpg")

