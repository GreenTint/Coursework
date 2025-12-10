import pefile

pe = pefile.PE(sample)

print("Entry Point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))

print("\nImported DLLs and Functions:")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print("DLL:", entry.dll.decode())
    for imp in entry.imports[:5]:  # show first 5 imports
        print(" -", imp.name.decode() if imp.name else "None")
