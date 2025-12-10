import hashlib, pefile, re, yara

sample = r"C:\Path\To\Procmon.exe"

# 1. Compute Hashes
def compute_hashes(path):
    algos = ["md5", "sha1", "sha256"]
    output = {}
    for algo in algos:
        h = hashlib.new(algo)
        with open(path, "rb") as f:
            h.update(f.read())
        output[algo] = h.hexdigest()
    return output

# 2. Extract Strings
def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    return re.findall(rb"[ -~]{4,}", data)

print("=== HASHES ===")
print(compute_hashes(sample))

print("\n=== STRINGS (first 10) ===")
print([s.decode(errors="ignore") for s in extract_strings(sample)[:10]])

# 3. Imports
print("\n=== IMPORT TABLE ===")
pe = pefile.PE(sample)
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print(entry.dll.decode())
    for imp in entry.imports[:5]:
        print("  -", imp.name.decode() if imp.name else "None")

# 4. Extract URLs and IPs
print("\n=== IOC EXTRACTION ===")
data = open(sample, "rb").read().decode(errors="ignore")
urls = re.findall(r"https?://[^\s\"']+", data)
ips = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", data)
print("URLs:", urls)
print("IPs:", ips)

# 5. YARA Rule
print("\n=== YARA MATCHES ===")
rule = yara.compile(source="""
rule SimpleHTTP {
    strings: $s = "http"
    condition: $s
}
""")
print(rule.match(sample))
