import os
import hashlib
import csv
from datetime import datetime

FOLDER = "files"  # folder that contains files to monitor
BASELINE = "baseline.csv"

def sha256_hash(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

# Create baseline file
with open(BASELINE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "sha256", "timestamp"])

    for filename in os.listdir(FOLDER):
        path = os.path.join(FOLDER, filename)
        if os.path.isfile(path):
            file_hash = sha256_hash(path)
            timestamp = datetime.now().isoformat()
            writer.writerow([filename, file_hash, timestamp])

print("Baseline created in baseline.csv")
