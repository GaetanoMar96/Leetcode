class Bag:
    # Data structure used to store data without the ability to remove them.
    # To be used when the insertion order is not important.

    def __init__(self) -> None:
        self.bags = []

    def add(self, val) -> None:
        self.bags.append(val)

    def getSize(self) -> int:
        return len(self.bags)
    
    def doOperation(self) -> None:
        # in this case a simple for loop
        for bag in self.bags:
            print(bag)
