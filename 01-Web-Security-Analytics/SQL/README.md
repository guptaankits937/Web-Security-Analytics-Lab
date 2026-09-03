# SQL Server Security Analytics

This directory documents the SQL Server stage of the Web Security Analytics & Bot Traffic Investigation project.

The cleaned Python dataset was imported into SQL Server for structured validation, aggregation, correlation, and preparation for Power BI and Tableau.

## Database

```text
WebSecurityAnalytics
```

## Primary Analysis Table

```text
dbo.WebTrafficLogs
```

The final table contains:

```text
1000 records
```

## Data Pipeline

```text
Apache Security Log
        |
        v
Python Parser
        |
        v
security_analytics_cleaned.csv
        |
        v
SQL Server Staging
        |
        v
Data-Type Validation
        |
        v
dbo.WebTrafficLogs
        |
        +----------------+
        |                |
        v                v
     Power BI         Tableau
```

## Staging and Validation

The cleaned CSV was first imported into a staging table.

During the import workflow, the staging object was created with the physical name:

```text
dbo.dbo.WebTrafficLogs_Staging
```

This naming issue resulted from the import configuration and was retained only as a staging object.

The final analysis table was created separately as:

```text
dbo.WebTrafficLogs
```

## Data-Type Validation

Before loading the final table, conversion checks were performed for:

- Timestamp
- Date
- Hour
- HTTP Status Code
- Bytes Transferred
- Response Time

The validation returned:

```text
0 invalid timestamp values
0 invalid date values
0 invalid hour values
0 invalid status-code values
0 invalid byte values
0 invalid response-time values
```

This confirmed that the 1,000 imported records could be safely converted into the required SQL data types.

## Final Dataset Validation

The final SQL table contained:

```text
1000 rows
```

Traffic-type distribution:

```text
Normal        600
Bot           150
Recon         100
Auth Failure  100
Server Error   50
```

## HTTP Status Distribution

SQL analysis confirmed:

```text
200  760
401  100
403   10
404   80
500   50
```

Percentage distribution:

```text
200  76%
401  10%
403   1%
404   8%
500   5%
```

## Traffic and Status Correlation

Traffic categories were correlated with HTTP status codes to understand how the controlled request types behaved.

Examples included:

- Normal application requests
- Automated Bot traffic
- Reconnaissance requests
- Authentication failures
- Controlled server errors

This provided a structured way to compare behavioral categories with application responses.

## Busiest Minute Analysis

Minute-level SQL analysis identified the busiest period as:

```text
2026-08-30 13:22 UTC
```

Request count:

```text
23
```

All requests during this minute belonged to the controlled:

```text
Bot
```

traffic category.

The primary requested resource during this period was:

```text
/login/index.html
```

with HTTP status:

```text
200
```

An HTTP 200 response in this project represents successful delivery of the static login page and does not indicate a successful user authentication.

## Reconnaissance Analysis

The 100 controlled Recon requests produced:

```text
80 x HTTP 404
10 x HTTP 403
10 x HTTP 200
```

The combination of repeated requests to multiple paths and a high number of 404 responses was used as a controlled reconnaissance pattern in the laboratory dataset.

## Response-Time Analysis

Response-time values were also reviewed in SQL Server.

They were treated as a secondary analytical signal rather than a primary security indicator.

Approximate observed values included:

```text
Traffic Type    Average (ms)    Maximum (ms)
Recon               2.92            292
Normal              1.06            294
Auth Failure        0.29             29
Bot                 0                 0
Server Error        0                 0
```

## Tableau Reporting View

A SQL view was created to provide Tableau with a compatible timestamp representation.

```sql
CREATE OR ALTER VIEW dbo.vw_WebTrafficLogs_Tableau
AS
SELECT
    log_id,
    source_ip,
    CAST(
        SWITCHOFFSET([timestamp], '+00:00')
        AS DATETIME2(0)
    ) AS event_timestamp_utc,
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
```

The view resolved Tableau compatibility issues with the original `DATETIMEOFFSET` field while preserving the event time in UTC.

## Analytical Use

SQL Server was used to:

- Validate imported records
- Verify data types
- Confirm traffic-category counts
- Analyze HTTP status distribution
- Identify top requested URLs
- Correlate traffic type with status codes
- Analyze reconnaissance behavior
- Identify busiest traffic periods
- Review authentication-failure peaks
- Prepare structured data for visualization

## Key Finding

The SQL results matched the earlier Bash and Python analysis.

This cross-tool consistency provided confidence that the dataset remained accurate throughout the processing pipeline.

## Skills Demonstrated

- Microsoft SQL Server
- Data import and staging
- Data-type validation
- SQL querying
- Aggregation and grouping
- Security-event correlation
- Time-based analysis
- Data-quality validation
- Reporting-view creation
- Security analytics
