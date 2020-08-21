
#import statistics as s
#x = s.mean(example_list) #now you don't need to type our statitics just 's'
#can also do what is below
#from statistics import *
#x = mean(example_list)
#y = variance(example_list)

from statistics import mean as m, variance as v

example_list = [1,2,3,4,5,6,7,10]
x = m(example_list)
y = v(example_list)




print("Mean:", x)
print("Variance:", y)
