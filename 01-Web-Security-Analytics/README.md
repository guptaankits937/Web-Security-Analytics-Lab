# Web Security Analytics & Bot Traffic Investigation

## Overview

This project demonstrates a practical end-to-end web security analytics investigation using Apache, Bash, Python, SQL Server, Power BI, and Tableau.

The objective was to generate and analyze controlled HTTP traffic, identify suspicious request patterns, investigate bot-style activity, reconnaissance, authentication failures, and server errors, and transform raw Apache logs into structured security analytics.

The investigation was performed in a controlled home-lab environment using a dataset of 1,000 HTTP requests.

---

## Investigation Scenario

An Apache web server was configured with normal and security-relevant test endpoints.

Controlled HTTP traffic was generated to represent:

- Normal web browsing
- Bot-style automated traffic
- Web reconnaissance
- Authentication failures
- Server-error activity

The investigation focused on determining:

- Which traffic patterns were normal or security-relevant
- Which resources were most frequently requested
- Which HTTP response codes were returned
- Whether automated traffic bursts could be identified
- How authentication failures appeared in the logs
- How reconnaissance behavior could be identified
- How raw web logs could be processed and enriched
- Whether Bash, SQL Server, Power BI, and Tableau produced consistent findings
- What conclusions could be supported by the available evidence

---

## Investigation Workflow

### 1. Apache Security Logging

Apache was configured with a custom security access log.

The log captured:

- Source IP
- Timestamp
- HTTP Method
- URL
- Query String
- Protocol
- HTTP Status Code
- Bytes Transferred
- Response Time
- Referrer
- User-Agent

This provided structured security-relevant HTTP data for later investigation.

### 2. Controlled Traffic Generation

A controlled dataset of **1,000 HTTP requests** was generated.

Traffic distribution:

- 600 Normal
- 150 Bot
- 100 Recon
- 100 Auth Failure
- 50 Server Error

The traffic was deliberately generated for laboratory analysis and does not represent real malicious activity.

### 3. Bash Log Analysis

Linux command-line tools were used for initial investigation of the raw Apache logs.

The analysis included:

- Total request counting
- HTTP status-code analysis
- Requested URL frequency
- User-Agent frequency
- Requests-per-minute analysis
- Busiest-minute identification
- Reconnaissance-path analysis
- Authentication-failure analysis
- Correlation between traffic patterns, URLs, and HTTP responses

This demonstrated how Bash can support fast security triage before moving data into a structured analytics platform.

### 4. Python Log Processing

Python was used to parse the raw pipe-delimited Apache logs and prepare a clean analytical dataset.

Processing included:

- Reading raw log records
- Splitting records into structured fields
- Validating log structure
- Parsing timestamps
- Cleaning field values
- Adding date and hour fields
- Categorizing HTTP status codes
- Adding controlled traffic-type labels
- Exporting processed data to CSV

The final processed dataset contained **1,000 validated records**.

### 5. SQL Server Analysis

The cleaned dataset was imported into SQL Server for structured security analysis.

The final analysis table was:

`dbo.WebTrafficLogs`

SQL queries were used to investigate:

- Record counts
- Data-type validity
- Traffic-type distribution
- HTTP status distribution
- Traffic and HTTP-status correlation
- Requested URL frequency
- Authentication failures
- Reconnaissance activity
- Busiest traffic periods
- Requests per minute
- Response-time statistics

A separate reporting view was also created for Tableau:

`dbo.vw_WebTrafficLogs_Tableau`

This provided Tableau with a compatible UTC timestamp representation.

### 6. Power BI Analysis

Power BI was connected to SQL Server and used to build an interactive security analytics dashboard.

The dashboard included:

- Total Requests
- Bot Requests
- Authentication Failures
- Suspicious Requests
- Traffic Type Distribution
- HTTP Status Code Distribution
- Top Requested URLs
- Requests Over Time
- Interactive Traffic Type filtering

The dashboard was tested with traffic categories such as Bot and Recon to confirm that the visualizations and DAX measures responded correctly to filter context.

### 7. Tableau Analysis

Tableau was used as a second visualization platform.

The dashboard included:

- Traffic Type Distribution
- HTTP Status Code Distribution
- Top 5 Requested URLs
- Requests Over Time

A SQL reporting view was used to resolve compatibility between Tableau and the SQL Server `DATETIMEOFFSET` field.

The final timeline used a continuous minute-level timestamp to preserve actual chronological request activity.

### 8. Cross-Tool Validation

Results from Bash, SQL Server, Power BI, and Tableau were compared before reaching the final analyst conclusions.

The same major traffic patterns and request counts were successfully reproduced across the analysis workflow.

---

## Key Tools and Techniques

- Apache HTTP Server
- Ubuntu Linux
- Bash
- `grep`
- `cut`
- `awk`
- `sort`
- `uniq`
- `wc`
- Python
- Structured log parsing
- Data cleaning and enrichment
- SQL Server
- SQL Server Management Studio
- SQL security analysis
- Power BI Desktop
- DAX
- Tableau Desktop
- HTTP status-code analysis
- URL-frequency analysis
- Authentication-failure analysis
- Reconnaissance analysis
- Bot-traffic analysis
- Timeline analysis
- Cross-tool evidence validation

---

## Analyst Findings

The 1,000-request dataset contained:

- 600 Normal requests
- 150 Bot requests
- 100 Recon requests
- 100 Authentication Failure requests
- 50 Server Error requests

This resulted in:

- **600 normal requests**
- **400 controlled security-test requests**

HTTP status distribution was:

- `200` — 760 requests
- `401` — 100 requests
- `403` — 10 requests
- `404` — 80 requests
- `500` — 50 requests

### Bot Activity

The controlled Bot dataset contained **150 requests**.

The bot-style traffic primarily targeted:

`/login/index.html`

The busiest observed minute was:

`2026-08-30 13:22 UTC`

with:

**23 requests**

All 23 requests during that minute belonged to the controlled Bot traffic category and targeted `/login/index.html` with HTTP status `200`.

An HTTP `200` response only indicates that the static login page was successfully served. It does **not** demonstrate successful authentication.

### Authentication Failures

The dataset contained **100 authentication-failure requests**.

These requests targeted:

`/secure/`

and resulted in HTTP `401` responses.

Repeated authentication failures can be an important security signal when investigating password guessing, credential attacks, or incorrectly configured automated clients.

### Reconnaissance Activity

The controlled Recon dataset contained **100 requests**.

HTTP response distribution:

- 80 × `404`
- 10 × `403`
- 10 × `200`

Repeated requests to missing, restricted, and administrative-style paths demonstrated a reconnaissance-style request pattern.

### Server Errors

The dataset contained **50 HTTP 500 responses**.

These responses were intentionally generated through controlled Apache configuration for testing.

They do **not** represent evidence of a real application crash or successful attack.

### Traffic Source Limitation

All requests originated from one actual laboratory client system.

Therefore, source IP alone could not be used to distinguish the different traffic categories.

Controlled User-Agent values were used as lab ground truth for traffic generation, but User-Agent strings alone are not reliable bot-detection evidence because they can be spoofed.

The correct analyst conclusion was therefore to identify the dataset as **controlled security-test activity demonstrating bot-style traffic, reconnaissance, authentication failures, and server-error patterns**, rather than claiming a real attack or confirmed compromise.

---

## Evidence

Sanitized screenshots documenting the investigation are available in:

[`Screenshots/`](Screenshots/)

The evidence set covers the project from Apache logging and controlled traffic generation through Bash analysis, Python processing, SQL Server investigation, Power BI visualization, and Tableau analysis.

Screenshots intended for the public repository are sanitized to avoid exposing credentials, personal information, and unnecessary internal environment details.

---

## Detailed Investigation Report

Detailed technical documentation is maintained in:

[`Documentation/Web-Security-Analytics.md`](Documentation/Web-Security-Analytics.md)

The detailed documentation contains the practical commands, command purposes, processing logic, SQL queries, dashboard development, verification results, troubleshooting, limitations, and lessons learned during the project.

Additional project components are maintained in:

- [`Architecture/`](Architecture/)
- [`Data/`](Data/)
- [`Scripts/Bash/`](Scripts/Bash/)
- [`Scripts/Python/`](Scripts/Python/)
- [`SQL/`](SQL/)
- [`Power-BI/`](Power-BI/)
- [`Tableau/`](Tableau/)

---

## Skills Demonstrated

- Web server log analysis
- Web security analytics
- SOC-style investigation
- Apache security logging
- Linux command-line analysis
- Bash log filtering and aggregation
- Python log parsing
- Data cleaning and enrichment
- SQL Server analytics
- Security-focused SQL queries
- HTTP status-code investigation
- Bot-traffic analysis
- Reconnaissance analysis
- Authentication-failure analysis
- Timeline reconstruction
- Request-frequency analysis
- Power BI dashboard development
- DAX
- Tableau dashboard development
- Data visualization
- Cross-tool validation
- Technical troubleshooting
- Evidence-based security analysis
- Avoiding unsupported security conclusions

---

## Outcome

The project demonstrated a complete web security analytics workflow from HTTP traffic generation and Apache log collection through Bash analysis, Python processing, SQL Server investigation, and security visualization using Power BI and Tableau.

The project successfully validated a 1,000-request dataset across multiple analytical tools and identified controlled bot-style activity, reconnaissance patterns, authentication failures, server errors, and traffic spikes.

Most importantly, the investigation demonstrated evidence-driven security reasoning by distinguishing controlled suspicious traffic patterns from proof of a real attack or successful compromise.

---

## Repository Information

- **Repository:** Web-Security-Analytics-Lab
- **Section:** 01-Web-Security-Analytics
- **Lab:** Web Security Analytics & Bot Traffic Investigation
- **Status:** Completed
- **Environment:** Controlled Home Lab
- **Dataset:** 1,000 HTTP Requests
- **Platforms:** Apache, Bash, Python, SQL Server, Power BI, Tableau
- **Version:** 1.0
