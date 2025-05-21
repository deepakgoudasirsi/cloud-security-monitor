import os
from typing import List

# Mock AWS Configuration
AWS_ACCOUNTS = [
    "dev-account-123",
    "prod-account-456",
    "staging-account-789"
]

# Monitoring Configuration
SCAN_INTERVAL = 5  # 5 seconds for testing (changed from 3600)
RISK_SCORE_THRESHOLD = 7.0

# Severity Levels
SEVERITY_LEVELS = {
    "critical": 9.0,
    "high": 7.0,
    "medium": 4.0,
    "low": 1.0,
}

# Report Configuration
REPORT_TEMPLATES = {
    "summary": "templates/summary_report.html",
    "detailed": "templates/detailed_report.html",
}

# Cache Configuration
CACHE_DURATION = 300  # 5 minutes 