# -*- coding:utf-8 -*-
'''
@Author: yanwii
@Date: 2018-08-31 15:43:28
'''
import gearman

gm_worker = gearman.GearmanWorker(['localhost:4731'])

def task_listener_reverse(worker, job):
    print "Reversing string: " + job.data
    return job.data[::-1]

gm_worker.set_client_id("python-worker")
gm_worker.register_task("reverse", task_listener_reverse)

gm_worker.work()