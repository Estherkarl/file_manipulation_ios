import csv
import os

DATA_ROOT = '/home/dci-student/python/file-manipulation-1-Estherkarl/src/data/initial'



def generate_pending_jobs_report():
    # Ensure the reports directory exists
    reports_dir = os.path.join(DATA_ROOT, 'work', 'reports')
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    # Paths to the files
    customers_file = os.path.join(DATA_ROOT, 'work', 'customers.csv')
    jobs_file = os.path.join(DATA_ROOT, 'work', 'jobs.csv')
    pending_jobs_file = os.path.join(reports_dir, 'pending_jobs.csv')
    
    # Read customers and create a mapping of customer ID to name
    customer_dict = {}
    with open(customers_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer_dict[row['id']] = row['name']
    
    # Prepare the CSV for writing the pending jobs
    with open(pending_jobs_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['id', 'description', 'client'])
        
        # Read jobs and filter out those not done
        with open(jobs_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['status'] != 'done':
                    # Get the client name based on the customer ID
                    client_name = customer_dict.get(row['customer_id'], 'Unknown')
                    # Write the job details to the CSV
                    writer.writerow([row['id'], row['description'], client_name])

# Generate the pending jobs report
generate_pending_jobs_report()
