import random

THRESHOLD = 5  # flag host if they exceed this number
HOSTS = 10

def generate_activity():
    return [random.randint(0, 10) for _ in range(HOSTS)]

activity = generate_activity()

for host_id, count in enumerate(activity):
    if count > THRESHOLD:
        print(f"[ALERT] Host {host_id} shows unusual activity ({count} outbound requests)")
