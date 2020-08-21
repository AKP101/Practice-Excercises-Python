x = [6,4,3,2,5,76,8,8,6,4,2,1,123,4,2,1,3,4,5,6]
y = ["Janet", "Jessie", "Bobby", "Alice", "Kelly"]

x.append(2) #append a value to the list
x.insert(0,2)# insert 2 into index of 0 (it will append itself at that location)it does not replace!
x.remove(2) #removes the first 2
x.remove(x[2])#removes the third element
print(x.index(3))#tells you where the first 3 is (in our case after all the operations it should be 15)
print(x.count(6))#how many 6
print(x)
x.sort()# sort x
print(x)
y.sort()
print(y)
