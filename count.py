a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
c = ['z', 'x', 'y', 'k']

n = 0

for x, y, z in zip(a, b, c):
    if x != y or x != z:
        n += 1
    elif y != z:
        n += 1

print(n)