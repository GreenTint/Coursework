import re

def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()

    pattern = rb"[ -~]{4,}"  # ASCII characters between space and ~
    return re.findall(pattern, data)

strings = extract_strings(sample)

# Print the first 20 strings
for s in strings[:20]:
    print(s.decode(errors="ignore"))
