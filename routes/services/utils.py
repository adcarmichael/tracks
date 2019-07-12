from datetime import datetime


def convert_str_to_datetime(date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    return date
