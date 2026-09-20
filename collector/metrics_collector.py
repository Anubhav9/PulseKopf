from integrations import health_api
from datetime import datetime, timezone, timedelta

def collect_metrics_after_interval(parameter,interval):
    current_date_time = datetime.now(timezone.utc).replace(microsecond=0)
    time_in_minutes=interval/60
    one_minute_ago = current_date_time - timedelta(minutes=time_in_minutes)
    current_date_time = current_date_time.isoformat().replace("+00:00", "Z")
    one_minute_ago = one_minute_ago.isoformat().replace("+00:00", "Z")

    return health_api.get_health_data(parameter,one_minute_ago,current_date_time)
