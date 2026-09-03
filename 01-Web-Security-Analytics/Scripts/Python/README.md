# Python Security Log Parser

This directory contains the Python script used to parse, validate, enrich, and export the Apache security analytics dataset.

The Python script converts the raw pipe-delimited Apache security log into structured data suitable for SQL Server analysis and dashboard visualization.

## Script

```text
parser.py
```

## Input Dataset

```text
security_access-1000-working.log
```

The controlled dataset contains:

- 1,000 total HTTP requests
- 600 Normal requests
- 150 Bot requests
- 100 Recon requests
- 100 Authentication Failure requests
- 50 Server Error requests

## Processing Workflow

The parser performs the following steps:

1. Reads the Apache security log line by line
2. Splits each record using the `|` delimiter
3. Validates that each record contains exactly 11 fields
4. Converts the timestamp into a Python `datetime` object
5. Converts numeric fields into integer values
6. Derives HTTP status categories
7. Derives date and hour fields
8. Classifies controlled lab traffic
9. Creates structured Python records
10. Validates traffic-type counts
11. Exports the enriched dataset to CSV

## Input Fields

The Apache custom security log contains 11 fields:

```text
Source IP
Timestamp
HTTP Method
URL
Query String
Protocol
Status Code
Bytes Transferred
Response Time
Referrer
User-Agent
```

## Record Validation

Each raw record is validated using the expected field count:

```python
fields = line.strip().split("|")

if len(fields) == 11:
    valid_records += 1
else:
    invalid_records += 1
```

Final validation result:

```text
Total records: 1000
Valid records: 1000
Invalid records: 0
```

## Timestamp Conversion

Apache timestamps are converted using:

```python
datetime.strptime(
    fields[1],
    "%Y-%m-%dT%H:%M:%S%z"
)
```

This allows additional analytical fields such as:

- Date
- Hour

to be derived from the original event timestamp.

## HTTP Status Categories

The parser groups HTTP response codes into analytical categories:

```text
200–299 → Success
400–499 → Client Error
500–599 → Server Error
Other   → Other
```

This simplifies later analysis in SQL Server and visualization tools.

## Controlled Traffic Classification

The lab generated traffic with known User-Agent labels.

The parser maps these controlled labels to traffic categories:

```text
Normal-User-Dataset   → Normal
Bot-Dataset-Test      → Bot
Recon-Dataset-Test    → Recon
Auth-Failure-Dataset  → Auth Failure
Server-Error-Dataset  → Server Error
```

Any unmatched value is classified as:

```text
Unknown
```

### Important Limitation

This classification logic is designed for the controlled laboratory dataset.

The User-Agent labels provide known ground truth for validating the analytics pipeline. They should not be interpreted as a production bot-detection or threat-detection engine.

User-Agent values can be modified or spoofed in real environments, so production detection would require correlation with additional behavioral and security signals.

## Structured Output

Each parsed record contains:

```text
source_ip
timestamp
date
hour
http_method
url
query_string
protocol
status_code
status_category
bytes_transferred
response_time_ms
referrer
user_agent
traffic_type
```

## Traffic Count Validation

The Python analysis confirmed:

```text
Normal       : 600
Bot          : 150
Recon        : 100
Auth Failure : 100
Server Error : 50
```

Total:

```text
1000 requests
```

## CSV Export

The processed records are exported as:

```text
security_analytics_cleaned.csv
```

Python's built-in `csv.DictWriter` is used to create the structured CSV file.

Timestamp and date objects are converted to ISO-compatible strings before export.

## Portable Path Handling

The script uses Python's `pathlib` module:

```python
data_dir = Path.home() / "web-security-analytics" / "data"
```

This avoids hard-coding a specific Linux username in the source code and makes the script easier to reuse across different user environments.

## Run the Parser

From the Linux terminal:

```bash
python3 ~/web-security-analytics/scripts/parser.py
```

Successful execution should confirm:

```text
Total records: 1000
Valid records: 1000
Invalid records: 0
```

and display the verified traffic-category counts before exporting the cleaned CSV.

## Role in the Analytics Pipeline

```text
Apache Security Log
        |
        v
    parser.py
        |
        +--> Validate Records
        |
        +--> Parse Fields
        |
        +--> Convert Data Types
        |
        +--> Derive Fields
        |
        +--> Classify Controlled Traffic
        |
        v
security_analytics_cleaned.csv
        |
        v
    SQL Server
```

## Skills Demonstrated

- Python scripting
- Security log parsing
- Data validation
- Structured data transformation
- Timestamp handling
- Conditional classification logic
- CSV processing
- Security analytics data preparation
