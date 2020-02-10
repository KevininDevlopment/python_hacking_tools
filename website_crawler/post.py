#!/usr/bin/env python

import requests

target_url = "https://targetUrl.com"
data_dict = {"username:" "blahblah", "password:" "123", "Login:" "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)