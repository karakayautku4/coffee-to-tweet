# coffee-to-tweet

coffee-to-tweet: Automated Coffee Tweet using Arduino and Python
This project uses an Arduino Rev3 board and a temperature sensor to detect when a user prepares a cup of coffee. Once the coffee is prepared, a Python script automatically tweets a message on Twitter indicating that the user has made a cup of coffee.

Requirements
Arduino Rev3 Board
Temperature Sensor (LM35 or DS18B20)
Python 3.x
Wiring
Connect the temperature sensor to the Arduino board according to the following diagram:

Temperature Sensor Wiring Diagram

Usage
Clone the repository to your local machine.
Upload the temperature.ino sketch to your Arduino board using the Arduino IDE.
Open the coffee_tweet.py script in your preferred Python editor.
Edit the following variables at the top of the script to match your Twitter API credentials:
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
Run the script using the command python coffee_tweet.py.
The script will continuously monitor the temperature sensor and tweet a message on Twitter when the temperature rises above a certain threshold. This indicates that the user has made a cup of coffee.

Acknowledgements
This project was inspired by the Tweet-a-Pot project by Gregg Horton 2011.