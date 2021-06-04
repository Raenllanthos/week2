class Garage():

    def __init__(self, spaces,tickets, parkingSpaces):
        self.spaces = spaces
        self.tickets =tickets
        self.parkingSpaces = parkingSpaces

    def takeTicket(self, currentTickets):
        # currentTickets +=1
        print(currentTickets)
        # del self.tickets[0]
        # del self.parkingSpaces[0]
        return f"Available tickets {self.tickets}  \n available parking spaces {self.parkingSpaces}"
    
    
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
    ask = input("What would you like to do? \n Park/pay/leave/quit?")
    if ask.lower() == 'park':
        Garage().takeTicket(tickets, parkingSpaces, currentTickets)

    # for ticket in tickets:
    #     if input1 == "park":
    #         aasdf.append(tickets[0])
    #         del tickets[0]
    #         del parkingSpaces[0]
    #         print(f"tickets: {tickets}")
    #         print(f"aasdf: {aasdf}")
    # input1 = input("'pay' for tickey? ")
    # for ticket in tickets:
    #     if input1 == "pay":
    #         tickets.append(aasdf[0])
    #         parkingSpaces.append(aasdf[0])
    #         # currentTickets.update({tickets[0]:  parkingSpaces)
    #         if aasdf == []:
    #             break
    #         del aasdf[0]
    #         print(f"tickets: {sorted(tickets)}")
    #         print(f"aasdf: {aasdf}")
    #         if aasdf == []:
    #             break
        

main()