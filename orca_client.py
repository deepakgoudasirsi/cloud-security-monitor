from typing import Dict, List, Optional
from datetime import datetime
import logging
from mock_security_data import MockSecurityData

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrcaClient:
    def __init__(self):
        self.mock_data = MockSecurityData()

    def get_findings(self, severity: Optional[str] = None, account_id: Optional[str] = None) -> List[Dict]:
        """Get security findings from mock data."""
        return self.mock_data.get_mock_findings(account_id, severity)

    def get_risk_score(self, account_id: Optional[str] = None) -> Dict:
        """Get risk score from mock data."""
        return self.mock_data.get_mock_risk_score(account_id)

    def get_assets(self, account_id: Optional[str] = None) -> List[Dict]:
        """Get assets information from mock data."""
        return self.mock_data.get_mock_assets(account_id)

    def get_high_severity_findings(self, account_id: Optional[str] = None) -> List[Dict]:
        """Get high severity findings for an account."""
        return self.get_findings(severity="high", account_id=account_id)

    def get_critical_findings(self, account_id: Optional[str] = None) -> List[Dict]:
        """Get critical severity findings for an account."""
        return self.get_findings(severity="critical", account_id=account_id)

    def get_findings_by_time_range(self, start_time: datetime, end_time: datetime, 
                                 account_id: Optional[str] = None) -> List[Dict]:
        """Get findings within a specific time range."""
        findings = self.get_findings(account_id=account_id)
        return [
            f for f in findings 
            if start_time <= datetime.fromisoformat(f["timestamp"]) <= end_time
        ] 