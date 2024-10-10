from database.connect import daily, weekly, monthly


def find_by_day(date, area):
    return list(daily.find({'date': date, 'area': area}))


def find_by_week(date, area):
    return list(weekly.find({'week_start': date, 'area': area}))


def find_by_month(month, area):
    return list(monthly.find({'month': month, 'area': area}))
