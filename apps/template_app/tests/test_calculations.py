from template_app.utils.calculations import calculate_dental_metrics


def test_calculate_dental_metrics_normal() -> None:
    data = [1.0, 3.0, 5.0]
    result = calculate_dental_metrics(data)
    assert result["average"] == 3.0
    assert result["max"] == 5.0


def test_calculate_dental_metrics_empty() -> None:
    result = calculate_dental_metrics([])
    assert result["average"] == 0.0
    assert result["max"] == 0.0
