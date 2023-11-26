import random

def generate_weights(total_weight):
    weights = []
    cargo1 = random.randint(1, total_weight - 2)
    cargo2 = random.randint(1, total_weight - 1)
    cargo3 = total_weight - cargo1 - cargo2
    
    weights.append(cargo1)
    weights.append(cargo2)
    weights.append(cargo3)
    return weights