from translate import Translator
# translator = Translator(to_lang='ja')

# try:
#     with open('text2.txt', mode='r') as my_file:
#         text= my_file.read()
#         translation=translator.translate(text)
#         print(translation)
# except FileNotFoundError as e:
#     print('check your file path')
    
    
# output    僕はいませんよ

translator = Translator(to_lang='ja')

try:
    with open('text2.txt', mode='r') as my_file:
        text= my_file.read()
        translation=translator.translate(text)
        with open('test2-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path')
