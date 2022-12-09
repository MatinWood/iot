#!/bin/bash
nohup /usr/bin/python3 /root/projects/iot/blinker_stepping_motor.py >> /var/log/blinker.log 2>&1 &