filename = input("Enter filename to read: ")

try:
    with open(filename, 'r') as file:
        print("\n--- First 3 Lines ---")
        for _ in range(3):
            line = file.readline()
            if not line:
                break
            print(line, end='')
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File operation attempted.")