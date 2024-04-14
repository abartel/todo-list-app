def parse(feet_inches):
    split_height = feet_inches.split(" ")
    feet = float(split_height[0])
    inches = float(split_height[1])
    return {"feet":feet, "inches":inches}
