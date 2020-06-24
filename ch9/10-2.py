#10-2C语言学习笔记
filename = 'learning_python1.txt'
with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'C++')
    print(contents)