with open("my_file.txt", "w") as file:
    file.write("Hello, this is line 1.\n")
    file.write("12345 is an interesting number.\n")
    file.write("Python is awesome!\n")

print("File 'my_file.txt' created successfully with initial content.")

with open("my_file.txt", "r") as file:
    file_content = file.read()
    print("\nContents of 'my_file.txt':\n")
    print(file_content)
    
with open("my_file.txt", "a") as file:
    file.write("\nAppending a new line.\n")
    file.write("More text added here.\n")
    file.write("Final line for appending.\n")

print("\nFile 'my_file.txt' updated with additional content.")

try:
    # Attempt to open a non-existent file (for demonstration purposes)
    with open("non_existent_file.txt", "r") as non_existent_file:
        content = non_existent_file.read()
except FileNotFoundError:
    print("\nError: File not found. Please check the file name or path.")

except PermissionError:
    print("\nError: Permission denied. Make sure you have the necessary permissions.")

finally:
    print("\nFile handling completed.")