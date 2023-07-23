import time

def focused_clock(minutes):
    # Set the focus duration in minutes
    focus_duration = minutes

    # Calculate the end time
    end_time = time.time() + (focus_duration * 60)

    print("Focused Clock started.")
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        mins = int(remaining_time // 60)
        secs = int(remaining_time % 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print("Remaining Time:", timer, end="\r")
        time.sleep(1)

    print("Focused Clock ended.")

# Set the focus duration (in minutes)
focus_minutes = 25

# Start the focused clock
focused_clock(focus_minutes)
