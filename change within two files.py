
import difflib

def find_changes_in_cpp_files(file_path1, file_path2):
    try:
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            differ = difflib.Differ()
            diff = list(differ.compare(lines1, lines2))

            added_lines = []
            deleted_lines = []
 

            added_lines_count = sum(1 for line in diff if line.startswith('+ '))
            deleted_lines_count = sum(1 for line in diff if line.startswith('- '))

            for i, line in enumerate(diff, 1):
                if line.startswith('+ '):
                    added_lines.append((i, line[2:]))
                elif line.startswith('- '):
                    deleted_lines.append((i, line[2:]))
       

            return added_lines, deleted_lines, added_lines_count, deleted_lines_count
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return [], [], [], 0, 0, 0

# Example usage:
file_path1 = r'C:\Users\Md Arif Hasan\Desktop\code\file1.cpp'
file_path2 = r'C:\Users\Md Arif Hasan\Desktop\code\file2.cpp'
added, deleted, added_lines_count, deleted_lines_count = find_changes_in_cpp_files(file_path1, file_path2)

print(f"Number of added lines: {added_lines_count}")
print(f"Number of deleted lines: {deleted_lines_count}")

print(f"Total number of changes: {added_lines_count + deleted_lines_count}")

print("Added Lines for this file:")
for line_num, line_text in added:
    print(f"Single line : {line_text}")

print("\nDeleted Lines for this file:")
for line_num, line_text in deleted:
    print(f"Single line : {line_text}")
