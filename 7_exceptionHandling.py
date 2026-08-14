try:
    with open("data/harshal.txt", "r") as file:
        data = file.read()
    print("File read succefully")
except FileNotFoundError:
    print("File not present")