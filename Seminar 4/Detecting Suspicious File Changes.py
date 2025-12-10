import os
import csv
import hashlib

FOLDER = "files"
BASELINE = "baseline.csv"

def sha256_hash(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

# Load baseline
baseline = {}
with open(BASELINE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        baseline[row["filename"]] = row["sha256"]

current_files = os.listdir(FOLDER)

# Compare
for filename in baseline:
    if filename not in current_files:
        print(f"[ALERT] Missing file: {filename}")
    else:
        current_hash = sha256_hash(os.path.join(FOLDER, filename))
        if current_hash != baseline[filename]:
            print(f"[ALERT] Modified file: {filename}")

for filename in current_files:
    if filename not in baseline:
        print(f"[INFO] New file detected: {filename}")
