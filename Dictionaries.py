exDict = {"Jack":15, "Bob":22, "Alice":12, "Kevin":17}
print(exDict)

print(exDict['Jack']) #Jack is the key and the
#associated value for that is Jack's age. 
exDict['Tim'] = 14

print(exDict)
exDict["Tim"] =15

print(exDict)
del(exDict["Tim"])

print(exDict)

newExDict={
    "Jack":[15, "blonde"], "Bob":[22,"brown"],
    "Alice":[12, "black"], "Kevin":[17, "red"]
    }
print(newExDict["Jack"])
print(newExDict["Jack"][1])
