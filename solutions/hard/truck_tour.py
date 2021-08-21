#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

# Goal is to find the first petrol station on the circle starting
# from which the truck will have enough fuel to compelte the circle
# and get back to starting point.(truck gets to refuel at every station).
def truckTour(petrolpumps) -> int:
    # Write your code here
    fuel = 0
    n = len(petrolpumps)
    l = 0
    i = l
    while i < n:
        fuel = fuel + petrolpumps[i][0] - petrolpumps[i][1]
        if fuel < 0:
            l = l + 1
            i = l
            fuel = 0
        else:
            i += 1
    return l