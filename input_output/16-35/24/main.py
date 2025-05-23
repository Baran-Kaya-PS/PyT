filenames = input("enter filenames (comma-separated): ").split(',')

for name in filenames:
    try:
        name = name.strip()
        with open(name,'r') as f:
            content = f.read()
            print(f"{name} : {len(content)} characters")
    except FileNotFoundError:
        print(f"Warning: {name} not found")