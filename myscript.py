import os
import csv

DATA_ROOT = '/home/dci-student/python/file-manipulation-1-Estherkarl/src/data/initial'
# Task 1
def show_data_list():
    data_path = os.path.join(DATA_ROOT, 'initial')
    for item in os.listdir(data_path):
        print(item)

# Task 2
ROOT = os.path.dirname(os.path.realpath(__file__))
DATA_ROOT = os.path.join(ROOT, 'src', 'data', 'initial')

# Task 3
def create_data_directories(dirs):
    for directory in dirs:
        dir_path = os.path.join(DATA_ROOT, directory)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        else:
            print(f"The directory {directory} already exists.")

# Task 4
def classify(categories):
    for category, files in categories.items():
        category_path = os.path.join(DATA_ROOT, category)
        for file in files:
            file_path = os.path.join(DATA_ROOT, file)
            if os.path.exists(file_path):
                os.rename(file_path, os.path.join(category_path, file))

# Task 5
def generate_pending_jobs_report():
    customers = {}
    with open(os.path.join(DATA_ROOT, 'customers.csv'), 'r') as customers_file:
        reader = csv.DictReader(customers_file)
        for row in reader:
            customers[row['id']] = row['name']

    pending_jobs = []
    with open(os.path.join(DATA_ROOT, 'jobs.csv'), 'r') as jobs_file:
        reader = csv.DictReader(jobs_file)
        for row in reader:
            if row['status'] != 'done':
                job_description = row['description']
                client_id = row['client_id']
                client_name = customers.get(client_id, 'Unknown')
                pending_jobs.append({'id': row['id'], 'description': job_description, 'client': client_name})

    reports_dir = os.path.join(DATA_ROOT, 'work', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    report_file_path = os.path.join(reports_dir, 'pending_jobs.csv')
    with open(report_file_path, 'w', newline='') as report_file:
        writer = csv.DictWriter(report_file, fieldnames=['id', 'description', 'client'])
        writer.writeheader()
        writer.writerows(pending_jobs)

    # Additional Task: Read and print bookmarks
    bookmarks_file_path = os.path.join(DATA_ROOT, 'bookmarks.txt')
    if os.path.exists(bookmarks_file_path):
        print("\nBookmarks:")
        with open(bookmarks_file_path, 'r') as bookmarks_file:
            for line in bookmarks_file:
                print(line.strip())

# Task 1
print("Task 1 Output:")
show_data_list()
print()

# Task 2
print("Task 2 Output:")
print(ROOT)
print(DATA_ROOT)
print()

# Task 3
print("Task 3 Output:")
create_data_directories(["personal", "work"])
print()

# Task 4
print("Task 4 Output:")
categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}
classify(categories)
print()

# Task 5
print("Task 5 Output:")
generate_pending_jobs_report()
