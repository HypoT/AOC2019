data = '382345-843167'

rng = [*map(int, data.split('-'))]

#Part1

options = set()
for i in range(*rng):
    i = str(i)
    if list(i) != sorted(i): continue
    for j in range(len(i) - 1):
        if i[j] == i[j+1]:
            options.add(i)


print(len(options))


#Part2

doubles = set()
for i in options:
    count = 0
    for j in range(1, len(i) - 2):
        if i[j] == i[j+1] and i[j] not in  (i[j-1], i[j+2]):
            doubles.add(i)

    if i[0] == i[1] and i[0] != i[2]:
        doubles.add(i)
    if i[-1] == i[-2] and i[-1] != i[-3]:
        doubles.add(i)


print(len(doubles))
