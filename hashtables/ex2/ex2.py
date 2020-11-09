#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"{self.source} {self.destination}"


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
        
    hash_table = {}
    arr = []
    count0 = 0
    count1 = 1

    for x in tickets:
        split = str(x).split()
        arr.append(split)

    for x in range(0, length):
        hash_table[arr[count0][0]] = arr[count0][1]
        count0 += 1
        count1 += 1
    
    route = []
    route_num = 0

    for x in range(0, length):
        if len(route) < 1:
            route.append(hash_table['NONE'])

        else:
            route.append(hash_table[route[route_num]])
            route_num += 1

    return route
