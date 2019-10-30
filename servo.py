import RPi.GPIO as GPIO
import time

# BOARDでpinで指定
GPIO.setmode(GPIO.BOARD)

#pin33を出力に設定
gp_out = 33
GPIO.setup(gp_out, GPIO.OUT)

#PMWを50Hzにセット
servo = GPIO.PWM(gp_out, 50)
servo.start(0)

#GPIO.setup(gp_out, GPIO.OUT)
#time.sleep(0.5)

#初期値
servo.ChangeDutyCycle(7.25)
time.sleep(0.5)

servo.ChangeDutyCycle(8.25) #12
time.sleep(0.5)
#玄関8 照明?
#位置の初期化
servo.ChangeDutyCycle(7.25)
time.sleep(0.5)

#サーボの出力ピンの設定をリセット
GPIO.cleanup(gp_out)