print(" _                                     _     _                 _")
print("| |                                   (_)   | |               | |")
print("| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |")
print("| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |")
print("| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |")
print("\__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|")

print("")

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice = input("You are at a crossroad. You can go left or right. Which do you choose? ")

if choice == "right":
    print("Game Over.")
else:
    choice = input("You have come across a vast lake. In the direction you came from you hear chanting. Do you swim or wait? ")
