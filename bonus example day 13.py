feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    split_height = feet_inches.split(" ")
    feet = float(split_height[0])
    inches = float(split_height[1])
    return {"feet":feet, "inches":inches}


def convert(feet, inches):
    meters = (feet*0.3048)+(inches*0.0254)
    return meters


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Too small")
else:
    print("ok")
