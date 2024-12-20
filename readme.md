# Financial Risk Management Application

A simple Python application for calculating various financial risk metrics.

## Features

- Value at Risk (VaR) calculation at different confidence levels
- Historical volatility calculation
- Basic risk metrics reporting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/financial-risk-management.git
cd financial-risk-management
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

```python
from risk_management import RiskCalculator

# Example data (historical returns)
returns_data = [0.01, -0.02, 0.03, -0.01, 0.02]

# Create a risk calculator instance
calc = RiskCalculator(returns_data)

# Calculate VaR at 95% confidence level
var_95 = calc.calculate_var(0.95)

# Get all risk metrics
metrics = calc.get_risk_metrics()
```

## Testing

Run the tests using pytest:
```bash
pytest
```

## CI/CD

This project uses GitHub Actions for continuous integration and testing. The workflow will automatically run tests on every push and pull request to the main branch.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
