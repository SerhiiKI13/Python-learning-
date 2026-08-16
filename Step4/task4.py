from pathlib import Path
folder = Path("data")
folder.mkdir(exist_ok=True)


for item in folder.glob("*.txt"):
    print(item)