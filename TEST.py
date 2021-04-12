listA = [99, 100, 102, 78, 150, 102, 59, 200, 1000]

fil_end = filter(lambda x:x>100, listA)

map_end = map(lambda x: x * 2, list(fil_end))

print(list(map_end))
