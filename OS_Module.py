
import os
curDir = os.getcwd() #checks what your current directory is.

print(curDir)

os.mkdir("newDir") #makes a new directory
import time
time.sleep(2) #Gives ya 2 seconds to pause before changing name. 
os.rename("newDir","NewDirectory") #Changes prevname to this
time.sleep(2)
os.rmdir("NewDirectory")#removes NewDirectory

help(os)
