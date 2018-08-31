#! /usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
@Author: yanwii
@Date: 2018-08-31 15:46:42
'''
from celery import Celery
import urllib


app = Celery(
    "tasks",
    broker="redis://0.0.0.0:6379/0",
)

import time
@app.task
def add(x, y):
    time.sleep(10)
    print(x, y)
    return x + y