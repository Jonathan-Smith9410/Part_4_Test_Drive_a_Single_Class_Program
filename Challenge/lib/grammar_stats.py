class GrammarStats:
    def __init__(self):
        self.total_checks = 0
        self.total_successful_checks = 0

    def check(self, text):
        # duplicated from Unit 3 exercise 2 (verify_text.py)
        if text == "":
            raise Exception("Input text required.")
        if text[0].isupper() and text[-1] in '.?")':
            self.total_checks += 1
            self.total_successful_checks += 1
            return True
        self.total_checks += 1
        return False

    def percentage_good(self):
        if self.total_checks == 0:
            raise Exception("Can't calculate percentage if no checks run.")
        return int((self.total_successful_checks / self.total_checks) * 100)