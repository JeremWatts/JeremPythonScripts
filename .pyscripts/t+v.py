import time
import sys
from datetime import datetime
from pycaw.pycaw import AudioUtilities

# Platform-specific imports for non-blocking input
if sys.platform == 'win32':
    import msvcrt
else:
    import select

# Get the default speakers and volume controller
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume

def fmt(dt):
    """Format time as 4:15pm (no leading zero, lowercase am/pm)"""
    s = dt.strftime("%I:%M%p").lower()
    s = s.lstrip("0").replace(" 0", " ")
    if s.startswith(":"):  # handles 12:05am -> :05am
        s = "12" + s
    return s

def get_current_volume_percent():
    return int(volume.GetMasterVolumeLevelScalar() * 100)

def display_status():
    now = datetime.now()
    current_time = fmt(now)
    current_vol = get_current_volume_percent()
    print(f"\r{current_time}_{current_vol}%V", flush=True, end="")

def get_seconds_until_next_5min():
    """Calculate seconds until next 5-minute mark"""
    now = datetime.now()
    mod = now.minute % 5
    wait = (5 - mod) * 60 - now.second
    return max(1, wait)  # Prevent negative/zero

def input_with_timeout(timeout):
    """Get input with timeout. Returns None if timeout occurs."""
    if sys.platform == 'win32':
        # Windows implementation
        start_time = time.time()
        input_str = ""
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getche().decode('utf-8')
                if char == '\r':  # Enter key
                    return input_str
                elif char == '\x08':  # Backspace
                    if input_str:
                        input_str = input_str[:-1]
                        print('\b \b', end='', flush=True)
                else:
                    input_str += char
            
            if time.time() - start_time > timeout:
                return None
            time.sleep(0.1)
    else:
        # Unix/Linux/Mac implementation
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().strip()
        return None

# Initial display
display_status()

while True:
    timeout = get_seconds_until_next_5min()
    print(": ", end="", flush=True)
    val = input_with_timeout(timeout)
    
    if val is None:  # Timeout - update display
        print()  # New line
        display_status()
        continue
    
    if val.lower() in {"exit", "quit", "q"}:
        print("\nGoodbye!")
        exit()
    
    if not val:  # Empty input
        print()
        display_status()
        continue
    
    try:
        fval = float(val)
        if 0.0 <= fval <= 1.0:
            volume.SetMasterVolumeLevelScalar(fval, None)
            print()  # New line
            display_status()
        else:
            print("\nError: Value must be 0.0-1.0")
            display_status()
    except ValueError:
        print("\nError: Invalid input")
        display_status()
