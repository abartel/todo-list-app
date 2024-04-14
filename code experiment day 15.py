import glob  # useful when you want to view all the files in a folder

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
