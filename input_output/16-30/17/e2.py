cible = b"test"
total = 0

with open("copy.bin","rb") as src:
    while True:
        chunk = src.read(1024).lower()
        if not chunk:
            break
        total +=chunk.count(cible)
print(f"Nombre totale d'occurences de {cible!r} : {total}")