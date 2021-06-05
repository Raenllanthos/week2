class Garage():

    def __init__(self,tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces

    def garageSize(self):
        while True:
            size = int(input("How big is the garage? (1 - 100) "))
            if (size > 0) and (size < 101):
                for x in range(1, size+1):
                    self.tickets.append(x)
                    self.parkingSpaces.append(x)
                break
            else:
                print("Incorrect size")
                continue

    def takeTicket(self, currentTickets):
        if self.tickets != []:
            currentTickets.update({self.tickets[0]:""})
            del self.tickets[0]
            del self.parkingSpaces[0]
            self.show(currentTickets)
        else:
            print("No more room :(")

    def payForParking(self, currentTickets):
        self.show(currentTickets)
        key = int(input("What is your ticket number? "))
        print(f"Your ticket number is {key}.")
        value = input("Pay in 'cash' or 'card'? ")
        if value.lower() == "cash":
            currentTickets[key] = "paid cash"
        elif value.lower() == "card":
            currentTickets[key] = "paid card"
        else:
            print("Incorrect Payment Type")

    def show(self, currentTickets):
        print(f"\nAvailable tickets: {sorted(self.tickets)}\nAvailable parking spaces: {sorted(self.parkingSpaces)}\nTaken spaces:")
        print(f"{currentTickets}\n")

    def leaveGarage(self, currentTickets):
        print(currentTickets)
        key = int(input("Pick a ticket that has been paid: "))
        if (currentTickets[key] == "paid cash") or (currentTickets[key] == "paid card"):
            print("You may leave")
            self.tickets.append(key)
            self.parkingSpaces.append(key)
            currentTickets.pop(key)
        else:
            print("YOU STILL NEED TO PAY ASSHOLE")
        
def main():
    tickets = []
    parkingSpaces = []
    currentTickets = {}
    Garage(tickets, parkingSpaces).garageSize()
    while True:
        ask = input("What would you like to do? \n Park/pay/show/leave/quit? ")
        if ask.lower() == 'park':
            Garage(tickets, parkingSpaces).takeTicket(currentTickets)
        elif ask.lower() == 'pay':
            Garage(tickets, parkingSpaces).payForParking(currentTickets)
        elif ask.lower() == 'leave':
            Garage(tickets, parkingSpaces).leaveGarage(currentTickets)
        elif ask.lower() == "show":
            Garage(tickets, parkingSpaces).show(currentTickets)
        elif ask.lower() == 'quit':
            break

main()