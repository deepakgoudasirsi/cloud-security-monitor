# Cloud Security Monitor

A powerful Python-based cloud security monitoring system that integrates with Orca Security APIs to detect, analyze, and report cloud misconfigurations across AWS accounts. This tool helps security teams maintain a strong security posture by providing real-time insights and automated reporting capabilities.

![Cloud Security Monitor](https://img.shields.io/badge/Cloud-Security-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

Cloud Security Monitor is designed to automate the process of monitoring cloud security configurations and detecting potential misconfigurations in AWS environments. It leverages Orca Security's powerful API to provide comprehensive security insights and automated reporting capabilities.

## Tech Stack

- **Backend**: Python 3.8+
- **API Integration**: Orca Security API
- **Cloud Platform**: AWS
- **Key Dependencies**:
  - `requests`: API communication
  - `python-dotenv`: Environment management
  - `pandas`: Data processing
  - `rich`: Console output formatting

## Features

- **Automated Detection**
  - Real-time cloud misconfiguration scanning
  - Continuous security posture monitoring
  - Automated vulnerability detection

- **Comprehensive Reporting**
  - Detailed security findings reports
  - Risk score tracking and trending
  - Improvement recommendations
  - Customizable report formats

- **Security Features**
  - Multi-account AWS monitoring
  - Secure credential management
  - Role-based access control
  - Audit logging

- **Performance**
  - Asynchronous API calls
  - Efficient data processing
  - Optimized report generation

## How to Run

### Prerequisites

- Python 3.8 or higher
- Orca Security API credentials
- AWS accounts to monitor
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/deepakgoudasirsi/cloud-security-monitor.git
cd cloud-security-monitor
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

### Configuration

1. Configure Orca Security API credentials in `.env`:
```
ORCA_API_KEY=your_api_key
ORCA_API_URL=https://api.orcasecurity.io
```

2. Set up AWS accounts in `config.py`

### Usage

1. Start the security monitor:
```bash
python security_monitor.py
```

2. Generate reports:
```bash
python report_generator.py
```



## 📁 Project Structure

```
cloud-security-monitor/
├── security_monitor.py    # Main monitoring logic
├── orca_client.py        # Orca Security API integration
├── report_generator.py   # Report generation utilities
├── config.py            # Configuration settings
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

---

## Contact

* **Deepak Gouda**
  [GitHub @deepakgoudasirsi](https://github.com/deepakgoudasirsi)
  [LinkedIn: Deepak Gouda](https://linkedin.com/in/deepakgoudasirsi)
