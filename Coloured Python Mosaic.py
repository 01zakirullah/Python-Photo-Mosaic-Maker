import Image
import math

##################Variables#################################################

#size of  image array OR number of pictures in the collection folder
size= 100

#size of cropped image and the size of the collection images after loading
cropSize=10

#a certain threshold is kept while comparing the luminances
thresh=18

# Initializing Arrays
collection = [Image]*size
averages = [[0 for x in range(3)] for x in range(size)]
rgbArr=[0]*3




#######################UTILITY FUNCTIONS###############################3


#returns the average color's r,g,b values in a 1dimensional array
def getAverageColor(image):
    (width,height)=image.size
    red=0
    green=0
    blue=0
    counter =0
    for x in range (height-1):
        for y in range (width-1):
            (r,g,b)= image.getpixel((y,x))
            red = red + r
            green = green + g
            blue = blue + b
            counter = counter+1
    color = [0]*3       #rgb array
    red = red/counter
    green = green/counter
    blue = blue/counter
    color[0]=red
    color[1]=green
    color[2]=blue
    return color

  
## compares the given color with collection images using Euclidean color difference formula
        
def compareColor( col, threshold ):
    for x in range (size):
        if ( (math.sqrt((averages[x][0]-col[0])**2 + (averages[x][1]-col[1])**2 + (averages[x][2]-col[2])**2)) < threshold):
            #print (math.sqrt((averages[x][0]-col[0])**2+(averages[x][1]-col[1])**2+(averages[x][2]-col[2])**2))
            return x

# If you want to calculate the percentage comparison using Euclidean Difference
#d=(math.sqrt((averages[x][0]-col[0])**2+(averages[x][1]-col[1])**2+(averages[x][2]-col[2])**2))
#p=d/math.sqrt((255)^2+(255)^2+(255)^2)#percentage 



###########################Loading Collection Images and Storing their Averages############################



# opening and loading the collection images in an array
for x in range (size):
    collection[x] = Image.open("./Collection/Collection (%d).jpg" %x)
    collection[x].thumbnail((cropSize,cropSize), Image.NEAREST) #shrinks the size of every collection image after storing its average
    collection[x]=collection[x].convert('RGB')
    rgbArr = getAverageColor(collection[x])
    averages[x][0]=rgbArr[0]
    averages[x][1]=rgbArr[1]
    averages[x][2]=rgbArr[2]
   

############################Sorting Calculated Averages##############33

averages.sort()
print  "Averages = ",averages

    
##############################Input Image###############

inputimg = Image.open("./InputOutput/input.jpg")
inputimg=inputimg.convert("RGB")
(width,height) = inputimg.size
print "Final image's dimensions",width,"  ",height

inputimg.thumbnail((750,750),Image.NEAREST)
inputimg.save("final.jpg")

inputimg.show()

## ##########################3Creating the Mosaic#####################
def createMosaic():
    for x in range((height)/cropSize):
       for y in range((width)/cropSize):
            box= ( y*cropSize, x*cropSize,    (y+1)*cropSize,    (x+1)*cropSize)
            #print box
            offset= (y*cropSize,    x*cropSize)
            crim= inputimg.crop(box)
            crim.save("part.jpg")
            cColor=[0,0,0]
            cColor = getAverageColor(crim)
            index=compareColor(cColor,thresh)
            #im[index].show()
            if (index!=None):
                inputimg.paste( collection[index] , offset )



createMosaic()   
inputimg.show()
inputimg.save("InputOutput/Final Image.jpg")

