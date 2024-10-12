import os

# Define the ROOT constant which is the path of the current script
ROOT = os.path.dirname(os.path.abspath(__file__))

# Define the DATA_ROOT constant based on the ROOT and the given relative path
DATA_ROOT = os.path.join(ROOT, 'src', 'data', 'initial')

# Print the constants
print(ROOT)
print(DATA_ROOT)

