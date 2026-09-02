import time

menu_options = ("h", "x", "s")

while True:
    print()
    print("** MENU **")
    print("h = help")
    print("x = exit")
    print("s = start")

    print()
    user_input = input("Enter option:")

    if user_input in menu_options:
        break
    else:
        print()
        print("Option not available")
