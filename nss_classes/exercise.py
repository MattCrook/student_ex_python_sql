class Exercise:
    def __init__(self, language, name):
        self.language = language
        self.name = name

    def __repr__(self):
        return f'{self.name} using the language: {self.language}' 
