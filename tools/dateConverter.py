from datetime import datetime
from .consts import Constants


def convertDateToTimestamp(date):
    try:
        return datetime.strptime(date, Constants.DATETIME_FORMAT).timestamp()
    except ValueError:
        return date


def convertTimestampToDate(timestamp):
    return datetime.fromtimestamp(float(timestamp)).strftime(Constants.DATETIME_FORMAT)
