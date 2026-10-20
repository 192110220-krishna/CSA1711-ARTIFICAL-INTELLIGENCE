
rooms = {
    "A": input("Enter state of Room A (clean/dirty): ").lower(),
    "B": input("Enter state of Room B (clean/dirty): ").lower()
}

location = input("Enter vacuum starting location (A/B): ").upper()

while location not in rooms:
    location = input("Enter a valid location (A/B): ").upper()

while "dirty" in rooms.values():
    print("\nCurrent location:", location)
    print("Room states:", rooms)

    if rooms[location] == "dirty":
        print("Action: SUCK")
        rooms[location] = "clean"
    else:
        location = "B" if location == "A" else "A"
        print("Action: MOVE")

print("\nBoth rooms are clean!")
print("Final room states:", rooms)
