feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    split_height = feet_inches.split(" ")
    feet = float(split_height[0])
    inches = float(split_height[1])
    meters = (feet*0.3048)+(inches*0.0254)
    return meters


result = convert(feet_inches)

if result < 1:
    print("Too small")
else:
    print("ok")