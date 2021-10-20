import datetime

FIRST_SEMESTER_DATE = datetime.datetime(2021, 9, 1)
SECOND_SEMESTER_DATE = datetime.datetime(2022, 2, 1)


def get_current_week_parity():
    now = datetime.datetime.now()

    if now.month >= 9:
        week_count = (now - FIRST_SEMESTER_DATE).days // 7
    else:
        week_count = (now - SECOND_SEMESTER_DATE).days // 7

    if week_count % 2:
        return "even"
    else:
        return "odd"
