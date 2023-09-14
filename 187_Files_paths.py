# create a new file, type the name 'sad.txt' 'w' then run the code b4 opening this file 'sad.txt' in cmd
# with open('app/text2.txt', mode='r') as my_file:
#     print=(my_file.read())
   

with open('text2.txt', mode='w') as my_file:
    text=my_file.write("I'm not here")
    print(text)
