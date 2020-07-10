from time import sleep
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

DATA_PIN = 18
SCK_PIN = 23

with SHT1x(DATA_PIN, SCK_PIN, gpio_mode=GPIO.BCM) as sensor:
    temp = sensor.read_temperature()
    humidity = sensor.read_humidity(temp)
    sensor.calculate_dew_point(temp, humidity)
    print (sensor)
    sleep(2)


