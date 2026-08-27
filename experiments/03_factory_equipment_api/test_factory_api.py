from factory_api import get_equipment_status


def test_known_alarm_equipment() -> None:
    result = get_equipment_status("Conveyor3")

    assert result["status"] == "high_alarm"
    assert result["temperature_c"] == 91


def test_known_running_equipment() -> None:
    result = get_equipment_status("Conveyor7")

    assert result["status"] == "running"
    assert result["temperature_c"] == 63


def test_unknown_equipment() -> None:
    result = get_equipment_status("UnknownConveyor")

    assert result["status"] == "unknown"
