import random


class Definition:
    def __int__(self, word, noun, verb, exclamation, examples):
        self.word = word
        self.noun = noun
        self.verb = verb
        self.exclamation = exclamation
        self.examples = examples

    def getDefinition(self, word_type):
        active = []
        match word_type:
            case "noun":
                active = self.noun
            case "verb":
                active = self.verb
            case "exclamation":
                active = self.exclamation
            case "example":
                active = self.examples
        return active[random.Random.randint(0, len(active))]
