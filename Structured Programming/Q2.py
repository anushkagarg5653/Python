x = lambda z: 2*(z[0]+z[1])+z[2]
y = [(3,5,2), (7,10,2), (81,16,3)]
result = map(x,y[::1])
print(list(result))