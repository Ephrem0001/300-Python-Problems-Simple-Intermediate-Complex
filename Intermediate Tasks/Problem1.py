import os

file = input("Enter a file with extension")
file_name ,file_extension = os.path.splitext(file)
if file_extension == ".mp3":
    print("file name is not allowed")
else:
    print("file name is " + file_extension)
