import csv
import os
from database.connect import daily, weekly, monthly, area_colaction
from utils.data_utils import parse_date, get_week_range, safe_int


def read_csv(path: str):
    with open(path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row


def init_accidents():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
    for row in read_csv(data_path):
        crash_date = parse_date(row['CRASH_DATE'])
        area = row['BEAT_OF_OCCURRENCE']

        # Convert date to string format
        date_str = crash_date.strftime('%Y-%m-%d')
        week_start_str, week_end_str = get_week_range(crash_date)
        week_start_str = week_start_str.strftime('%Y-%m-%d')
        week_end_str = week_end_str.strftime('%Y-%m-%d')

        # Daily document
        daily.update_one(
            {'date': date_str, 'area': area},
            {'$inc': {
                'total_accidents': 1,
                'injuries.total': safe_int(row['INJURIES_TOTAL']),
                'injuries.fatal': safe_int(row['INJURIES_FATAL']),
                'injuries.non_fatal': safe_int(row['INJURIES_TOTAL']) - safe_int(row['INJURIES_FATAL']),
                f'contributing_factors.{row["PRIM_CONTRIBUTORY_CAUSE"]}': 1,
            }},
            upsert=True
        )

        # Weekly document
        weekly.update_one(
            {'week_start': week_start_str, 'area': area},
            {'$inc': {
                'total_accidents': 1,
                'injuries.total': safe_int(row['INJURIES_TOTAL']),
                'injuries.fatal': safe_int(row['INJURIES_FATAL']),
                'injuries.non_fatal': safe_int(row['INJURIES_TOTAL']) - safe_int(row['INJURIES_FATAL']),
                f'contributing_factors.{row["PRIM_CONTRIBUTORY_CAUSE"]}': 1,
            }},
            upsert=True
        )

        # Monthly document
        monthly.update_one(
            {'year': str(crash_date.year), 'month': str(crash_date.month), 'area': area},
            {'$inc': {
                'total_accidents': 1,
                'injuries.total': safe_int(row['INJURIES_TOTAL']),
                'injuries.fatal': safe_int(row['INJURIES_FATAL']),
                'injuries.non_fatal': safe_int(row['INJURIES_TOTAL']) - safe_int(row['INJURIES_FATAL']),
                f'contributing_factors.{row["PRIM_CONTRIBUTORY_CAUSE"]}': 1,
            }},
            upsert=True
        )
        # Area document
        area_colaction.update_one(
            {'area': area},
            {'$inc': {
                'total_accidents': 1,
                'injuries.total': safe_int(row['INJURIES_TOTAL']),
                'injuries.fatal': safe_int(row['INJURIES_FATAL']),
                'injuries.non_fatal': safe_int(row['INJURIES_TOTAL']) - safe_int(row['INJURIES_FATAL']),
                f'contributing_factors.{row["PRIM_CONTRIBUTORY_CAUSE"]}': 1,
            }},
            upsert=True
        )
    return "ok"

