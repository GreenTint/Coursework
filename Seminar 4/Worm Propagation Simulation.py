import random

HOSTS = 20
INFECTED = {0}  # worm starts on host 0
ATTEMPTS_PER_HOST = 3

def propagate(infected):
    new_infected = set(infected)
    for host in infected:
        for _ in range(ATTEMPTS_PER_HOST):
            target = random.randint(0, HOSTS - 1)
            new_infected.add(target)
    return new_infected

step = 0
while len(INFECTED) < HOSTS:
    print(f"Step {step}: {len(INFECTED)} infected")
    INFECTED = propagate(INFECTED)
    step += 1

print("\nAll hosts infected in", step, "steps")
