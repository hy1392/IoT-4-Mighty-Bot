import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
import datetime
motor_1=0
motor_2=0

gpio.setmode(gpio.BCM)
gpio.setup(18 , gpio.OUT)
gpio.setup(23 , gpio.OUT)
#left motor1
p_1 = gpio.PWM(18, 50)  # 50Hz = 20 ms
p_1.start(5.5)
p_1.ChangeDutyCycle(5.5) # middle position

#right motor2
p_2 = gpio.PWM(23, 50)  # 50Hz = 20 ms
p_2.start(7.5)
p_2.ChangeDutyCycle(7.5) # middle position

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    if rc == 0:
        client.subscribe("motor")
    else:
        print "Error!"
    
def on_message(client, userdata, msg):
    global motor_1
    global motor_2
    print("message\n")
    if msg.payload == "motor1":
        motor_1=1
    if msg.payload == "motor2":
        motor_2=1
    run()


def run():
    # button press
    global motor_1
    global motor_2
    
    if motor_1==1 :
        print "left\n"
        p_1.ChangeDutyCycle(6.3) # -90 degree
        time.sleep(0.2)
        p_1.ChangeDutyCycle(8.3) # -90 degree
        time.sleep(0.2)
        p_1.ChangeDutyCycle(10.3) # -90 degree
        time.sleep(2)
        p_1.ChangeDutyCycle(5.5) # middle position

        
    if motor_2==1 :
        print "right\n"
        p_2.ChangeDutyCycle(6.7) # -90 degree 
        time.sleep(0.2)
        p_2.ChangeDutyCycle(4.7) # -90 degree
        time.sleep(0.2)
        p_2.ChangeDutyCycle(2.7) # -90 degree
        time.sleep(2)
        p_2.ChangeDutyCycle(7.5) # middle position

    motor_1=0
    motor_2=0
    time.sleep(0.5)

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    #client.connect("localhost")
    client.username_pw_set("root", "root")
    client.connect("m11.cloudmqtt.com", 10874, 10)
    client.loop_forever()

except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("motor")
    client.loop_stop()
    client.disconnect()
finally:
    p_1.stop();
    p_2.stop();
    gpio.cleanup()
    
