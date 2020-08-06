from translate import Translator

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'example.txt')
translator = Translator(to_lang="ja")

try:
    with open(my_file, mode='r+') as txt_file:
        file_to_translate = txt_file.read()
        translation = translator.translate(file_to_translate)
        print(translation)

except FileNotFoundError:
    print("File Not Found!!")
