import zipfile
import os

filename = "flag.txt"

with zipfile.ZipFile(f"{filename}.0.zip", 'w') as file:
    file.write(filename)

    for i in range(1,9002):
        file.write(filename, f"{filename}.{i}.zip")
        filename = f"{filename}.{i}.zip"