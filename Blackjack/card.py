class card:

    def __init__(self, card_type, value):
        self.card_type = card_type
        self.value = value

    #getters/setters (accessors) are very non-pythonic!
    def getType(self):
        return self.card_type
    
    def getValue(self):
        return self.value
    
