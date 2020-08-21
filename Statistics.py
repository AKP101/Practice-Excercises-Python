import statistics
example_list = [1,2,3,4,5,6,7,10]
x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.stdev(example_list)
a = statistics.mode(example_list)
b = statistics.variance(example_list)
print("mean:", x)
print("median:", y)
print("std-dev:", z)
print("mode:", a)
print("variance:", b)
