import json
from datetime import datetime
from typing import Dict, List
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from orca_client import OrcaClient
from config import AWS_ACCOUNTS, SEVERITY_LEVELS

console = Console()

class ReportGenerator:
    def __init__(self):
        self.orca_client = OrcaClient()

    def load_findings_history(self, filename: str = "security_summary.json") -> Dict:
        """Load findings history from JSON file."""
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            console.print(f"[red]Error: {filename} not found[/red]")
            return {}

    def generate_account_report(self, account_id: str) -> Dict:
        """Generate a detailed report for a single account."""
        findings = {
            "critical": self.orca_client.get_critical_findings(account_id),
            "high": self.orca_client.get_high_severity_findings(account_id),
            "risk_score": self.orca_client.get_risk_score(account_id)
        }

        return {
            "account_id": account_id,
            "timestamp": datetime.now().isoformat(),
            "findings": findings,
            "summary": {
                "critical_count": len(findings["critical"]),
                "high_count": len(findings["high"]),
                "risk_score": findings["risk_score"].get("score", 0)
            }
        }

    def generate_comparison_report(self, current_data: Dict, historical_data: Dict) -> Dict:
        """Generate a comparison report between current and historical data."""
        comparison = {
            "timestamp": datetime.now().isoformat(),
            "accounts": {}
        }

        for account_id in AWS_ACCOUNTS:
            if account_id in current_data["accounts"] and account_id in historical_data["accounts"]:
                current = current_data["accounts"][account_id]
                historical = historical_data["accounts"][account_id]

                comparison["accounts"][account_id] = {
                    "critical_findings_change": current["critical_findings"] - historical["critical_findings"],
                    "high_findings_change": current["high_findings"] - historical["high_findings"],
                    "risk_score_change": current["risk_score"] - historical["risk_score"]
                }

        return comparison

    def display_report(self, report: Dict):
        """Display the report in a rich format."""
        console.print("\n[bold blue]Security Report[/bold blue]")
        console.print(f"Generated at: {report['timestamp']}\n")

        for account_id, data in report["accounts"].items():
            console.print(f"[bold]Account: {account_id}[/bold]")
            
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Metric")
            table.add_column("Current")
            table.add_column("Change")

            table.add_row(
                "Critical Findings",
                str(data["critical_findings"]),
                f"{data['critical_findings_change']:+d}"
            )
            table.add_row(
                "High Findings",
                str(data["high_findings"]),
                f"{data['high_findings_change']:+d}"
            )
            table.add_row(
                "Risk Score",
                f"{data['risk_score']:.2f}",
                f"{data['risk_score_change']:+.2f}"
            )

            console.print(table)
            console.print()

    def export_to_csv(self, report: Dict, filename: str = "security_report.csv"):
        """Export the report to CSV format."""
        data = []
        for account_id, metrics in report["accounts"].items():
            data.append({
                "Account ID": account_id,
                "Critical Findings": metrics["critical_findings"],
                "High Findings": metrics["high_findings"],
                "Risk Score": metrics["risk_score"],
                "Critical Findings Change": metrics["critical_findings_change"],
                "High Findings Change": metrics["high_findings_change"],
                "Risk Score Change": metrics["risk_score_change"]
            })

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        console.print(f"[green]Report exported to {filename}[/green]")

def main():
    generator = ReportGenerator()
    
    # Generate current report
    current_report = {}
    for account_id in AWS_ACCOUNTS:
        current_report[account_id] = generator.generate_account_report(account_id)

    # Load historical data
    historical_data = generator.load_findings_history()

    # Generate comparison report
    if historical_data:
        comparison_report = generator.generate_comparison_report(current_report, historical_data)
        generator.display_report(comparison_report)
        generator.export_to_csv(comparison_report)
    else:
        console.print("[yellow]No historical data found for comparison[/yellow]")

if __name__ == "__main__":
    main() 