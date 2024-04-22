from re import fullmatch

class InputChecker:
    def __init__(self, root, regex, max_length=0):
        self.root = root
        self.max_length = max_length
        self.regex = regex

    def validate(self, input):
        match = fullmatch(self.regex, input)
        if self.max_length > 0:
            return match is not None and len(match.group(0)) <= self.max_length
        return match is not None

    def create_tcl_wrapper(self):
        wrapper = (self.root.register(self.validate), '%P')
        return wrapper