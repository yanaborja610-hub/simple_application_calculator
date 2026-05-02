from added_feature_simple_calculator import AddedFeature

def main_calculator():
    calculator = AddedFeature()

    print("Simple App Calculator")
    print("Commands: undo | history | exit")
    print("You can also type expression like: 5+3 and another +2 (for chaining)\n")

    while True:
        user_input = input("Enter expression: ").strip()

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        elif user_input.lower() == "history":
            calculator.show_history()

        elif user_input.lower() == "undo":
            calculator.undo()