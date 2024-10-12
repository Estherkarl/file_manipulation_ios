import os
import shutil

DATA_ROOT = '/home/dci-student/python/file-manipulation-1-Estherkarl/src/data/initial'


def classify(categories):
    # Iterate through the dictionary of categories
    for directory, files in categories.items():
        # Define the target directory path
        dir_path = os.path.join(DATA_ROOT, directory)
        
        # For each file in the directory
        for file in files:
            # Define the source file path
            source_file = os.path.join(DATA_ROOT, file)
            
            # Define the destination file path
            dest_file = os.path.join(dir_path, file)
            
            # Move the file to the target directory
            if os.path.exists(source_file):
                shutil.move(source_file, dest_file)
                print(f"Moved {file} to {directory}")
            else:
                print(f"File {file} does not exist.")

# Test the function with the given dictionary
categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}
classify(categories)
