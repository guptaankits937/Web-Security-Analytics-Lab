# Tableau Security Analytics Dashboard

This directory documents the Tableau stage of the Web Security Analytics & Bot Traffic Investigation project.

Tableau was used as a secondary visualization platform to validate the SQL Server dataset and present key web security findings through an interactive dashboard.

## Data Source

Tableau connected to:

```text
SQL Server
Database: WebSecurityAnalytics
```

Connection mode:

```text
Live
```

A dedicated SQL reporting view was used:

```text
dbo.vw_WebTrafficLogs_Tableau
```

## Why a Reporting View Was Required

The original SQL Server table stored the event timestamp using a `DATETIMEOFFSET` data type.

Tableau compatibility with this timestamp format caused issues during time-series analysis.

To resolve this, a reporting view converted the timestamp into a Tableau-compatible UTC `DATETIME2` value.

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

This preserved the event time in UTC while providing a format Tableau could use reliably.

## Dashboard Overview

The final dashboard contains four primary visualizations:

- Traffic Type Distribution
- HTTP Status Code Distribution
- Top Requested URLs
- Requests Over Time

The upper section presents categorical traffic analysis, while the lower section provides a full-width timeline for time-based investigation.

## Traffic Type Distribution

The Tableau worksheet confirmed:

```text
Normal        600
Bot           150
Recon         100
Auth Failure  100
Server Error   50
```

Total:

```text
1000 requests
```

## HTTP Status Code Distribution

The dashboard confirmed:

```text
200  760
401  100
403   10
404   80
500   50
```

These values matched the Bash, Python, SQL Server, and Power BI analysis.

## Top Requested URLs

The five highest-volume URLs were:

```text
/login/index.html      279
/index.html            161
/dashboard/index.html  156
/products/index.html   154
/secure/               100
```

The `/login/index.html` endpoint was the most frequently requested resource.

An HTTP 200 response for this endpoint means that the static login page was successfully served. It does not represent a successful user authentication.

## Requests Over Time

Minute-level analysis was used to identify traffic spikes.

The busiest minute was:

```text
2026-08-30 13:22 UTC
```

with:

```text
23 requests
```

The requests during this period belonged to the controlled Bot traffic category.

## Tableau Time-Axis Troubleshooting

During the initial timeline configuration, Tableau used a discrete blue Minute field.

This grouped records by the minute component of the hour rather than maintaining the complete chronological event timeline.

The resulting visualization incorrectly produced a peak value of:

```text
35 requests
```

The issue was corrected by changing the timestamp visualization to a continuous green Minute axis.

After correction, the Tableau result matched the earlier analysis:

```text
23 requests
```

at the actual busiest minute.

## Cross-Tool Validation

The Tableau results were compared with:

- Bash log analysis
- Python processing
- SQL Server queries
- Power BI dashboard results

The final counts and traffic patterns remained consistent across the analytics workflow.

This helped validate that the transformations and visualizations had not changed the underlying analytical results.

## Dashboard Evidence

The final Tableau dashboard is documented in:

```text
75-Tableau-Web-Security-Analytics-Dashboard
```

Dashboard title:

```text
Web Application Security Analytics Dashboard
```

## Important Limitation

Traffic categories in this project come from controlled laboratory labels.

They provide known ground truth for testing the analytics pipeline and are not intended to represent a production bot-detection or threat-detection system.

In a real environment, additional behavioral and security telemetry would be required before classifying activity as malicious.

## Repository Handling

Tableau workbook files may contain connection details, local data-source metadata, or other environment-specific information.

The workbook should therefore be reviewed before public publication.

Sanitized dashboard screenshots and documentation can be used to demonstrate the analytical workflow without exposing unnecessary internal environment details.

## Skills Demonstrated

- Tableau Desktop
- SQL Server integration
- Live database connectivity
- Security data visualization
- Time-series analysis
- Dashboard development
- Data-source troubleshooting
- Timestamp compatibility handling
- Web traffic analysis
- Cross-tool result validation
