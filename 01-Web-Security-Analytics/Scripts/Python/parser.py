from datetime import datetime
from pathlib import Path
import csv

data_dir = Path.home() / "web-security-analytics" / "data"

log_file = data_dir / "security_access-1000-working.log"
output_file = data_dir / "security_analytics_cleaned.csv"

total_records = 0
valid_records = 0
invalid_records = 0

records = []

with open(log_file, "r") as file:
    for line in file:
        total_records += 1

        fields = line.strip().split("|")

        if len(fields) == 11:
            valid_records += 1

            timestamp = datetime.strptime(
                fields[1],
                "%Y-%m-%dT%H:%M:%S%z"
            )

            status_code = int(fields[6])
            user_agent = fields[10]

            if 200 <= status_code < 300:
                status_category = "Success"
            elif 400 <= status_code < 500:
                status_category = "Client Error"
            elif 500 <= status_code < 600:
                status_category = "Server Error"
            else:
                status_category = "Other"

            if "Normal-User-Dataset" in user_agent:
                traffic_type = "Normal"
            elif "Bot-Dataset-Test" in user_agent:
                traffic_type = "Bot"
            elif "Recon-Dataset-Test" in user_agent:
                traffic_type = "Recon"
            elif "Auth-Failure-Dataset" in user_agent:
                traffic_type = "Auth Failure"
            elif "Server-Error-Dataset" in user_agent:
                traffic_type = "Server Error"
            else:
                traffic_type = "Unknown"

            record = {
                "source_ip": fields[0],
                "timestamp": timestamp,
                "date": timestamp.date(),
                "hour": timestamp.hour,
                "http_method": fields[2],
                "url": fields[3],
                "query_string": fields[4],
                "protocol": fields[5],
                "status_code": status_code,
                "status_category": status_category,
                "bytes_transferred": int(fields[7]),
                "response_time_ms": int(fields[8]),
                "referrer": fields[9],
                "user_agent": user_agent,
                "traffic_type": traffic_type
            }

            records.append(record)

        else:
            invalid_records += 1

print("Total records:", total_records)
print("Valid records:", valid_records)
print("Invalid records:", invalid_records)

print("\nFirst structured record:")
print(records[0])

traffic_counts = {}

for record in records:
    traffic_type = record["traffic_type"]

    if traffic_type in traffic_counts:
        traffic_counts[traffic_type] += 1
    else:
        traffic_counts[traffic_type] = 1

print("\nTraffic Type Counts:")

for traffic_type, count in traffic_counts.items():
    print(traffic_type, ":", count)

fieldnames = [
    "source_ip",
    "timestamp",
    "date",
    "hour",
    "http_method",
    "url",
    "query_string",
    "protocol",
    "status_code",
    "status_category",
    "bytes_transferred",
    "response_time_ms",
    "referrer",
    "user_agent",
    "traffic_type"
]

with open(output_file, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for record in records:
        csv_record = record.copy()

        csv_record["timestamp"] = record["timestamp"].isoformat()
        csv_record["date"] = record["date"].isoformat()

        writer.writerow(csv_record)

print("\nCSV exported to:", output_file)
