filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("hello\n")
    file_object.write("world\n")