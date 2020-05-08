#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    s = dict()
    for ticket in tickets:
        s[ticket.source] = ticket.destination
    route = [None] * length
    route[0] = s["NONE"]
    for i in range(1, len(route)):
        route[i] = s[route[i-1]] 

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)



# tickets = [
#     Ticket{ source: "NONE", destination: "ORD" },
#     Ticket{ source: "ORD", destination: "CID" },
#     Ticket{ source: "CID", destination: "BHM" },
#     Ticket{ source: "BHM", destination: "XNA" },
#     Ticket{ source: "XNA", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "SFO", destination: "SLC" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "PIT", destination: "NONE" }
# ]
