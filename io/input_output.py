import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'example.txt')

# txt_file = open(my_file)

# print(txt_file.read())

# txt_file.close()

with open(my_file, mode='a') as txt_file:
    text = txt_file.write("\nHey it's me")
    print(text)
    print(txt_file.readlines())
