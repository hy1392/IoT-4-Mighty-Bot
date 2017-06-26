import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
import datetime
motor_3=0
motor_4=0

motor_3_state=False
motor_4_state=False

gpio.setmode(gpio.BCM)
gpio.setup(18 , gpio.OUT)
gpio.setup(23 , gpio.OUT)
#left motor1
p_3 = gpio.PWM(18, 50)  # 50Hz = 20 ms
p_3.start(5.5)
p_3.ChangeDutyCycle(5.5) # middle position

#right motor2
p_4 = gpio.PWM(23, 50)  # 50Hz = 20 ms
p_4.start(7.5)
p_4.ChangeDutyCycle(7.5) # middle position

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    if rc == 0:
        client.subscribe("motor")
    else:
        print "Error!"
    
def on_message(client, userdata, msg):
    global motor_3
    global motor_4
    print("message\n")
    if msg.payload == "motor3":
        motor_3=1
    if msg.payload == "motor4":
        motor_4=1
    run()


def run():
    # button press
    global motor_3
    global motor_4
    global motor_3_state
    global motor_4_state
    
    if motor_3==1 and motor_3_state==False:
        print "left\n"
        p_3.ChangeDutyCycle(6.3) # -90 degree
        time.sleep(0.2)
        p_3.ChangeDutyCycle(8.3) # -90 degree
        time.sleep(0.2)
        p_3.ChangeDutyCycle(10.3) # -90 degree
        time.sleep(2)
        p_3.ChangeDutyCycle(5.5) # middle position

        motor_3_state=True
        motor_4_state=False
        
    if motor_4==1 and motor_4_state==False:
        print "right\n"
        p_4.ChangeDutyCycle(6.7) # -90 degree 
        time.sleep(0.2)
        p_4.ChangeDutyCycle(4.7) # -90 degree
        time.sleep(0.2)
        p_4.ChangeDutyCycle(2.7) # -90 degree
        time.sleep(2)
        p_4.ChangeDutyCycle(7.5) # middle position

        motor_4_state=True
        motor_3_state=False

    motor_3=0
    motor_4=0
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
    p_3.stop();
    p_4.stop();
    gpio.cleanup()
    
