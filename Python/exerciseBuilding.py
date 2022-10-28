# method 1
for i in range(0, 20):
    if i != 13: print(i)

# method 2
i=20
while True:
    i -= 1
    if i == 0:
        break
    elif i != 13:
        print(i)
        continue