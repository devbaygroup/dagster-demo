from datetime import datetime
from datetime import timedelta

from .log import Logger

log = Logger()


def get_day(day, log=log):
    """
    day: shorthand or 'xxxx-xx-xx'
    # for upstream ingestion
    day = yesterday, today (now), custom date
    # for downstream
    day = hardcode day and write offset, custom date --> ingest only
    workflow_day = yesterday (date when writing to partition)
    """

    day_now = datetime.now().date()

    if day == "yesterday":
        day_value = str(day_now - timedelta(days=1))
    elif day == "today":
        day_value = str(day_now)
    else:
        day_value = str(day)
    log.info("day_value: {}".format(day_value))

    return day_value