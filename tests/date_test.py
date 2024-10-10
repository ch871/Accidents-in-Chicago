from repository.date_repository import find_by_day, find_by_week, find_by_month


def test_count_accident_by_day():
    count = find_by_day('2023-09-05', '225')
    print(count)
    assert count


def test_count_accident_by_week():
    count = find_by_week('2023-09-05', '225')
    print(count)
    assert count


def test_count_accident_by_month():
    count = find_by_month('9', '225')
    print(count)
    assert count
