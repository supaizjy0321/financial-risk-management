import pytest
import numpy as np
from risk_management import RiskCalculator


def test_risk_calculator_initialization():
    data = [0.01, -0.02, 0.03, -0.01, 0.02]
    calc = RiskCalculator(data)
    assert isinstance(calc.data, np.ndarray)
    assert len(calc.data) == 5


def test_var_calculation():
    data = [0.01, -0.02, 0.03, -0.01, 0.02]
    calc = RiskCalculator(data)
    var_95 = calc.calculate_var(0.95)
    assert isinstance(var_95, float)
    assert var_95 >= 0  # VaR should be positive


def test_invalid_confidence_level():
    calc = RiskCalculator([0.01, -0.02, 0.03])
    with pytest.raises(ValueError):
        calc.calculate_var(1.5)


def test_volatility_calculation():
    data = [0.01, -0.02, 0.03, -0.01, 0.02]
    calc = RiskCalculator(data)
    vol = calc.calculate_volatility()
    assert isinstance(vol, float)
    assert vol >= 0  # Volatility should be positive


def test_risk_metrics():
    data = [0.01, -0.02, 0.03, -0.01, 0.02]
    calc = RiskCalculator(data)
    metrics = calc.get_risk_metrics()
    assert isinstance(metrics, dict)
    assert all(key in metrics for key in ['var_95', 'var_99', 'volatility', 'max_loss', 'max_gain'])
    assert all(isinstance(value, float) for value in metrics.values())
