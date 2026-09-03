# Web Security Analytics & Bot Traffic Investigation — Detailed Documentation

## Lab Information

**Lab Name:** Web Security Analytics & Bot Traffic Investigation  
**Project Folder:** `01-Web-Security-Analytics`  
**Repository:** `Web-Security-Analytics-Lab`  
**Lab Type:** End-to-End Web Security Analytics Project  
**Environment:** Controlled Home Lab  
**Status:** Completed  
**Version:** 1.0  

### Objective

The objective of this project was to build and investigate a complete web security analytics workflow using Apache, Linux, Bash, Python, SQL Server, Power BI, and Tableau.

The project was designed to develop practical experience in:

- Web server log analysis
- HTTP traffic investigation
- Bash-based security triage
- Python log parsing and enrichment
- SQL-based security analysis
- Bot-style traffic investigation
- Reconnaissance analysis
- Authentication-failure analysis
- Time-based traffic analysis
- Power BI visualization
- Tableau visualization
- Cross-tool result validation
- Evidence-based security conclusions

The project used controlled traffic so that suspicious patterns could be generated safely and analyzed without claiming that a real attack had occurred.

---

## Ticket Information

**Ticket ID:** N/A — Project-Based Security Investigation  
**Category:** Security Analytics / Web Traffic Investigation  
**Priority:** Lab Exercise  
**Source:** Apache Web Server Security Logs  
**Affected System:** Controlled Apache Web Server  
**Investigation Type:** Traffic Analysis and Security Monitoring  

### Investigation Question

Can raw Apache web logs be transformed into structured security analytics and used to identify controlled bot-style traffic, reconnaissance, authentication failures, server errors, and abnormal request-frequency patterns?

---

## Scenario

An Apache web server was configured in a controlled home-lab environment.

Several test resources were made available, including normal pages and security-relevant endpoints such as:

- `/`
- `/products/`
- `/login/`
- `/dashboard/`
- `/admin/`
- `/secure/`
- `/error-test/`

Controlled HTTP traffic was then generated from a Windows client.

The traffic included:

| Traffic Type | Requests |
|---|---:|
| Normal | 600 |
| Bot | 150 |
| Recon | 100 |
| Auth Failure | 100 |
| Server Error | 50 |
| **Total** | **1,000** |

The raw traffic was recorded by Apache using a custom pipe-delimited security log.

The investigation workflow was:

```text
Controlled HTTP Requests
        ↓
Apache Web Server
        ↓
Custom Security Access Log
        ↓
Bash Analysis
        ↓
Python Parsing and Enrichment
        ↓
Structured CSV
        ↓
SQL Server
        ↓
Security Analysis Queries
        ↓
Power BI + Tableau
        ↓
Analyst Findings
```

The objective was not simply to create dashboards. Each stage was used to validate the data and confirm that the same security findings could be reproduced across multiple tools.

---

## Environment

### Server Environment

- Ubuntu Server
- Apache HTTP Server
- VirtualBox virtual machine
- Custom Apache security logging
- Bash command-line utilities
- Python 3

### Client Environment

- Windows client system
- PowerShell
- Web browser
- Controlled HTTP request generation

### Analytics Environment

- SQL Server
- SQL Server Management Studio
- Power BI Desktop
- Tableau Desktop

### Project Data

Raw Apache security log:

```text
/var/log/apache2/security_access.log
```

Frozen 1,000-record dataset:

```text
/var/log/apache2/security_access-1000-dataset.log
```

Working copy:

```text
/home/ankit/web-security-analytics/data/security_access-1000-working.log
```

Python project directory:

```text
/home/ankit/web-security-analytics/
```

Processed CSV:

```text
security_analytics_cleaned.csv
```

SQL Server database:

```text
WebSecurityAnalytics
```

Final SQL analysis table:

```text
dbo.WebTrafficLogs
```

Tableau reporting view:

```text
dbo.vw_WebTrafficLogs_Tableau
```

### Custom Apache Security Log Fields

The custom log captured 11 fields:

1. Source IP
2. Timestamp
3. HTTP Method
4. URL
5. Query String
6. Protocol
7. Status Code
8. Bytes Transferred
9. Response Time
10. Referrer
11. User-Agent

Python processing later added analytical fields including:

- Date
- Hour
- Status Category
- Traffic Type

---

## Lab Duration

This was a multi-session practical project completed in a controlled home-lab environment.

The work was performed in multiple phases:

1. Apache configuration
2. Security endpoint testing
3. Controlled traffic generation
4. Dataset validation
5. Bash analysis
6. Python processing
7. SQL Server analysis
8. Power BI visualization
9. Tableau visualization
10. Cross-tool verification
11. Documentation

The project was intentionally completed phase by phase so that each component could be tested and verified before moving to the next stage.

---

## Commands Used

### 1. Apache Custom Security Logging

A custom Apache log format was configured:

```apache
LogFormat "%a|%{%Y-%m-%dT%H:%M:%S%z}t|%m|%U|%q|%H|%>s|%B|%{ms}T|%{Referer}i|%{User-Agent}i" security_analytics
CustomLog ${APACHE_LOG_DIR}/security_access.log security_analytics
```

### Purpose

This created a pipe-delimited security log containing the HTTP fields required for later parsing and analysis.

Important fields included:

- `%a` — client IP address
- `%m` — HTTP method
- `%U` — requested URL path
- `%q` — query string
- `%H` — HTTP protocol
- `%>s` — final HTTP response status
- `%B` — response size
- `%{ms}T` — response time in milliseconds
- `%{Referer}i` — HTTP referrer
- `%{User-Agent}i` — client User-Agent

Apache configuration was validated before continuing with traffic generation.

---

### 2. Bash Log Analysis

Bash was used for initial log investigation.

#### Count log records

```bash
wc -l security_access-1000-working.log
```

**Purpose:**  
Count the number of records in the dataset.

Expected result:

```text
1000
```

---

#### Filter records

```bash
grep "pattern" security_access-1000-working.log
```

**Purpose:**  
Search the raw log for specific HTTP status codes, URLs, User-Agent values, or traffic patterns.

---

#### Extract a pipe-delimited field

```bash
cut -d'|' -f7 security_access-1000-working.log
```

**Purpose:**  
Extract field 7 from the custom Apache log.

Because the custom log used `|` as the delimiter, `-d'|'` specifies the field separator and `-f7` selects the HTTP status-code field.

---

#### Count unique values

```bash
sort | uniq -c
```

**Purpose:**  
Group identical values and count how frequently each value occurred.

This pattern was used during analysis of:

- HTTP status codes
- URLs
- User-Agent values
- Traffic categories

---

#### Sort by frequency

```bash
sort -nr
```

**Purpose:**  
Sort numerical counts from highest to lowest so the most frequent traffic patterns appear first.

---

#### Display top results

```bash
head
```

**Purpose:**  
Display only the first results after sorting, useful for identifying the most frequently requested resources.

---

#### Structured field analysis

`awk` was used for field-based analysis and timestamp grouping.

This supported:

- Requests-per-minute analysis
- Traffic-frequency analysis
- URL/status correlation
- Busiest-period investigation

The Bash phase was used as the initial security-triage layer before moving the dataset into Python and SQL Server.

---

### 3. Python Log Processing

Python was used to transform each raw Apache log record into structured data.

The parser processed the 11 pipe-delimited raw fields and added analytical fields.

Processing included:

- Reading each log line
- Splitting records using the pipe delimiter
- Validating field count
- Parsing timestamps
- Cleaning values
- Creating date values
- Creating hour values
- Categorizing status codes
- Adding controlled traffic labels
- Writing structured CSV output

Python version used:

```text
Python 3.12.3
```

Permanent parser location:

```text
~/web-security-analytics/scripts/parser.py
```

The parser produced a cleaned CSV containing all 1,000 records.

The complete Python source is maintained separately in:

```text
Scripts/Python/
```

---

### 4. SQL Server Analysis

The processed CSV was imported into SQL Server.

Database:

```sql
WebSecurityAnalytics
```

Final table:

```sql
dbo.WebTrafficLogs
```

Security analysis was performed for:

- Traffic type
- HTTP status
- URL frequency
- Authentication failures
- Reconnaissance
- Traffic spikes
- Response times

### Tableau Reporting View

Tableau did not initially expose the SQL Server `DATETIMEOFFSET` timestamp correctly.

A reporting view was therefore created:

```sql
USE WebSecurityAnalytics;
GO

CREATE OR ALTER VIEW dbo.vw_WebTrafficLogs_Tableau
AS
SELECT
    log_id,
    source_ip,
    CAST(SWITCHOFFSET([timestamp], '+00:00') AS DATETIME2(0)) AS event_timestamp_utc,
    [date],
    [hour],
    http_method,
    [url],
    query_string,
    protocol,
    status_code,
    status_category,
    bytes_transferred,
    response_time_ms,
    referrer,
    user_agent,
    traffic_type
FROM dbo.WebTrafficLogs;
GO
```

### Purpose

`SWITCHOFFSET` preserves the timestamp in UTC.

`CAST(... AS DATETIME2(0))` converts the value into a Tableau-compatible SQL Server timestamp type.

This allowed Tableau to correctly analyze full chronological timestamps.

---

### 5. Power BI Calculations

Power BI was connected to:

```text
localhost
```

Database:

```text
WebSecurityAnalytics
```

Import mode was used.

#### Total Requests

```DAX
Total Requests =
COUNTROWS(WebTrafficLogs)
```

#### Bot Requests

```DAX
Bot Requests =
COALESCE(
    CALCULATE(
        COUNTROWS(WebTrafficLogs),
        KEEPFILTERS(WebTrafficLogs[traffic_type] = "Bot")
    ),
    0
)
```

#### Authentication Failures

```DAX
Auth Failures =
COALESCE(
    CALCULATE(
        COUNTROWS(WebTrafficLogs),
        KEEPFILTERS(WebTrafficLogs[traffic_type] = "Auth Failure")
    ),
    0
)
```

#### Suspicious Requests

```DAX
Suspicious Requests =
COALESCE(
    CALCULATE(
        COUNTROWS(WebTrafficLogs),
        KEEPFILTERS(WebTrafficLogs[traffic_type] <> "Normal")
    ),
    0
)
```

`KEEPFILTERS` was used so that the measures respected the interactive traffic-type slicer.

`COALESCE` was used to display `0` instead of a blank value where no matching records existed.

---

### Minute Bucket

```DAX
Minute Bucket =
DATE(
    YEAR(WebTrafficLogs[timestamp]),
    MONTH(WebTrafficLogs[timestamp]),
    DAY(WebTrafficLogs[timestamp])
)
+
TIME(
    HOUR(WebTrafficLogs[timestamp]),
    MINUTE(WebTrafficLogs[timestamp]),
    0
)
```

### Minute Label

```DAX
Minute Label =
FORMAT(
    WebTrafficLogs[Minute Bucket],
    "HH:mm"
)
```

These fields were used to create the request timeline.

---

### 6. Tableau Analysis

Tableau Desktop was connected directly to SQL Server.

The following worksheets were created:

1. Traffic Type Distribution
2. HTTP Status Code Distribution
3. Top 5 Requested URLs
4. Requests Over Time

The final dashboard combined all four visualizations.

For the time-series analysis, the timestamp was configured using a **continuous minute-level date value**.

This was important because using the discrete `MINUTE` date part grouped records only by minute-of-hour and produced an incorrect traffic peak.

The corrected continuous timeline produced a peak of:

```text
23 requests
```

matching SQL Server and Power BI.

---

## Verification Results

### Dataset Validation

Final record count:

```text
1000
```

Traffic-type distribution:

| Traffic Type | Count |
|---|---:|
| Normal | 600 |
| Bot | 150 |
| Recon | 100 |
| Auth Failure | 100 |
| Server Error | 50 |

Total:

```text
1000
```

---

### HTTP Status Validation

| HTTP Status | Count |
|---|---:|
| 200 | 760 |
| 401 | 100 |
| 403 | 10 |
| 404 | 80 |
| 500 | 50 |

Total:

```text
1000
```

---

### Traffic and Status Correlation

Verified relationships included:

```text
Auth Failure → 401 → 100
Bot          → 200 → 150
Normal       → 200 → 600
Recon        → 404 → 80
Recon        → 403 → 10
Recon        → 200 → 10
Server Error → 500 → 50
```

---

### Bot Traffic Verification

Controlled Bot requests:

```text
150
```

Primary target:

```text
/login/index.html
```

The busiest observed minute was:

```text
2026-08-30 13:22 UTC
```

Request count:

```text
23
```

All 23 requests during that minute were Bot traffic targeting:

```text
/login/index.html
```

with HTTP status:

```text
200
```

HTTP `200` indicates that the static page was served.

It does **not** represent successful authentication.

---

### Authentication Failure Verification

Controlled authentication failures:

```text
100
```

Target:

```text
/secure/
```

HTTP response:

```text
401
```

---

### Reconnaissance Verification

Recon requests:

```text
100
```

Distribution:

```text
80 × 404
10 × 403
10 × 200
```

This demonstrated repeated requests to missing, restricted, and administrative-style resources.

---

### Server Error Verification

Controlled server errors:

```text
50
```

HTTP response:

```text
500
```

These errors were intentionally generated for testing and did not represent an actual server crash.

---

### Cross-Tool Verification

The key dataset totals and traffic patterns were validated across:

- Bash
- Python
- SQL Server
- Power BI
- Tableau

The busiest-minute result of **23 requests** was reproduced across the structured analysis and visualization workflow.

---

## Troubleshooting

### 1. Linux Ownership and Permission Command

During Apache authentication configuration, ownership and permission commands were initially mixed up.

The issue was corrected by distinguishing:

- `chown` — changes file ownership
- `chmod` — changes file permissions

This reinforced the difference between Linux file ownership and permission modes.

---

### 2. Controlled HTTP 500 Testing

The initial controlled server-error test returned HTTP `404` instead of the expected `500`.

The issue was traced to a mismatch in the configured test path.

After correcting the Apache rewrite configuration and request path, the endpoint returned the intended controlled HTTP `500`.

This demonstrated the importance of validating test conditions before interpreting log evidence.

---

### 3. PowerShell Traffic Generation

Multi-line PowerShell commands caused execution issues during controlled traffic generation.

The commands were corrected and simplified so that the intended request loops executed successfully.

This highlighted the importance of validating traffic-generation scripts before trusting the resulting dataset.

---

### 4. SQL Server Staging Table Naming

During CSV import, a staging table was accidentally created with a duplicated schema-style name:

```text
dbo.dbo.WebTrafficLogs_Staging
```

The staging data was still validated successfully.

The final typed analysis table was created correctly as:

```text
dbo.WebTrafficLogs
```

All 1,000 rows were successfully inserted into the final table.

---

### 5. SQL Data-Type Validation

Before inserting the staging data into the final typed table, conversion validation was performed.

The results showed:

```text
InvalidTimestamp     0
InvalidDate          0
InvalidHour          0
InvalidStatusCode    0
InvalidBytes         0
InvalidResponseTime  0
```

This confirmed that the dataset could be safely loaded into the typed analysis table.

---

### 6. Power BI Date Hierarchy

Power BI automatically created a Date Hierarchy when the timestamp field was used.

This made minute-level visualization more difficult.

A custom minute bucket and text-based minute label were created so that the request timeline could be controlled explicitly.

---

### 7. Power BI Filter Context

The initial Bot and Authentication Failure measures did not behave correctly when the Traffic Type slicer was used.

The measures were updated using:

```text
KEEPFILTERS
```

This preserved the slicer filter context.

`COALESCE` was also added so that measures returned `0` instead of blank values.

---

### 8. Tableau DATETIMEOFFSET Compatibility

Tableau did not expose the original SQL Server `DATETIMEOFFSET` timestamp correctly.

A SQL reporting view was created using:

```sql
SWITCHOFFSET
```

and:

```sql
DATETIME2
```

This provided Tableau with a UTC timestamp that could be used for chronological analysis.

---

### 9. Tableau Minute Aggregation

The first Tableau timeline used a discrete Minute date part.

This grouped records by minute-of-hour rather than the complete timestamp and produced an incorrect peak of:

```text
35
```

The timeline was changed to a continuous minute-level date value.

The corrected result was:

```text
23 requests
```

which matched the SQL Server and Power BI analysis.

This was an important example of validating visualization results against the underlying data instead of assuming that a chart is automatically correct.

---

## Evidence

Evidence is maintained in:

```text
Screenshots/
```

The screenshot set documents major project milestones including:

- Apache configuration
- Custom security logging
- Endpoint validation
- Authentication testing
- Controlled HTTP 500 testing
- Dataset generation
- Dataset verification
- Bash analysis
- Python parsing
- SQL Server analysis
- Power BI dashboard
- Interactive Power BI client view
- Tableau dashboard

Only meaningful evidence is retained.

Public screenshots should be sanitized before upload.

Credentials, passwords, tokens, usernames, hostnames, and unnecessary internal network information should not be exposed.

---

## Lessons Learned

### Security Analysis

A single signal should not automatically be treated as proof of malicious activity.

Examples include:

- HTTP status code
- User-Agent
- Source IP
- Request frequency
- URL name

Security conclusions should be based on correlation between multiple indicators and the surrounding context.

---

### HTTP 200 Does Not Mean Successful Login

The controlled Bot traffic generated HTTP `200` responses for:

```text
/login/index.html
```

This only means that the static login page was served.

It does not mean that authentication succeeded.

---

### User-Agent Is Not Reliable Identity Evidence

Controlled User-Agent labels were useful as lab ground truth.

However, User-Agent strings can be modified or spoofed.

Real bot detection should therefore include behavioral features such as:

- Request frequency
- Timing
- URL patterns
- Session behavior
- Authentication behavior
- Response patterns
- Multiple correlated indicators

---

### Source IP Alone Was Insufficient

All controlled requests originated from the same actual laboratory client.

Therefore, source IP could not distinguish Normal, Bot, Recon, Authentication Failure, and Server Error traffic.

This demonstrated why security analysis should not depend on a single field.

---

### Visualization Must Be Validated

The Tableau discrete-minute issue demonstrated that a visually convincing dashboard can still contain analytically incorrect results.

Dashboard results should be checked against:

- Raw data
- Command-line analysis
- SQL queries
- Independent analytical tools

---

### Data Quality Comes Before Visualization

The project reinforced the importance of validating:

- Record counts
- Field structure
- Data types
- Timestamp handling
- Category values
- Import results

before creating dashboards or drawing security conclusions.

---

### Controlled Lab Labels Are Ground Truth, Not Detection Logic

The traffic categories in this project were deliberately generated and labeled.

They provide known ground truth for the lab.

They should not be presented as a production bot-detection system.

A production detection model would require behavioral rules, thresholds, correlation, baselining, and additional contextual data.

---

## Skills Demonstrated

- Apache HTTP Server administration
- Custom Apache logging
- Linux administration
- Bash
- Linux log analysis
- `grep`
- `cut`
- `awk`
- `sort`
- `uniq`
- `wc`
- Python
- Log parsing
- Data cleaning
- Data enrichment
- CSV processing
- SQL Server
- SQL Server Management Studio
- SQL data validation
- Security-focused SQL analysis
- HTTP status-code investigation
- URL-frequency analysis
- Bot-style traffic analysis
- Reconnaissance analysis
- Authentication-failure investigation
- Server-error analysis
- Time-series analysis
- Power BI
- DAX
- Tableau
- Data visualization
- Cross-tool validation
- Troubleshooting
- Evidence-based security investigation
- Technical documentation

---

## Outcome

The project successfully demonstrated an end-to-end web security analytics workflow.

A controlled 1,000-request dataset was generated and analyzed through multiple stages:

```text
Apache
   ↓
Bash
   ↓
Python
   ↓
SQL Server
   ↓
Power BI / Tableau
   ↓
Security Findings
```

The final analysis successfully identified and validated:

- 600 Normal requests
- 150 controlled Bot requests
- 100 Recon requests
- 100 Authentication Failure requests
- 50 controlled Server Error requests
- HTTP status-code distribution
- Frequently requested URLs
- Authentication-failure activity
- Reconnaissance patterns
- Bot-style request bursts
- A busiest-minute peak of 23 requests

The results were validated across multiple tools rather than relying on a single dashboard or query.

Most importantly, the project demonstrated evidence-based analyst reasoning by separating controlled suspicious behavior from unsupported claims of real compromise.

---

## Repository Information

**Repository:** `Web-Security-Analytics-Lab`  
**Section:** `01-Web-Security-Analytics`  
**Lab:** `Web Security Analytics & Bot Traffic Investigation`  
**Documentation:** `01-Web-Security-Analytics/Documentation/Web-Security-Analytics.md`  
**Screenshots:** `01-Web-Security-Analytics/Screenshots/`  
**Scripts:** `01-Web-Security-Analytics/Scripts/`  
**SQL:** `01-Web-Security-Analytics/SQL/`  
**Power BI:** `01-Web-Security-Analytics/Power-BI/`  
**Tableau:** `01-Web-Security-Analytics/Tableau/`  
**Status:** Completed  
**Version:** 1.0
