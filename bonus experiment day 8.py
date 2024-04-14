date = input("Enter today's date: ")
mood = input("Scale of 1-10, how are you? ")
thoughts = input("Preach:\n")

with open(f"journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)