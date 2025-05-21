import random
from datetime import datetime, timedelta
from typing import Dict, List

class MockSecurityData:
    def __init__(self):
        self.mock_accounts = [
            "dev-account-123",
            "prod-account-456",
            "staging-account-789"
        ]
        
        self.mock_findings = [
            {
                "id": "S3-001",
                "title": "Public S3 Bucket Access",
                "severity": "critical",
                "description": "S3 bucket has public read access enabled",
                "recommendation": "Disable public access and use IAM policies"
            },
            {
                "id": "EC2-001",
                "title": "Exposed Security Group",
                "severity": "high",
                "description": "Security group allows unrestricted inbound access",
                "recommendation": "Restrict inbound rules to specific IP ranges"
            },
            {
                "id": "IAM-001",
                "title": "Overly Permissive IAM Policy",
                "severity": "high",
                "description": "IAM policy grants excessive permissions",
                "recommendation": "Follow principle of least privilege"
            },
            {
                "id": "KMS-001",
                "title": "Unencrypted EBS Volume",
                "severity": "critical",
                "description": "EBS volume is not encrypted",
                "recommendation": "Enable encryption for all EBS volumes"
            },
            {
                "id": "VPC-001",
                "title": "Open VPC Security Group",
                "severity": "high",
                "description": "VPC security group allows all traffic",
                "recommendation": "Restrict VPC security group rules"
            }
        ]

    def get_mock_findings(self, account_id: str = None, severity: str = None) -> List[Dict]:
        """Generate mock security findings."""
        findings = []
        num_findings = random.randint(1, 5)
        
        for _ in range(num_findings):
            finding = random.choice(self.mock_findings).copy()
            if severity and finding["severity"] != severity:
                continue
                
            finding.update({
                "account_id": account_id or random.choice(self.mock_accounts),
                "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
                "status": random.choice(["open", "resolved"]),
                "risk_score": random.uniform(1.0, 10.0)
            })
            findings.append(finding)
            
        return findings

    def get_mock_risk_score(self, account_id: str = None) -> Dict:
        """Generate mock risk score."""
        return {
            "account_id": account_id or random.choice(self.mock_accounts),
            "score": random.uniform(1.0, 10.0),
            "timestamp": datetime.now().isoformat(),
            "trend": random.choice(["improving", "stable", "degrading"]),
            "findings_count": {
                "critical": random.randint(0, 5),
                "high": random.randint(0, 10),
                "medium": random.randint(0, 15),
                "low": random.randint(0, 20)
            }
        }

    def get_mock_assets(self, account_id: str = None) -> List[Dict]:
        """Generate mock asset inventory."""
        asset_types = ["EC2", "S3", "RDS", "Lambda", "IAM"]
        assets = []
        
        for _ in range(random.randint(5, 15)):
            asset_type = random.choice(asset_types)
            assets.append({
                "id": f"{asset_type}-{random.randint(1000, 9999)}",
                "type": asset_type,
                "account_id": account_id or random.choice(self.mock_accounts),
                "region": random.choice(["us-east-1", "us-west-2", "eu-west-1"]),
                "status": random.choice(["running", "stopped", "terminated"]),
                "last_updated": (datetime.now() - timedelta(days=random.randint(0, 7))).isoformat()
            })
            
        return assets 