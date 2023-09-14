# 'r'=read
# with open('test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# ['ABCDE\n', 'hiii\n', 'jskqjkdq']

# have to run this code b4 opening in cmd file
# cmd go to this file and type the file name 'test1.txt'

# to read & write in the file 'r+'
# with open('test.txt', mode='r+') as my_file:
#     text=my_file.write('hey it\' me!')
#     print(text)

# # append something in the file
# with open('test.txt', mode='a') as my_file:
#     text=my_file.write(':)')
#     print(text)

# with open('test.txt', mode='w') as my_file:
#     text=my_file.write(':)')
#     print(text)

# create a new file, type the name 'sad.txt' 'w' then run the code b4 opening this file 'sad.txt' in cmd
with open('sad.txt', mode='w') as my_file:
    text=my_file.write("I'm not here")
    print(text)
