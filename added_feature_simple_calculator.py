class AddedFeature(BasicCalculator):
    def __init__(self, filename ="calculator_history.txt"):
        super().__init__()
        self.filename = filename
        self.history = []
        self.last_result = 0

    def history_storage(self, expression, result):
        entry = {"expression": expression, "result": result}

        self.history.append(entry)
        self.last_result = result

        with open(self.filename, "a") as file:
            file.write(f"{expression} = {result}\n")

    def expression_chain(self, expression):
        expression = expression.strip()
        if expression[0] in "+-*/":
            expression = str(self.last_result) + expression

        result = eval(expression)
        self.show_history(expression, result)

        return result

    def undo(self):
        if not self.history:
            print("Nothing to undo")
            return

        removed = self.history.pop()
        print(f"Undone: {removed['expression']} = {removed['result']}")

        self.last_result = self.history[-1]["result"] if self.history else 0

        with open(self.filename, "w") as file:
            for item in self.history:
                file.write(f"{item['expression']} = {item['result']}\n")

    def show_history(self):
        if not self.history:
            print("No history yet.")
            return

        print("\n History:")
        for i, item in enumerate(self.history, 1):
            print(f"{i}. {item['expression']} = {item['result']}")