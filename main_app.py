import subprocess
import time
import sensor_reading as sr

amount_coffee = 0

while True:
    try:
        current_time = time.strftime("%H:%M:%S")
        if (current_time >= '08:00:00' and sr.machine_temp()> 60):
            #subprocess.call(['python3', 'create_tweet.py'])
            print('Tweet sent through API!')
            amount_coffee += 1
            time.sleep(900)
        else:
            print('Not worked!')
            break
    except:
        break