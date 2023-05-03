import serial

def machine_temp():
    try:
        # replace 'COM3' with the serial port of your Arduino board
        ser = serial.Serial('COM3', 9600)
        temperature = None
        while temperature is None:
            temperature = ser.readline().decode().strip()
        ser.close()
        return temperature
    except serial.SerialException as e:
        print(f"Error communicating with the serial port: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None