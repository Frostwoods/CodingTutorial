# python functional programming

# list comprehension

# lambda map filter
# sorted reversed zip enumerate

# itertools functools collections operator
# numpy pandas scipy

a = ['1', '2', '3', '6', '7', '8']

print(list(map(int, a)))
print(list(map(eval, a)))

print(eval("1+1"))


a = [-1, 2, 3, -4]
f = lambda x: x**2
print([f(i) for i in a])


print([abs(i) for i in a if i < 0])

print(list(filter(lambda x: x < 0, a)))

a = [-1, 2, 3, -4]
b = [4, 3, 2, 1]
c = list(zip(a, b))
print(max(c, key=lambda x: x[0]))

print(sorted(a))
print(sorted(a, reverse=True))
print(sorted(a, key=lambda x: abs(x)))

for index, value in enumerate(a):
    print(index, value)

print([[index, value] for index, value in enumerate(a)])

kk = {index: value for index, value in enumerate(a)}
print(kk)

a = 'a'
print(isinstance(a, int))
assert isinstance(a, int)
