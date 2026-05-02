class AddedFeature(BasicCalculator):
    def __init__(self, filename ="calc_history.txt"):
        self.filename = filename
        self.history = []
        self.last_result = 0

    def show_history(self, expression, result):
        entry = {"expression": expression, "result": result}

        self.history.append(entry)
        self.last_result = result

