#open the file for reading
with open("testic.txt") as souceFile:
    lines = souceFile.readlines()

lines[0] = "This is the line that's replaced.\n"

with open("testic.txt", "w") as souceFile:
    souceFile.writelines(lines)