def example():
    print("Basic function")
    z = 3+9
    print(z)


example()

print()
print()


def simple_addition(num1, num2):
    ans = num1 + num2
    print("num1 is ", num1)
    print(ans)


simple_addition(5, 3)

print()


def example2(num1, num2=5):
    return num1+num2


print(example2(33))
