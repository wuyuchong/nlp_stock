#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import time
from src.auto import train_sim_doc2vec

while True:
    submit_dir = '/similarity/submit/doc2vec/'
    # mkdir
    try:
        os.makedirs(submit_dir)
    except FileExistsError:
        pass
    tasks = os.listdir(submit_dir)
    if tasks != []:
        print(tasks)
        task = tasks[0]
        f = open(submit_dir + task)
        arguments = json.load(f)
        f.close()
        print(arguments)
        os.remove(submit_dir + task)
        print('start --------> ', task)
        try:
            train_sim_doc2vec(**arguments)
        except:
            print('error here')
            continue
        print('finish --------> ', task)
    time.sleep(3)
