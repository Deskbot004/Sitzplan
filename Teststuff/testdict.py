dict ={}

for x in range(10):
    dict[10-x] = "A" + str(x)

for x in dict:
    print(x)
    print(dict[x])
print(dict)
print("test")