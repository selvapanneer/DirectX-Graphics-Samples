# Generates 256 sample resolved images
import os, numpy, PIL
from PIL import Image

for frameNo in range(256):
    imlist=[]
    for i in range(256):
        path =  "c:/temp/data/"
        path += str(i)
        path += "/"
        path += str(frameNo)
        path += ".png"
        imlist.append(path)
    
    print ("frame no ", frameNo)

    # Assuming all images are the same size, get dimensions of first image
    w,h=Image.open(imlist[0]).size
    N=len(imlist)

    # Create a numpy array of floats to store the average (assume RGB images)
    arr = imarr=numpy.array(Image.open(imlist[0]).convert('RGB'),dtype=numpy.float64)

    # Build up average pixel intensities, casting each image as an array of floats
    for i in range(1,255,1):
        imarr=numpy.array(Image.open(imlist[i]).convert('RGB'),dtype=numpy.float64)
        arr = arr + imarr
    
    arr = arr / N

    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

    # Generate, save and preview final image
    out=Image.fromarray(arr,mode="RGB")
    output = "c:/temp/data/256MSAA/"
    output += str(frameNo)
    output += ".png"
    out.save(output)
    #out.show()