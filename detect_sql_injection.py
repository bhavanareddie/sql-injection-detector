import re

# Define common SQL injection patterns
sql_patterns = [
    r"(?i)(\%27)|(\')|(\-\-)|(\%23)|(#)",       # SQL meta characters
    r"(?i)(\bOR\b|\bAND\b).*(=|LIKE)",          # OR/AND logic
    r"(?i)UNION(\s+ALL)?\s+SELECT",             # UNION SELECT
    r"(?i)(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|EXEC)",  # SQL keywords
    r"(?i)(\bWHERE\b).*(\=)",                   # WHERE clause
    r"(?i)1\s*=\s*1",                           # Always-true condition
    r"(?i)(--|#|\/\*)",                         # Comments
]

# Function to detect SQL injection patterns
def detect_sql_injection(log_file):
    with open(log_file, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    suspicious_requests = []

    for line_number, line in enumerate(lines, start=1):
        for pattern in sql_patterns:
            if re.search(pattern, line):
                suspicious_requests.append((line_number, line.strip()))
                break  # Stop after the first match

    if suspicious_requests:
        print(" Potential SQL Injection Attempts Detected:\n")
        for line_number, request in suspicious_requests:
            print(f"[Line {line_number}] {request}")
    else:
        print(" No SQL injection patterns detected.")

# Call the function with the file in the same folder
detect_sql_injection("access.log")
