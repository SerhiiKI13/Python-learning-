from pathlib import Path
folder = Path("fileOrganizer")

for file in folder.iterdir():
    if file.is_file():
        if file.suffix == ".jpg" or file.suffix == ".png" or file.suffix == ".jpeg":
           destination =Path(folder / "Images" / file.name)
           file.rename(destination)
        elif file.suffix == ".pdf" or file.suffix == ".txt" or file.suffix == ".docx" :
            destination = Path(folder / "Documents" / file.name)
            file.rename(destination)
        elif file.suffix == ".mp3" :
            destination = Path(folder / "Music" / file.name)
            file.rename(destination)
    else:
        print("Not a file")
