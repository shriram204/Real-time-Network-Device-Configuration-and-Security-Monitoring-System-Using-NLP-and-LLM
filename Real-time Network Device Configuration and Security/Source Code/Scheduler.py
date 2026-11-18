from apscheduler.schedulers.background import BackgroundScheduler from monitor import monitor
from email_alert import send_email_alert def periodic_check():
alerts = monitor() if alerts:
message = "\n".join(alerts) send_email_alert(message) def start_scheduler():
scheduler = BackgroundScheduler() scheduler.add_job(periodic_check, "interval", minutes=10) scheduler.start()
