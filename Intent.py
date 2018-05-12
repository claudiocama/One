class c_intent():
    def __init__(self, name, entities, function):
        self.name = name
        self.entities = entities
        self.function = function
    def run(self):
        self.function(self.entities)
        
