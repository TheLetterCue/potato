from random import randint

def Roll():
    match randint(1,6):
        case 1|2:
            match randint(1,6):
                case 1:
                    return [0,1,0,0]
                case 2:
                    return [1,1,0,0]
                case 3:
                    return [1,0,1,0]
                case 4:
                    return [0,-1,1,0]
                case 5:
                    return [0,-1,0,0]
                case 6:
                    return [0,2,0,0]
        case 3|4:
            match randint(1,6):
                case 1:
                    return [0,0,1,0]
                case 2:
                    return [1,0,0,0]
                case 3:
                    return [1,0,1,0]
                case 4:
                    return [0,-1,2,0]
                case 5:
                    return [1,0,0,0]
                case 6:
                    return [0,2,0,0]
        case 5|6:
            return [0,0,0,1]

def Play(use_potatoes = False, verbose = False):
    stats = [0,0,0,1]
    while max(stats[:-1]) < 10:
        while use_potatoes and stats[1] >= stats[3]:
            stats[1] -= stats[3]
            stats[2] -= 1
        stats = [sum(a) for a in zip(stats, Roll())]
    
    match (result := stats[:-1].index(max(stats[:-1]))):
        case 0:
            if verbose:print("Wizard kidnapping")
        case 1:
            if verbose:print("Cozy hole")
        case 2:
            if verbose:print("Eaten by orcs")
    return result

EXPERIMENTS = 10000

wins = 0
for a in range(EXPERIMENTS):
    if Play(use_potatoes=True) != 2:
        wins += 1
print(f"{wins/EXPERIMENTS} wins per experiment")

wins = 0
for a in range(EXPERIMENTS):
    if Play() != 2:
        wins += 1    
print(f"{wins/EXPERIMENTS} wins per experiment")