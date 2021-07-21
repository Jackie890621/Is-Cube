x1, y1 = input("Please input coordinate: ").split()
x2, y2 = input("Please input coordinate: ").split()
x3, y3 = input("Please input coordinate: ").split()
x4, y4 = input("Please input coordinate: ").split()

x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
x4 = int(x4)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)
y4 = int(y4)

a = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
b = (x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)
c = (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)
d = list()
d.append(a)
d.append(b)
d.append(c)
d.sort()

if (d[0] == d[1] and d[2] == d[0] + d[1]):
    print("Square!!")
else:
    print("Not a Square!!")
