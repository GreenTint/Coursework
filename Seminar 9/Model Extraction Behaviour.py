import subprocess

def ask(prompt):
    result = subprocess.run(
        ["ollama", "run", "smollm2:1.7b"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

prompts = [
    "Summarise Gen AI security in one sentence.",
    "Summarise Gen AI security in one sentence.",
    "Summarise Gen AI security in one sentence."
]

for i, p in enumerate(prompts, 1):
    print(f"Attempt {i}:")
    print(ask(p))
