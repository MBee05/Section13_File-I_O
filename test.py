try:
    with open('./text2.txt', mode='r') as my_file:
        print(my_file.read())
except FileExistsError as e:
    print('check your file path')