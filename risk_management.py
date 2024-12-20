import numpy as np
from typing import List, Dict


class RiskCalculator:
    """A simple financial risk calculator."""
    def __init__(self, data: List[float]):
        """Initialize with historical returns data."""
        self.data = np.array(data)

    def calculate_var(self, confidence_level: float = 0.95) -> float:
        """Calculate Value at Risk (VaR) at the specified confidence level.
        Args:
            confidence_level: The confidence level for VaR calculation (default: 0.95)
        Returns:
            The VaR value
        """
        if not 0 < confidence_level < 1:
            raise ValueError("Confidence level must be between 0 and 1")
        return -np.percentile(self.data, (1 - confidence_level) * 100)

    def calculate_volatility(self) -> float:
        """Calculate historical volatility (standard deviation).
        Returns:
            The volatility value
        """
        return np.std(self.data)

    def get_risk_metrics(self) -> Dict[str, float]:
        """Calculate and return multiple risk metrics.
        Returns:
            Dictionary containing various risk metrics
        """
        return {
            'var_95': self.calculate_var(0.95),
            'var_99': self.calculate_var(0.99),
            'volatility': self.calculate_volatility(),
            'max_loss': np.min(self.data),
            'max_gain': np.max(self.data)
        }
