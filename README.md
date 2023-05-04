# coffee-to-tweet

Automated Coffee Tweet using Arduino and Python:

This project uses an Arduino Rev3 board and a temperature sensor to detect when a user prepares a cup of coffee. Once the coffee is prepared, a Python script automatically tweets a message on Twitter indicating that the user has made a cup of coffee.

## Requirements

Arduino Rev3 Board

Temperature Sensor (LM35 or DS18B20)

Python 3.x

Wiring

Connect the temperature sensor to the Arduino board according to the following diagram:

![diagram](https://user-images.githubusercontent.com/84205608/236194604-1b504f49-4308-4e66-b5a7-496d30a786c1.png)


Temperature Sensor Wiring Diagram:

![scheme](https://user-images.githubusercontent.com/84205608/236194658-2873ba54-a583-409a-a236-96ad8357c7b2.png)

## Usage

Clone the repository to your local machine.

Upload the temperature.ino sketch to your Arduino board using the Arduino IDE.

Open the coffee_tweet.py script in your preferred Python editor.

Edit the following variables at the .env file to match your Twitter API credentials:

CONSUMER_KEY

CONSUMER_SECRET

Run the script using the command:

    python3 coffee_tweet.py
The script will continuously monitor the temperature sensor and tweet a message on Twitter when the temperature rises above a certain threshold. This indicates that the user has made a cup of coffee.

## Todo

- [ ] Optimize create_tweet.py for Auth
- [ ] Optimize other scripts.

## Contributing

If you'd like to contribute to this project, please feel free to fork this repository and submit a pull request.

## Acknowledgements

This project was inspired by the Tweet-a-Pot project by Gregg Horton 2011.
