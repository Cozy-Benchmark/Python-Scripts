import datetime as dt

def log_hello():
    current_time = dt.datetime.now().replace(second=0, microsecond=0)
    date = to_mm_dd_yyyy(current_time.date())
    time = to_am_pm(current_time.time())
    with (open("startup_log.txt", "a")) as f:
        f.write(f"\nLogin Report: Bryan Benchmark Mendoza has turned on their PC at {date}, at {time}")

def to_mm_dd_yyyy(current_time):
    return f"{current_time.month}/{current_time.day}/{current_time.year}" 

def to_am_pm(current_time):
    hour = current_time.hour
    if hour < 12:
        return f"{hour}:{current_time.minute} AM"
    elif hour == 12:
        return f"{hour}:{current_time.minute} PM"
    else:
        return f"{hour - 12}:{current_time.minute} PM"

def main():
    log_hello()

if __name__ == "__main__":
    main()