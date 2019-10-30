# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import re

import RPi.GPIO as GPIO
import time

def open():
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

def light_off():
    # BOARDでpinで指定
    GPIO.setmode(GPIO.BOARD)

    #pin33を出力に設定
    gp_out = 32
    GPIO.setup(gp_out, GPIO.OUT)

    #PMWを50Hzにセット
    servo = GPIO.PWM(gp_out, 50)
    servo.start(0)

    GPIO.setup(gp_out, GPIO.OUT)
    time.sleep(0.5)

    #初期値
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

    servo.ChangeDutyCycle(9.1) #12
    time.sleep(0.5)

    #位置の初期化
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

    #サーボの出力ピンの設定をリセット
    GPIO.cleanup(gp_out)

def light_on():
    # BOARDでpinで指定
    GPIO.setmode(GPIO.BOARD)

    #pin33を出力に設定
    gp_out = 32
    GPIO.setup(gp_out, GPIO.OUT)

    #PMWを50Hzにセット
    servo = GPIO.PWM(gp_out, 50)
    servo.start(0)

    GPIO.setup(gp_out, GPIO.OUT)
    time.sleep(0.5)

    #初期値
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

    servo.ChangeDutyCycle(9.3) #12
    time.sleep(0.5)

    #位置の初期化
    servo.ChangeDutyCycle(7.25)
    time.sleep(0.5)

    #サーボの出力ピンの設定をリセット
    GPIO.cleanup(gp_out)

@listen_to('玄関あけ')
@respond_to('玄関開け')
def open_autolock(message):
    message.send('オートロックを解除します')
    open()

@listen_to('ライトけし')
@listen_to('ライト消し')
@respond_to('ライトけし')
@respond_to('ライト消し')
def light_1click(message):
    message.send('リビングの照明を消します')
    light_off()

@listen_to('ライトつけ')
@listen_to('ライト点け')
@respond_to('ライトつけ')
@respond_to('ライト点け')
def light_1click(message):
    message.send('リビングの照明を点けます')
    light_on()
