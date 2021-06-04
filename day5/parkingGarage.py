class Garage():

    def __init__(self,tickets, parkingSpaces):
        #self.spaces = spaces
        self.tickets =tickets
        self.parkingSpaces = parkingSpaces

    def takeTicket(self, currentTickets):
        currentTickets.update({self.tickets[0]:""})
        print(currentTickets)
        del self.tickets[0]
        del self.parkingSpaces[0]
        print(f"Available tickets: {self.tickets}\nAvailable parking spaces: {self.parkingSpaces}")
    
    
    def giveBackSpace(self):
        tickets += 1
        parkingSpaces += 1

    def payForParking(self, currentTickets):
        print(currentTickets.keys())
        ask = int(input("What is your ticket number? "))
        print(f"Your ticket number is {ask}.")
        ask = input("How would you like to pay? ")

        

        
        

    def paidForParking(self):
        tickets += 1
        parkingSpaces += 1


    def leaveGarage(self):
        self.giveBackSpace(tickets, parkingSpaces)
        print("Thank you, enjoy your day!")


def main():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
    currentTickets = {}
    aasdf = []
    while True:
        ask = input("What would you like to do? \n Park/pay/leave/quit? ")
        if ask.lower() == 'park':
            Garage(tickets, parkingSpaces).takeTicket(currentTickets)
        elif ask.lower() == 'pay':
            Garage(tickets, parkingSpaces).payForParking(currentTickets)

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