import os

# Directory path
directory = r"C:\Users\82107\Downloads\part3\part3"

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        try:
            parts = filename.split("_")
            race = int(parts[2])

            if race != 2:
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
                print(f"Deleted: {filename}")
        except (IndexError, ValueError):
            print(f"Skipped: {filename} (unexpected format)")


directory = r"C:\Users\82107\Downloads\part3\part3"

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        try:
            parts = filename.split("_")
            race = int(parts[2])
            if race == 2:
                count += 1
        except (IndexError, ValueError):
            pass

print(f"Remaining files with race Asian : {count}") # 총 3465개가 나옴.
