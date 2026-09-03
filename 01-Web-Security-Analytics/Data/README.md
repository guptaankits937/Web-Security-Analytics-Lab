# Web Security Analytics Dataset

This directory documents the dataset used in the Web Security Analytics & Bot Traffic Investigation project.

The dataset was generated in a controlled laboratory environment to test the complete security analytics workflow from Apache logging through Bash, Python, SQL Server, Power BI, and Tableau.

## Dataset Overview

The final dataset contains:

```text
1000 HTTP requests
```

Controlled traffic distribution:

```text
Normal        600
Bot           150
Recon         100
Auth Failure  100
Server Error   50
```

## Traffic Generation

Traffic was intentionally generated against controlled Apache web application endpoints.

The dataset includes examples of:

- Normal application browsing
- Automated bot-style requests
- Reconnaissance activity
- Authentication failures
- Controlled server-error responses

These traffic categories provide known laboratory ground truth for validating the analytics pipeline.

## Raw Log Format

Apache was configured to generate a custom pipe-delimited security log.

Each raw record contains 11 fields:

```text
Source IP
Timestamp
HTTP Method
URL
Query String
Protocol
HTTP Status Code
Bytes Transferred
Response Time
Referrer
User-Agent
```

Conceptual format:

```text
source_ip|timestamp|method|url|query|protocol|status|bytes|response_time|referrer|user_agent
```

## HTTP Status Distribution

The completed dataset contains:

```text
HTTP 200    760 requests    76%
HTTP 401    100 requests    10%
HTTP 403     10 requests     1%
HTTP 404     80 requests     8%
HTTP 500     50 requests     5%
```

## Processed Dataset

Python was used to parse and enrich the raw security log.

The processed CSV contains:

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

Output filename:

```text
security_analytics_cleaned.csv
```

## Derived Fields

The Python processing stage added analytical fields including:

### Date

Derived from the original event timestamp.

### Hour

Used for time-based traffic analysis.

### Status Category

HTTP response codes were grouped into:

```text
Success
Client Error
Server Error
Other
```

### Traffic Type

Controlled laboratory User-Agent labels were mapped to:

```text
Normal
Bot
Recon
Auth Failure
Server Error
Unknown
```

## Dataset Validation

Python validation confirmed:

```text
Total records:   1000
Valid records:   1000
Invalid records: 0
```

The dataset was later validated again using SQL Server, Power BI, and Tableau.

## Important Limitation

The traffic classifications in this dataset are based on intentionally assigned laboratory labels.

They provide known ground truth for testing the analytics workflow.

They must not be interpreted as a production bot-detection or threat-classification system.

In real-world security monitoring, classification would require correlation with additional signals such as:

- Request behavior
- Authentication activity
- Network telemetry
- Identity information
- Application context
- Threat intelligence
- Historical baselines

## Public Repository Data Handling

The original laboratory logs and full processed dataset may contain internal environment information such as:

- Internal IP addresses
- Local usernames
- Hostnames
- Environment-specific metadata

For this reason, the original raw dataset is retained locally and is not published directly in the public repository.

Any dataset published publicly should first be sanitized or replaced with a representative sanitized sample.

## Data Integrity

The original frozen dataset is retained locally as read-only investigation evidence.

Analysis was performed using a separate working copy so that the original captured dataset was not modified during processing.
