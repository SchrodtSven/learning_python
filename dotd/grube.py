fh = open('foo.txt', 'r')
data = fh.read()

lines = data.split('\n')
for line in lines:
    i = line.split()
    print (i)



#print(type(data), data)