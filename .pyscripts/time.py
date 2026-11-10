import time
from datetime import datetime

def fmt(dt):
    return dt.strftime("%I:%M%p").lower()

while True:
    now = datetime.now()
    print(fmt(now), flush=True)

    mod = now.minute % 15
    wait = (15 - mod) * 60 - now.second
    time.sleep(wait)
