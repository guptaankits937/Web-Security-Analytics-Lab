# Evidence Screenshots

This directory contains sanitized evidence captured during the Web Security Analytics & Bot Traffic Investigation project.

The screenshots document the end-to-end workflow from Apache web server configuration and controlled traffic generation through Bash log analysis, Python processing, SQL Server investigation, Power BI visualization, and Tableau analysis.

## Evidence Index

| # | Screenshot | Evidence |
|---|---|---|
| 01 | `01-Network-Interfaces` | Network interface verification for the controlled Ubuntu web-server environment. |
| 02 | `02-Apache-Service-Running` | Apache HTTP Server service verified as running. |
| 03 | `03-Apache-HTTP-200-Test` | Successful HTTP 200 response confirming Apache availability. |
| 04 | `04-Apache-Default-Access-Log` | Default Apache access log inspected before custom analytics logging was introduced. |
| 05 | `05-Apache-GET-Request-Logged` | Standard HTTP GET request successfully recorded in the Apache log. |
| 06 | `06-Apache-Logging-Configuration-Check` | Existing Apache logging configuration inspected before changes. |
| 07 | `07-Custom-Security-Log-Config` | Custom security analytics log configuration added to Apache. |
| 08 | `08-Apache-Config-Test-Syntax-OK` | Apache configuration validation returned Syntax OK. |
| 09 | `09-Custom-Security-Analytics-Log` | Custom pipe-delimited security analytics log successfully generated. |
| 10 | `10-Windows-Client-Request-404` | External Windows client request recorded with an HTTP 404 response. |
| 11 | `11-Test-Web-Endpoints-Created` | Controlled web application test endpoints created for traffic generation. |
| 12 | `12-Login-Endpoint-HTTP-200` | Login test endpoint successfully returned HTTP 200. |
| 13 | `13-Endpoint-Redirect-Test` | Trailing-slash redirect behavior verified for a test endpoint. |
| 14 | `14-All-Test-Endpoints-HTTP-200` | Login, admin, products, and dashboard endpoints validated with HTTP 200 responses. |
| 15 | `15-Normal-Traffic-Baseline` | Normal-user baseline traffic recorded across the controlled application endpoints. |
| 16 | `16-Bot-Traffic` | Controlled automated bot-style traffic generated against the web application. |
| 17 | `17-Request-Count` | Initial request-count verification performed on the security analytics log. |
| 18 | `18-Request-Frequency-Count` | Request-frequency analysis performed on the captured traffic. |
| 19 | `19-Request-Frequency-Count-Normal-User` | Frequency analysis performed specifically for normal-user traffic. |
| 20 | `20-Recon-Test-Frequency-Code-Status` | Controlled reconnaissance traffic analyzed by request frequency and HTTP status. |
| 21 | `21-Frequency-count-Recon-Test` | Request-count verification performed for the Recon test traffic. |
| 22 | `22-Password-File-Permission-Change` | File permissions adjusted for the Apache Basic Authentication password file. |
| 23 | `23-Apache-Basic-Auth-Configuration` | Apache Basic Authentication configured for the protected test endpoint. |
| 24 | `24-401-User-Test` | Controlled unauthorized request verified with HTTP 401. |
| 25 | `25-Auth-Failure-Test-Count` | Authentication-failure test requests counted. |
| 26 | `26-Auth-Failure-Test-Count-Code` | Authentication-failure requests correlated with their HTTP response code. |
| 27 | `27-Auth-Failure-Test-Frequency-Count` | Frequency analysis performed for authentication-failure traffic. |
| 28 | `28-Rewrite-Module-Enabled` | Apache rewrite module enabled for controlled server-error testing. |
| 29 | `29-HTTP-500-Rewrite-Configuration` | Rewrite configuration created to generate controlled HTTP 500 responses. |
| 30 | `30-Apache-500-Config-Syntax-OK` | Apache configuration syntax validated after the controlled HTTP 500 configuration. |
| 31 | `31-Controlled-HTTP-500-Test` | Controlled endpoint successfully returned an HTTP 500 response. |
| 32 | `32-HTTP-500-Security-Log-Evidence` | Controlled HTTP 500 response captured in the security analytics log. |
| 33 | `33-Server-Error-Test-Request-Count` | Controlled server-error requests counted. |
| 34 | `34-Server-Error-Test-Status-Distribution` | HTTP status distribution verified for the server-error test traffic. |
| 35 | `35-Server-Error-Test-Request-Frequency` | Request-frequency analysis performed for controlled server-error traffic. |
| 36 | `36-Normal-Traffic-Dataset-600-Requests` | Final Normal traffic category verified at 600 requests. |
| 37 | `37-Bot-Traffic-Dataset-150-Requests` | Final Bot traffic category verified at 150 requests. |
| 38 | `38-Recon-Traffic-Dataset-100-Requests` | Final Recon traffic category verified at 100 requests. |
| 39 | `39-Auth-Failure-Dataset-100-Requests` | Final Authentication Failure category verified at 100 requests. |
| 40 | `40-Final-Dataset-1000-Requests` | Final security analytics dataset verified at 1,000 HTTP requests. |
| 41 | `41-Final-Dataset-Category-Verification` | All controlled traffic categories verified against the final dataset. |
| 42A | `42A-HTTP-Status-Code-Distribution` | HTTP status-code counts verified: 200, 401, 403, 404, and 500. |
| 42B | `42B-HTTP-Status-Code-Percentage` | HTTP status-code counts converted into percentage distribution. |
| 43 | `43-Top-Requested-URLs` | Most frequently requested URLs identified from the final dataset. |
| 44 | `44-User-Agent-Distribution` | User-Agent distribution analyzed across the captured traffic. |
| 45 | `45-Requests-Per-Source-IP` | Request counts grouped by source IP address. |
| 46 | `46-Requests-Per-Minute-1` | Traffic grouped into one-minute intervals for time-based analysis. |
| 47 | `47-Top-10-Busiest-Minutes` | Ten busiest traffic minutes identified from the dataset. |
| 48 | `48-Busiest-Minute-Traffic-Type` | Busiest minute correlated with the controlled traffic category. |
| 49 | `49-Busiest-Minute-URL-Status-Correlation` | Busiest-minute requests correlated with URL and HTTP status. |
| 50 | `50-Auth-Failure-Busiest-Minutes` | Peak periods of authentication-failure traffic identified. |
| 51 | `51-Recon-Status-Code-Distribution` | HTTP status-code distribution analyzed for Recon traffic. |
| 52 | `52-Top-Recon-URLs` | Most frequently requested reconnaissance URLs identified. |
| 53 | `53-Recon-URL-Status-Correlation` | Reconnaissance URLs correlated with their HTTP response codes. |
| 54 | `54-Python-Read-First-Line` | Python successfully read the first record from the raw security log. |
| 55 | `55-Python-Log-Line-Split-11-Fields` | Raw Apache log record successfully split into the expected 11 fields. |
| 56 | `56-Python-Parsed-Log-Record` | Apache log record parsed into a structured Python representation. |
| 57 | `57-Python-1000-Record-Validation` | Python validated 1,000 total records, 1,000 valid records, and zero invalid records. |
| 58 | `58-Python-Structured-Record-Output` | Structured Python dictionary output verified for a parsed security-log record. |
| 59 | `59-Python-Data-Type-and-Timestamp-Conversion` | Data-type and timestamp conversion implemented during Python processing. |
| 60 | `60-Python-Status-Category-Derived-Field` | Derived HTTP status-category field created in Python. |
| 61 | `61-Python-Date-and-Hour-Derived-Fields` | Date and hour analytical fields derived from request timestamps. |
| 62 | `62-Python-Traffic-Type-Classification` | Controlled traffic-type classification implemented during Python enrichment. |
| 63 | `63-Python-Traffic-Type-Count-Validation` | Python traffic-category counts validated against the expected dataset. |
| 64 | `64-Python-CSV-Export-Validation` | Cleaned and enriched dataset successfully exported to CSV and validated. |
| 65 | `65-SQL-Server-Localhost-Connection` | Successful local connection established to SQL Server. |
| 66 | `66-SQL-WebSecurityAnalytics-Database-Created` | WebSecurityAnalytics database successfully created. |
| 67 | `67-SQL-WebTrafficLogs-Table-Created` | WebTrafficLogs analysis table successfully created. |
| 68 | `68-SQL-Staging-Table-1000-Rows-Validation` | SQL staging import validated with all 1,000 dataset rows. |
| 69 | `69-SQL-Staging-Data-Type-Validation` | Staging values checked for invalid timestamp, date, hour, status, byte, and response-time conversions. |
| 70 | `70-SQL-Final-Table-Sample-Validation` | Sample records from the final typed WebTrafficLogs table validated successfully. |
| 71 | `71-SQL-Traffic-Type-Distribution` | SQL query confirmed the expected distribution of all traffic categories. |
| 72 | `72-SQL-Traffic-Type-Status-Correlation` | SQL analysis correlated traffic categories with HTTP response codes. |
| 73 | `73-PowerBI-Web-Security-Analytics-Dashboard` | Final Power BI Web Application Security Analytics dashboard. |
| 74 | `74-PowerBI-Interactive-Client-View` | Interactive Power BI client view with traffic-type filtering. |
| 75 | `75-Tableau-Web-Security-Analytics-Dashboard` | Final Tableau Web Application Security Analytics dashboard. |

## Evidence Handling

IP addresses, usernames, hostnames, credentials, passwords, and other unnecessary internal environment details are sanitized before screenshots are published.

The original unsanitized screenshots and raw laboratory evidence are retained locally and are not included in the public repository.
