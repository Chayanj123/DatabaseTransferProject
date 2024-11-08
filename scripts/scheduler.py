import schedule
import time
from data_transfer import perform_transfer  # Adjust import as needed

def job():
    print("Running scheduled data transfer...")
    perform_transfer()

# Schedule the job
schedule.every().hour.do(job)         # Hourly
schedule.every().day.at("00:00").do(job)  # Daily at midnight
schedule.every().week.at("Monday 00:00").do(job)  # Weekly on Monday at midnight
schedule.every().month.at("1st 00:00").do(job)  # Monthly on the 1st at midnight

while True:
    schedule.run_pending()
    time.sleep(1)
