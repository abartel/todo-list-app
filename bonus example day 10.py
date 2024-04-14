try:
    width = float(input("Width?"))
    length = float(input("Length?"))

    if width == length:
        exit("We don't take no squares 'round here!")

    area = width * length
    print(area)

except ValueError:
    print("Numbers only.")