import time, subprocess

style = "mac"
timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

# TODO: At the end of the countdown, play a sound file.

if style == "win":
    # Windows
    subprocess.Popen(['start', 'alarm.wav'], shell=True)
elif style == "mac":
    # MacOS / Linux
    subprocess.Popen(['afplay', 'alarm.wav'], shell=False)