# writing and appending to a file are different. writing poverwrites and appending adds

text = "Sample Text to save\nA new Line!"
saveFile = open("exampleFile.txt", "w") # open a new file to overwrite to it.
saveFile.write(text)

saveFile.close()
