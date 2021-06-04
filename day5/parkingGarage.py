class Garage():

    def __init__(self, spaces):
        self.spaces = spaces

    def takeTicket(self, tickets, parkingSpaces):
        del tickets[0]
        del parkingSpaces[0]
    
    def giveBackSpace(self, tickets, parkingSpaces):
        tickets += 1
        parkingSpaces += 1

    def paymentMethod(self):
        pass

    def payForParking(self, tickets, parkingSpaces):
        self.takeTicket(self, tickets, parkingSpaces)
        

    def paidForParking(self, tickets, parkingSpaces):
        tickets += 1
        parkingSpaces += 1


    def leaveGarage(self, tickets, parkingSpaces):
        self.giveBackSpace(tickets, parkingSpaces)
        print("Thank you, enjoy your day!")


def main():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
    currentTickets = {}
    aasdf = []
    input1 = input("'pay' for tickey? ")
    for ticket in tickets:
        if input1 == "pay":
            aasdf.append(tickets[0])
            del tickets[0]
            print(f"tickets: {tickets}")
            print(f"aasdf: {aasdf}")
    input1 = input("'pay' for tickey? ")
    for ticket in tickets:
        if input1 == "leave":
            tickets.append(aasdf[0])
            if aasdf == []:
                break
            del aasdf[0]
            print(f"tickets: {sorted(tickets)}")
            print(f"aasdf: {aasdf}")
            if aasdf == []:
                break
        

main()