import os

DATA_ROOT = '/home/dci-student/python/file-manipulation-1-Estherkarl/src/data/initial'


def show_data_list():
    # Get the current directory of the script
    current_path = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to 'src/data/initial' directory
    data_path = os.path.join(current_path, 'src', 'data', 'initial')
    
    # List all the files and directories in the path
    files = os.listdir(data_path)
    
    # Print each file/directory name
    for file in files:
        print(file)

# Call the function to print the contents
show_data_list()
