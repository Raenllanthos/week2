class Garage():
    TICKETS = []
    PARKINGSPACES = []
    CURRENTTICKET = {}

    def __init__(self, spaces):
        self.spaces = spaces

    def spacesInfo(self, spaces):
        tickets = spaces
        parkingSpaces = spaces
        return spaces, tickets, parkingSpaces

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
        self.giveBackSpace(tickets,parkingSpaces)
        print('Thank you, enjoy your day!')


def main():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
    currentTickets = {}

main()