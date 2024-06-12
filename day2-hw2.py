# Assignments: Nested If

# 1. Nested Decisions: The Adventure Game 🏰

# Task 1: Code Correction

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!") 
elif place == "cave":
    # print("You find a hidden treasure!")
    # Task 2: Setting the Scene:
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark": 
        print("You fell in a trap!")
# Task 3: Default Path
else:
    pass

# 2. Quick Decisions: The Event Planner 🎉

# Task 1: Code Correction

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)

# Task 2: Catering Choices

is_vegetarian = input("Do you want vegetarian food? y/n\n")
if is_vegetarian == "y":
    print("We recommend veggie delight daterers")
else:
    print("We recommend gourmet meals caterers")