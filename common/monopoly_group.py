class MonopolyGroup:

    def __init__(self, props):
        self.props = props
        self.is_monopoly = False

    def check_monopoly(self):
        owners = {p.owner for p in self.props}
        if None not in owners and len(owners) == 1:
            self.is_monopoly = True
            for prop in self.props:
                prop.cost *= 2
            print(f'{" ".join((p.name for p in self.props))} are now a monopoly owned by {owners.pop()}')
