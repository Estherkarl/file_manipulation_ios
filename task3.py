import os

def create_data_directories(directories):
    # Iterate through the directories to be created
    for directory in directories:
        # Define the full path of the directory
        dir_path = os.path.join(DATA_ROOT, directory)
        
        # Check if the directory exists
        if not os.path.exists(dir_path):
            # If not, create the directory
            os.makedirs(dir_path)
            print(f"Created directory: {directory}")
        else:
            # If it exists, print a message
            print(f"The directory {directory} already exists.")

# Call the function with the required directories
dirs = ["personal", "work"]
create_data_directories(dirs)
