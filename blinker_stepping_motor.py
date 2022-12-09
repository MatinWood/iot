#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "tianma"

from blinker import Device, ButtonWidget, NumberWidget
from stepping_motor import clock_1_round, rclock_1_round
import os
from blinker.voice_assistant import VoiceAssistant, VAType

authKey = os.environ.get('DEVICE_KEY')
print('authKey', authKey)
device = Device(authKey,
                mi_type=VAType.LIGHT)
button1 = device.addWidget(ButtonWidget('clockwise'))
button2 = device.addWidget(ButtonWidget('rclockwise'))


async def button1_callback(msg):
    clock_1_round()
    print("clockwise: {0}".format(msg))


async def button2_callback(msg):
    rclock_1_round()
    print("rclockwise: {0}".format(msg))


async def heartbeat_func(msg):
    print("Heartbeat func received: {0}".format(msg))


async def ready_func():
    # 获取设备配置信息
    print(vars(device.config))
    # 发送微信通知
    await device.wechat(title="oraingepi2上线啦", state="在线", text="oraingepi2上线啦")


button1.func = button1_callback
button2.func = button2_callback
voice_assistant = VoiceAssistant(VAType.LIGHT)
voice_assistant.power_change_callable = button1_callback

device.addVoiceAssistant(voice_assistant)
device.heartbeat_callable = heartbeat_func
device.ready_callable = ready_func

if __name__ == '__main__':
    device.run()
