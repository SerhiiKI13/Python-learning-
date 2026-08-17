from pathlib import Path
folder = Path("fileOrganizer")
folder.mkdir(exist_ok=True)

folderImages = folder / "Images"
folderImages.mkdir(exist_ok=True)

folderDocuments = folder / "Documents"
folderDocuments.mkdir(exist_ok=True)

folderMusic = folder / "Music"
folderMusic.mkdir(exist_ok=True)


file = Path("fileOrganizer/photo.jpg")
destination = Path("fileOrganizer/photo.jpg")
file.rename(destination)