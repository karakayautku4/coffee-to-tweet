import subprocess
import time
import sensor_reading as sr

amount_coffee = 0

def application(amount_coffee):
    while True:
        try:
            current_time = time.strftime("%H:%M:%S")
            if ((sr.machine_temp() > 70) and (current_time >= '08:00:00') and (current_time < '21:00:00')):
                subprocess.call(['python3', 'create_tweet.py'])
                print('Tweet sent through API!')
                amount_coffee += 1
                time.sleep(900)
            else:
                print('Not worked!')
                break
        except KeyboardInterrupt:
            print('Application stopped by user.')
            break
        except sr.SensorReadingError:
            print('Could not read sensor data.')
            break
        except Exception as e:
            print('An error occurred:', e)
            break

application(amount_coffee)