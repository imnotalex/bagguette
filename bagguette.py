#import image module
from PIL import Image as bagguette
import os

imagebayby = "36839.jpg"
ime = bagguette.open(imagebayby)

#infinite loop variable
loop = 0
#number of times (test mode only)
verycoolinput = input("how many times should bagguette(this is only a test node fature)")
print(type(verycoolinput))
verycoolinput = int(verycoolinput)
print(type(verycoolinput))
#loop
while(loop <= verycoolinput):
  loop = loop + 1
  #show image
  ime.show()
  
        
#thats all the code bitch
