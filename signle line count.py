def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return -1

# Replace 'your_file.txt' with the path to your file
file_path = 'hello.cpp'
num_lines = count_lines(file_path)
if num_lines >= 0:
    print(f"The number of lines in '{file_path}' is: {num_lines}")
