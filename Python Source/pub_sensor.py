import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
import dht11
import datetime

import spidev
gpio.setwarnings(True)
gpio.setmode(gpio.BCM)




#ultra
trig_pin = 13
echo_pin = 19
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)
distance=0
    
instance = dht11.DHT11(pin = 5)


#vibration
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_DOWN)

#result
temhum_result = 1
vibration_result =1

light_level=0
light_volts=0

spi=spidev.SpiDev()
spi.open(0,0)

light_channel=0

#tem hum
tem=0
hum=0

    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    
def readChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((adc[1] & 3) << 8) + adc[2]
    return adc_out
def convert2volts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

def light_run():
    global light_level
    global light_volts

    light_level = readChannel(light_channel)
    light_volts = convert2volts(light_level, 2)

    print("Light: %d (%f V)" %(light_level, light_volts))

def temhum_run():
    global tem
    global hum
    global temhum_result
    temhum_result=instance.read()
    print("Last valid input: " +str(datetime.datetime.now()))    
    if temhum_result.is_valid():
        tem=temhum_result.temperature
        hum=temhum_result.humidity
        print("Temperature: %d C" % tem)
        print("Humidity: %d %%" % hum)
        return True
    else:
        print("Temperature: %d C" % tem)
        print("Humidity: %d %%" % hum)
        return False

def vibration_run():
    global vibration_result
    vibration_result = gpio.input(26)
    if vibration_result == 1:
        print("Vibration : ON")
    else :
        print("Vibration : OFF")


def distance_run():

    global distance

    #ultra
    gpio.output(trig_pin, False)
    time.sleep(0.5)
    gpio.output(trig_pin, True)
    time.sleep(0.00001)
    gpio.output(trig_pin, False)

    while gpio.input(echo_pin) == 0:
        pulse_start = time.time()
        
    while gpio.input(echo_pin) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)

    if distance < 1.5:
        distance = 30
    
    print "Distance : ", distance, "cm\n"
    print("-------------------------------------")
    
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
#mqttc.connect("localhost")
mqttc.username_pw_set("root", "root")
mqttc.connect("m11.cloudmqtt.com", 10874, 10)


try:
    mqttc.loop_start()
    global light_level
    while True:
        global result 
        if temhum_run():
            mqttc.publish("environment/tem", tem)
            mqttc.publish("environment/hum", hum)
        else:
            print("temhum failed")
            mqttc.publish("environment/tem", tem)
            mqttc.publish("environment/hum", hum)

        #light    
        light_run()
        mqttc.publish("environment/light", light_level)

        #vibration
        vibration_run()
        mqttc.publish("environment/impact", vibration_result)
        
        distance_run()
        mqttc.publish("environment/ultra", distance)

        time.sleep(0.5)
except KeyboardInterrupt:
    printf("Finished")
    mqttc.loop_stop()
    mqttc.disconnect()
    gpio.cleanup()
