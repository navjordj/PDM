import requests
import json
import time

import numpy as np

URL = "http://localhost:5001/data"

while True:
    data = {"num": np.random.normal(10, 10)}
    r = requests.post(URL, json.dumps(data))
    print(r.status_code)

    time.sleep(1)