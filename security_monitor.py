import time
import logging
from datetime import datetime
from typing import Dict, List
import json
from rich.console import Console
from rich.table import Table

from mock_security_data import MockSecurityData
from config import AWS_ACCOUNTS, SCAN_INTERVAL, RISK_SCORE_THRESHOLD

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
console = Console()

class SecurityMonitor:
    def __init__(self):
        self.mock_data = MockSecurityData()
        self.findings_history: Dict[str, List[Dict]] = {}

    def scan_account(self, account_id: str) -> Dict:
        """Scan a single AWS account for security findings."""
        logger.info(f"Scanning account: {account_id}")
        
        findings = {
            "critical": self.mock_data.get_mock_findings(account_id, severity="critical"),
            "high": self.mock_data.get_mock_findings(account_id, severity="high"),
            "risk_score": self.mock_data.get_mock_risk_score(account_id)
        }
        
        return findings

    def display_findings(self, account_id: str, findings: Dict):
        """Display findings in a rich table format."""
        table = Table(title=f"Security Findings for {account_id}")
        table.add_column("Severity", style="bold")
        table.add_column("Count", justify="right")
        table.add_column("Risk Score", justify="right")

        for severity in ["critical", "high"]:
            count = len(findings[severity])
            table.add_row(
                severity.upper(),
                str(count),
                str(findings["risk_score"].get("score", "N/A"))
            )

        console.print(table)

    def monitor_accounts(self):
        """Monitor all configured AWS accounts."""
        try:
            while True:
                for account_id in AWS_ACCOUNTS:
                    # Scan account
                    findings = self.scan_account(account_id)
                    
                    # Display results
                    self.display_findings(account_id, findings)
                    
                    # Update history
                    timestamp = datetime.now().isoformat()
                    if account_id not in self.findings_history:
                        self.findings_history[account_id] = []
                    self.findings_history[account_id].append({
                        "timestamp": timestamp,
                        "findings": findings
                    })

                logger.info(f"Sleeping for {SCAN_INTERVAL} seconds...")
                time.sleep(SCAN_INTERVAL)

        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
            self.save_summary()

    def save_summary(self):
        """Save the final summary to a JSON file."""
        summary = {
            "timestamp": datetime.now().isoformat(),
            "accounts": {}
        }

        for account_id in AWS_ACCOUNTS:
            if account_id in self.findings_history:
                latest_findings = self.findings_history[account_id][-1]
                summary["accounts"][account_id] = {
                    "critical_findings": len(latest_findings["findings"]["critical"]),
                    "high_findings": len(latest_findings["findings"]["high"]),
                    "risk_score": latest_findings["findings"]["risk_score"].get("score", 0)
                }

        with open("security_summary.json", "w") as f:
            json.dump(summary, f, indent=2)
        logger.info("Summary saved to security_summary.json")

def main():
    monitor = SecurityMonitor()
    monitor.monitor_accounts()

if __name__ == "__main__":
    main() 