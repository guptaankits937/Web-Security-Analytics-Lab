# Power BI Security Analytics Dashboard

This directory documents the Power BI stage of the Web Security Analytics & Bot Traffic Investigation project.

Power BI was used to convert the validated SQL Server dataset into an interactive security analytics dashboard for traffic monitoring, anomaly review, and investigation.

## Data Source

Power BI connected to:

```text
SQL Server
Database: WebSecurityAnalytics
Table: dbo.WebTrafficLogs
```

Connection mode:

```text
Import
```

The dataset contained:

```text
1000 web requests
```

## Dashboard Overview

The dashboard provides a consolidated view of:

- Total Requests
- Bot Requests
- Authentication Failures
- Suspicious Requests
- Traffic Type Distribution
- HTTP Status Code Distribution
- Top Requested URLs
- Requests Over Time

## Key Metrics

The main dashboard cards displayed:

```text
Total Requests        1000
Bot Requests           150
Auth Failures          100
Suspicious Requests    400
```

Suspicious Requests represents all controlled traffic categories except Normal traffic.

## DAX Measures

### Total Requests

```DAX
Total Requests =
COUNTROWS(WebTrafficLogs)
```

### Bot Requests

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

### Authentication Failures

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

### Suspicious Requests

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

## Minute-Level Time Analysis

A calculated column was created to group requests into one-minute intervals.

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

A display label was then created:

```DAX
Minute Label =
FORMAT(
    WebTrafficLogs[Minute Bucket],
    "HH:mm"
)
```

The Minute Label was used as text where required to avoid unwanted automatic Date Hierarchy behavior.

## Dashboard Visuals

### Traffic Type Distribution

Displays the controlled traffic categories:

```text
Normal        600
Bot           150
Recon         100
Auth Failure  100
Server Error   50
```

### HTTP Status Code Distribution

Displays:

```text
200  760
401  100
403   10
404   80
500   50
```

### Top Requested URLs

The dashboard highlights the most frequently requested resources.

The highest-volume URL was:

```text
/login/index.html
```

with:

```text
279 requests
```

An HTTP 200 response for this endpoint represents successful delivery of the static login page and does not indicate successful authentication.

### Requests Over Time

Minute-level traffic visualization was used to identify spikes and unusual activity periods.

The busiest minute was:

```text
2026-08-30 13:22 UTC
```

with:

```text
23 requests
```

All 23 requests belonged to the controlled Bot traffic category.

## Interactive Filtering

A `traffic_type` slicer was added to allow the dashboard to be filtered by:

- Normal
- Bot
- Recon
- Auth Failure
- Server Error

This made it possible to investigate each controlled traffic pattern independently while keeping the dashboard metrics synchronized.

## Validation

The Power BI results were compared with the earlier:

- Bash analysis
- Python processing
- SQL Server queries

The counts remained consistent across all stages of the analytics pipeline.

## Dashboard Evidence

The project evidence includes:

```text
73-PowerBI-Web-Security-Analytics-Dashboard
74-PowerBI-Interactive-Client-View
```

Screenshot 73 documents the final dashboard.

Screenshot 74 demonstrates interactive traffic-type filtering.

## Important Limitation

The traffic categories in this project are based on controlled laboratory labels.

They are used to validate the analytics pipeline and should not be interpreted as a production threat-detection or bot-detection model.

Real-world detection would require correlation with additional behavioral, identity, network, application, and security telemetry.

## Repository Handling

The Power BI file uses Import mode, which can embed source data inside the `.pbix` file.

For this reason, the original project file should be reviewed and sanitized before being published publicly.

The public repository can safely demonstrate the dashboard through sanitized screenshots and documentation without exposing unnecessary internal laboratory data.

## Skills Demonstrated

- Microsoft Power BI
- SQL Server data integration
- DAX measures
- Calculated columns
- Interactive filtering
- Security dashboard design
- Time-series analysis
- Web traffic analysis
- Security data visualization
- Cross-tool validation
