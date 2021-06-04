class Garage():
    TICKETS = []
    PARKINGSPACES = []
    CURRENTTICKET = {}

    def __init__(self, spaces):
        self.spaces = spaces

    def spacesInfo(self, spaces):
        tickets = spaces
        parkingSpaces = spaces
        return spaces

    def takeTicket(self, tickets, parkingSpaces):
        tickets -= 1
        parkingSpaces -= 1
    
    def giveBackSpace(self, tickets, parkingSpaces):
        tickets += 1
        parkingSpaces += 1

    def paymentMethod(self):
        pass

    def payForParking(self, tickets, parkingSpaces):
        pass

    def paidForParking(self, tickets, parkingSpaces):
        tickets += 1
        parkingSpaces += 1


    def leaveGarage(self, tickets, parkingSpaces):
        pass


def main():
    pass

main()