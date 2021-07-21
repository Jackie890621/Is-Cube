x = list()
y = list()
z = list()
dist = list()

f = open("test.txt", "r")
case = f.readlines()
f.close()

for i in range(8):
    temp = case[i].split(' ')
    x.append(int(temp[0]))
    y.append(int(temp[1]))
    z.append(int(temp[2]))

for i in range(8):
    for j in range(i + 1, 8):
        temp = (x[j] - x[i]) * (x[j] - x[i]) + (y[j] - y[i]) * (y[j] - y[i]) + (z[j] - z[i]) * (z[j] - z[i])
        dist.append(temp)
dist.sort()

flag = 1
for i in range(1, len(dist)):
    if (i <= 11):
        if (dist[i] != dist[i - 1]):
            flag = 0
            break
    elif (i <= 23):
        if (dist[i] != 2 * dist[0]):
            flag = 0
            break
    else:
        if (dist[i] != 3 * dist[0]):
            flag = 0
            break

if (flag):
    print("It's a Square!!!")
else:
    print("It's not a Square!!!")
    
