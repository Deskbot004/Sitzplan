dictionary ={}

for x in range(10):
    dictionary[str(10-x)] = "A" + str(x)

for x in dictionary:
    print(x)
    print(dictionary[x])
print(dictionary)
print("test")


dictionary = {int(k):v for k,v in dictionary.items()}
dictionary = dict(sorted(dictionary.items()))
dictionary = {str(k):v for k,v in dictionary.items()}

print(dictionary)
print(str("hi"))