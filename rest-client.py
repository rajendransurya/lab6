#!/usr/bin/env python3
from __future__ import print_function
import requests
import json
import time
import sys
import base64
import jsonpickle
import random
import numpy as np

def doRawImage(addr, debug=False):
    # prepare headers for http request
    headers = {'content-type': 'image/png'}
    img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    # send http request with image and receive response
    image_url = addr + '/api/rawimage'
    response = requests.post(image_url, data=img, headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(json.loads(response.text))

def doAdd(addr, debug=False):
    headers = {'content-type': 'application/json'}
    # send http request with image and receive response
    add_url = addr + "/api/add/5/10"
    response = requests.post(add_url, headers=headers)
    if debug:
        # decode response
        print("Response is", response)
        print(json.loads(response.text))

def doDotProduct(addr, debug=False):
    dot_url=addr + "/api/dotproduct"
    a = [random.random() for _ in range(100)]
    b = [random.random() for _ in range(100)]
    body={
        'a':a,
        'b':b
    }
    response=requests.post(dot_url,json=body)
    if debug:
        # decode response
        try:
            print("Response is",response.text)
        except json.JSONDecodeError:
            print("Response does not contain valid JSON data.")
        # print(json.loads(response.text))


def doJsonImage(addr, debug=False):
    img_url= addr+"/api/jsonimage"
    filename = "Flatirons_Winter_Sunrise_edit_2.jpg"
    with open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb') as img:
        encoded_img = str(base64.b64encode(img.read()).decode())
    body={
        "image":encoded_img
    }
    response = requests.post(img_url, json=body)
    if debug:
        # decode response
        try:
            print("Response is", response.text)
        except json.JSONDecodeError:
            print("Response does not contain valid JSON data.")

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
    print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
    print(f"and <reps> is the integer number of repititions for measurement")

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])

addr = f"http://{host}:5000"
print(f"Running {reps} reps against {addr}")

if cmd == 'rawImage':
    start = time.perf_counter()
    for x in range(reps):
        doRawImage(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'add':
    start = time.perf_counter()
    for x in range(reps):
        doAdd(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'jsonImage':
    start = time.perf_counter()
    for x in range(reps):
        doJsonImage(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
elif cmd == 'dotProduct':
    start = time.perf_counter()
    for x in range(reps):
        doDotProduct(addr)
    delta = ((time.perf_counter() - start)/reps)*1000
    print("Took", delta, "ms per operation")
else:
    print("Unknown option", cmd)