with open("file.txt", "rb") as f:
    f.seek(-10, 2)
    f.readline().decode('utf-8')
