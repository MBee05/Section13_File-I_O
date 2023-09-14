# my_file=open('test.txt')
# print(my_file)

# output <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>

# to access the file
# print(my_file.read())
# ABCDE

# using open, file will be print once but if want to print more then 
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)


# print(my_file.readline())
# ABCDE     read just first line to print the next line, we have to print it more
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

#ABCDE

# hiii

# jskqjkdq




# To print all the lines 
# print(my_file.readlines())
# ['ABCDE\n', 'hiii\n', 'jskqjkdq']


# close the file
# my_file.close()


