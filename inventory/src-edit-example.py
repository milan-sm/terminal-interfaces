# Research more, "keyboard", "curses"

import keyboard

def edit_item_name():
    print("Editing Item Name...")

def edit_category():
    print("Editing Category...")

def edit_location():
    print("Editing Location...")

def edit_quantity():
    print("Editing Quantity...")

def edit_price():
    print("Editing Price...")

def save_changes():
    print("Saving Changes...")

def cancel_changes():
    print("Canceling Changes...")

def main():
    print("Inventory Management App")
    print("Press F1-F7 to access corresponding edit options.")
    print("Press 'q' to quit.")

    keyboard.add_hotkey('f1', edit_item_name)
    keyboard.add_hotkey('f2', edit_category)
    keyboard.add_hotkey('f3', edit_location)
    keyboard.add_hotkey('f4', edit_quantity)
    keyboard.add_hotkey('f5', edit_price)
    keyboard.add_hotkey('f6', save_changes)
    keyboard.add_hotkey('f7', cancel_changes)

    keyboard.wait('q')

if __name__ == "__main__":
    main()
