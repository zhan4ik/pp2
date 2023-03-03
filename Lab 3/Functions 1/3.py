numheads = 35
numlegs = 94

def solve(numheads, numlegs):
    chicken = numheads - ((numlegs - 2 * numheads) / 2)
    rabbits = numheads - chicken
    print(chicken, rabbits) 
    
solve(numheads, numlegs)