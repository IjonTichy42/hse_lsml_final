#!/usr/bin/env python
# coding: utf-8

import os
import warnings
import time

import mlflow
import requests

# MLFLOW_SERVER_URL = 'http://127.0.0.1:5000/'
# experiment_name = 'soccer-news-experiment'

# warnings.filterwarnings("ignore")

# client = mlflow.tracking.MlflowClient(MLFLOW_SERVER_URL)

# os.system('echo here!')

# mlflow.set_tracking_uri(MLFLOW_SERVER_URL)

# os.system('echo track!')

# a = os.popen('lsof -t -i:5005').read()

# os.system("kill -9 `lsof -t -i:5005`")

# while a:
#     a = os.popen('lsof -t -i:5005').read()

os.system('echo almost!')

can_go = False

while not can_go:
    try:
        r = requests.get('http://mlflow:5000/#/experiments/1')
        r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        os.system('echo down!')
    else:
        can_go = True
        os.system('echo up!')
    time.sleep(2)

os.system('MLFLOW_TRACKING_URI=http://mlflow:5000 mlflow models serve -m "models:/soccer-model/Production" -h 0.0.0.0 --no-conda')

os.system('echo started!')

while True:
    time.sleep(10)

os.system('echo woke!')
