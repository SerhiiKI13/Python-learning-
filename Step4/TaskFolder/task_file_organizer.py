from pathlib import Path
folder = Path("Step4")
print(folder)

for file in folder.iterdir():
    if file.is_file():
        if file.suffix == ".jpg" or file.suffix == ".png" or file.suffix == ".jpeg":
           destination =Path(folder / "fileOrganizer" / "Images" / file.name)
           file.rename(destination)
        elif file.suffix == ".pdf" or file.suffix == ".txt" or file.suffix == ".docx" or file.suffix == ".xlsx" :
            destination = Path(folder / "fileOrganizer" / "Documents" / file.name)
            file.rename(destination)
        elif file.suffix == ".mp3" :
            destination = Path(folder / "fileOrganizer" / "Music" / file.name)
            file.rename(destination)
    else:
        print("Not a file")
