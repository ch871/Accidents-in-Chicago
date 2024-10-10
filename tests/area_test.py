from repository.area_repository import get_count_eccident_by_area, get_statictic_injuries_by_area, get_contributing_factors


def test_get_count_of_area_accidents():
    count = get_count_eccident_by_area('225')
    assert count


def test_get_reason_of_area_accidents():
    reason = get_contributing_factors('225')
    assert len(reason) > 0


def test_get_statistic_area_accidents():
    statistic = get_statictic_injuries_by_area('225')
    assert len(statistic) > 0
