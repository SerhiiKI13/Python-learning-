from pathlib import Path

parent_dir = Path(__file__).resolve().parent

folder = Path("ExelFolder")
folder.mkdir(exist_ok=True)
folder_task = Path("TaskFolder")
folder_task.mkdir(exist_ok=True)

for file in parent_dir.iterdir():
    if file.is_file():
        if file.suffix == ".xlsx":
            destination = Path(parent_dir/folder/file.name)
            file.rename(destination)
    for files in folder.iterdir():
                if files.is_file():
                    if files.stem.lower().startswith("task"):
                        destination = Path(parent_dir / folder_task / files.name)
                        files.rename(destination)


