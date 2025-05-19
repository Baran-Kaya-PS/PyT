from datetime import date, datetime
import pytz as p


def log_event(message, level="INFO"):
    with open("app.log","a",encoding="utf-8") as f: # append
        log_date = datetime.now().strftime("%Y-%m-%d  %H:%M")
        f.write(f"[{log_date}][{level}] {message}\n")

