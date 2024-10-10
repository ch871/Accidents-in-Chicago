from datetime import datetime, timedelta
from returns.maybe import Maybe


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


def get_week_range(date):
    end = date + timedelta(days=6)
    return date, end.date()


def safe_int(x: str) -> int:
    return (Maybe.from_optional(x)
            .map(lambda n: 0 if n == '' else n)
            .map(int)
            .value_or(0)
            )
