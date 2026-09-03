# Web Security Analytics Architecture

This document describes the end-to-end architecture used in the Web Security Analytics & Bot Traffic Investigation project.

## Architecture Flow

```text
Windows Client
Normal + Controlled Security-Test Traffic
        |
        v
Ubuntu Server
Apache HTTP Server
        |
        v
Custom Apache Security Access Log
        |
        +-------------------+
        |                   |
        v                   v
Bash Analysis          Python Processing
Quick Triage           Parse / Clean / Enrich
        |                   |
        +---------+---------+
                  |
                  v
            Structured CSV
                  |
                  v
             SQL Server
        WebSecurityAnalytics
                  |
                  v
        Security Analysis Queries
                  |
          +-------+-------+
          |               |
          v               v
       Power BI        Tableau
    Main Dashboard   Secondary Dashboard
          |               |
          +-------+-------+
                  |
                  v
          Security Findings
```

## Data Collection Layer

Apache HTTP Server was used as the primary source of web traffic evidence.

A custom security log captured:

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

## Analysis Layer

### Bash

Bash command-line utilities were used for rapid investigation of raw log data, including:

- Request counting
- HTTP status analysis
- URL frequency analysis
- User-Agent analysis
- Requests-per-minute analysis
- Authentication-failure analysis
- Reconnaissance analysis

### Python

Python was used to transform raw Apache log records into structured analytical data.

Processing included:

- Log parsing
- Field validation
- Timestamp conversion
- Data cleaning
- Derived fields
- Traffic classification
- CSV export

## Data Layer

The processed dataset was imported into Microsoft SQL Server.

Database:

`WebSecurityAnalytics`

Primary analysis table:

`dbo.WebTrafficLogs`

Tableau reporting view:

`dbo.vw_WebTrafficLogs_Tableau`

SQL Server provided a structured layer for validating and correlating the security data before visualization.

## Visualization Layer

### Power BI

Power BI was used as the primary analytics dashboard.

It visualized:

- Total Requests
- Bot Requests
- Authentication Failures
- Suspicious Requests
- Traffic Type Distribution
- HTTP Status Distribution
- Top Requested URLs
- Requests Over Time

### Tableau

Tableau was used as a secondary visualization platform to validate and present:

- Traffic Type Distribution
- HTTP Status Distribution
- Top Requested URLs
- Requests Over Time

## Investigation Principle

The project does not treat a single indicator as proof of malicious activity.

Traffic classification and findings were evaluated using multiple signals such as:

- Request frequency
- URL patterns
- HTTP status codes
- User-Agent values
- Authentication behavior
- Timeline patterns

The controlled traffic labels provide known lab ground truth and should not be interpreted as a production bot-detection system.

## Data Flow Summary

```text
Collect
   ↓
Parse
   ↓
Clean
   ↓
Enrich
   ↓
Store
   ↓
Analyze
   ↓
Visualize
   ↓
Investigate
   ↓
Communicate Findings
```
