# Bash Log Analysis

This directory documents the Bash and Linux command-line techniques used to investigate the Apache security analytics dataset.

The Bash phase was used for rapid security triage before the data was processed with Python and imported into SQL Server.

## Dataset

Working log file:

```text
security_access-1000-working.log
```

The dataset contained 1,000 controlled HTTP requests.

## Commands and Techniques Used

### Count Total Records

```bash
wc -l security_access-1000-working.log
```

**Purpose:**  
Verify the total number of records in the working security dataset.

**Result:**  
1,000 records.

---

### Extract HTTP Status Codes

```bash
cut -d'|' -f7 security_access-1000-working.log
```

**Purpose:**  
Extract the seventh pipe-delimited field, which contains the HTTP status code.

---

### Count HTTP Status Distribution

```bash
cut -d'|' -f7 security_access-1000-working.log | sort | uniq -c
```

**Purpose:**  
Group identical HTTP status codes and count their frequency.

Verified distribution:

```text
760 200
100 401
10  403
80  404
50  500
```

---

### Extract Requested URLs

```bash
cut -d'|' -f4 security_access-1000-working.log
```

**Purpose:**  
Extract the requested URL field for path-frequency analysis.

---

### Count Requested URLs

```bash
cut -d'|' -f4 security_access-1000-working.log | sort | uniq -c | sort -nr
```

**Purpose:**  
Identify the most frequently requested application resources.

This analysis showed that `/login/index.html` was the most frequently requested URL.

---

### Extract User-Agent Values

```bash
cut -d'|' -f11 security_access-1000-working.log
```

**Purpose:**  
Extract the User-Agent field from the custom Apache security log.

User-Agent analysis was used as one controlled lab indicator when comparing Normal, Bot, Recon, Authentication Failure, and Server Error traffic.

User-Agent values were not treated as proof of malicious activity because they can be spoofed.

---

### Filter Specific Traffic

```bash
grep "pattern" security_access-1000-working.log
```

**Purpose:**  
Filter log records containing a specific URL, status code, User-Agent value, or controlled traffic indicator.

`grep` was used throughout the investigation for targeted log review.

---

### Count Matching Records

```bash
grep "pattern" security_access-1000-working.log | wc -l
```

**Purpose:**  
Count how many log records matched a selected investigation condition.

This technique was used when validating controlled traffic categories.

---

### Sort and Count Unique Values

```bash
sort | uniq -c | sort -nr
```

**Purpose:**  
Aggregate repeated values and order the results from highest to lowest frequency.

This pattern was useful for:

- URL analysis
- HTTP status analysis
- User-Agent analysis
- Traffic-frequency analysis

---

### Time-Based Analysis

`awk` was used to extract and group timestamp information into minute-level intervals.

This supported:

- Requests-per-minute analysis
- Identification of the busiest minutes
- Authentication-failure peak analysis
- Reconnaissance timeline analysis
- Correlation of traffic type, URL, and HTTP status

The busiest observed minute was:

```text
2026-08-30 13:22 UTC
```

with:

```text
23 requests
```

All 23 requests during that minute belonged to the controlled Bot traffic category.

## Key Findings from Bash Analysis

The Bash investigation verified:

- Total dataset size: 1,000 requests
- Normal traffic: 600
- Bot traffic: 150
- Recon traffic: 100
- Authentication Failure traffic: 100
- Server Error traffic: 50
- HTTP 200 responses: 760
- HTTP 401 responses: 100
- HTTP 403 responses: 10
- HTTP 404 responses: 80
- HTTP 500 responses: 50
- Highest one-minute request volume: 23

## Analyst Note

Bash provided a fast way to inspect and validate raw security logs directly on the Linux server.

The command-line findings were later compared with Python, SQL Server, Power BI, and Tableau results to ensure that the analysis remained consistent across the complete project workflow.
