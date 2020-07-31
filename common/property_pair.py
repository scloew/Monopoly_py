class PropertyPair:

    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2
        self.is_monopoly = False

    def check_monopoly(self):
        if self.prop1 == self.prop2 and not self.is_monopoly:
            self.is_monopoly = True
            self.prop1.cost *= 2
            self.prop2.cost *= 2
            print(f'{self.prop1} and {self.prop2} are now a monopoly')
