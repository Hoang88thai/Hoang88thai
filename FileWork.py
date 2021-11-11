# Reading data from the file

obj = open("E:\PY.txt",'r')

# read all data from the file
# print(obj.read())

# read 1 line from file
#print(obj.readline()) # call first time, it reads the first line
#print(obj.readline()) # call second time, it reads the second line

# Read only a few characters from the file
print(obj.read(10)) # read the first 10 characters



