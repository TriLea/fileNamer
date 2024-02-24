import os
import uuid

def rename_files_in_directory(directory_path):
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        print("The provided path is not a valid directory.")
        return

    # List all files in the directory
    files = os.listdir(directory_path)

    for filename in files:
        # Generate a new unique name with the same file extension (if any)
        extension = os.path.splitext(filename)[1]
        new_filename = str(uuid.uuid4()) + extension

        # Construct the full old and new file paths
        old_file = os.path.join(directory_path, filename)
        new_file = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    directory_path = input("Enter the path of the directory: ").strip()
    rename_files_in_directory(directory_path)
