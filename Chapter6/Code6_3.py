#!/usr/bin/env python3

import time
import csv
import logging
import datetime
from bme280 import BME280

# Import the SMBus module, using smbus2 if available, otherwise smbus
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Configure logging to record information with a timestamp
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Startup message for the program
logging.info("""weather.py - Print readings from the BME280 weather sensor.

Press Ctrl+C to exit!

""")

# Initialize the I2C bus
bus = SMBus(1)
# Initialize the BME280 sensor
bme280 = BME280(i2c_dev=bus)

# Create a data file with the current timestamp in the name
name_datafile = 'data_' + str(datetime.datetime.now()) + '.txt'

# Create and immediately close the file to ensure it exists
datafile = open(name_datafile, "w")
datafile.close()

# Reopen the file in append mode
datafile = open(name_datafile, "a")

# Write the field names to the file
field_names = ['Date;', 'Temperature ( C);', 'Pressure (hPa);', 'Humidity (%);']
datafile.writelines(field_names)

# Infinite loop to read and record data from the sensor
while True:
    # Get the current timestamp
    x = datetime.datetime.now()
    # Read the temperature from the sensor
    temperature = bme280.get_temperature()
    # Read the pressure from the sensor
    pressure = bme280.get_pressure()
    # Read the humidity from the sensor
    humidity = bme280.get_humidity()
    # Log the data
    logging.info("""\n Temperature: {:05.2f} *C \n Pressure: {:05.2f} hPa \n Relative humidity: {:05.2f} % \n """.format(temperature, pressure, humidity))
    # Write the data to the file
    datafile.writelines('\n')
    datafile.writelines([str(x), ';', str(temperature), ';', str(pressure), ';', str(humidity)])
    # Ensure the data is written immediately
    datafile.flush()
    # Wait 1 second before repeating the loop (modifiable to 1800 seconds to record data every 30 minutes)
    time.sleep(1) # value in seconds, 1800 to record data every 30 minutes
