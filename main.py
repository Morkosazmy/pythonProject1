#File detection

import os

#direct connection:
file_path = "test.txt"

#indirect connection:
file_path2 = "C:/Users/morko/PycharmProjects/pythonProject/.venv/test.txt"
file_path3 = "C:/Users/morko/PycharmProjects/pythonProject/test.txt"
file_path1 = "C:/Users/morko/OneDrive/Bureau/New Document texte (11).txt"
path_dir = "C:/Users/morko/OneDrive/Bureau/Corrigé proba alternance"
if os.path.exists(file_path2):
    print(f"found the '{file_path2}' file")
else:
    print("file not found")

if os.path.exists(file_path):
    print(f"found the '{file_path}' file")
else:
    print("file not found")

if os.path.exists(file_path3):
    print(f"found the '{file_path3}' file")
else:
    print("file not found")

if os.path.exists(file_path1):
    print(f"found the '{file_path1}' file")
else:
    print("file not found")

if os.path.exists(file_path1):
    print(f"found the '{file_path1}' file")
else:
    print("file not found")

if os.path.isfile(path_dir):
    print(f"found the '{path_dir}' file")
elif os.path.isdir(path_dir): #no extension (ex: .txt .pdf etc...)
    print(f"found the '{path_dir}' directory")
else:
    print("File/Directory not found")