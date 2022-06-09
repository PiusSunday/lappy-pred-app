from flask import Flask, request, jsonify
import pickle
import pandas as pd
# import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "Oops!!!...These errors sucks!!!"


@app.route('/predictor', methods=['POST'])
def predictor():
    new = request.get_json()
    brand = new['BRAND']
    cpu_brand = new['CPU BRAND']
    cpu_core = new['CPU CORE']
    cpu_generation = new['CPU GENERATION']
    cpu_family = new['CPU FAMILY']
    ram_size = new['RAM SIZE']
    ddr_type = new['RAM(DDR) TYPE']
    disk_type = new['DISK TYPE']
    ssd_size = new['SSD SIZE']
    hdd_size = new['HDD SIZE']
    gpu_brand = new['GPU BRAND']
    gpu_type = new['GPU TYPE']
    screen_size = new['SCREEN SIZE']
    screen_resolution = new['SCREEN RESOLUTION']
    state = new['STATE']

    # characteristics = {
    #     'BRAND': brand,
    #     'CPU BRAND': cpu_brand,
    #     'CPU CORE': cpu_core,
    #     'CPU GENERATION': cpu_generation,
    #     'CPU FAMILY': cpu_family,
    #     'RAM SIZE': ram_size,
    #     'RAM(DDR) TYPE': ddr_type,
    #     'DISK TYPE': disk_type,
    #     'SSD SIZE': ssd_size,
    #     'HDD SIZE': hdd_size,
    #     'GPU BRAND': gpu_brand,
    #     'GPU TYPE': gpu_type,
    #     'SCREEN SIZE': screen_size,
    #     'SCREEN RESOLUTION': screen_resolution,
    #     'STATE': state
    # }

    options = {
        'BRAND': [brand],
        'CPU BRAND': [cpu_brand],
        'CPU CORE': [cpu_core],
        'CPU GENERATION': [cpu_generation],
        'CPU FAMILY': [cpu_family],
        'RAM SIZE': [ram_size],
        'RAM(DDR) TYPE': [ddr_type],
        'DISK TYPE': [disk_type],
        'SSD SIZE': [ssd_size],
        'HDD SIZE': [hdd_size],
        'GPU BRAND': [gpu_brand],
        'GPU TYPE': [gpu_type],
        'SCREEN SIZE': [screen_size],
        'SCREEN RESOLUTION': [screen_resolution],
        'STATE': [state]
    }

    input_query = pd.DataFrame(data=options)
    result = model.predict(input_query)[0]

    return jsonify(result.round().tolist())


if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.113", port=5111)
