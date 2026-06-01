import csv

total_requests = 0
error_count = 0
failed_requests = []
user_summary = {}
corrupted_rows = 0

try:
    with open('logs.csv','r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                user = row['user']
                status = int(row['status'])
                path = row['path']

                total_requests += 1
                user_summary[user] = user_summary.get(user, 0) + 1

                if status >= 400:
                    error_count += 1
                    failed_requests.append(row)

            except (KeyError, ValueError,TypeError):
                corrupted_rows += 1

except FileNotFoundError:
    print("File not found.")

print("Total requests:", total_requests)
print("Error count:", error_count)
print("Failed requests:", failed_requests)
print("User summary:", user_summary)
print("Corrupted rows:", corrupted_rows)