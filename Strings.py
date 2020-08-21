msge = """Bobby's world was a good
cartoon in the nineties"""
msg = "Hello World"
print(msg)
print(len(msg))
print(msg[0])
print(msg[0:5])  # including 0 and upto but not including 5th index
print(msg[:5])  # 0 to 5
print(msg[:])
print(msg[6:])
print(msg.lower())
print(msg.upper())
print(msg.count("l"))
print(msg.find("W"))
print(msg.find("w"))  # Doesn't exist
newMsg = msg.replace("World", "Universe")  # if you wanted to have message be equal to Universe
# you can do so by putting msg = msg.replace("World", "Universe")
print(newMsg)
print(msg + ". Or " + newMsg)
finalMsg = "{}. Or {}.".format(msg, newMsg)
# one could also use finalMsg = f"{msg}. Or {newMsg //(could use .upper if you wanted to)}.
print(finalMsg)
print(help(str.lower))
