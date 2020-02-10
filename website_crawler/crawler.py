#!/usr/bin/env python

import re
import requests
import urllib.parse

url = "google.com"


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"

# Subdomain crawler
with open("/root/Downloads/subdomains.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)

target_url2 = "http://ipaddress/mutillidae"

# Directory crawler
with open("/root/Downloads/common.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url2 + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)

target_url3 = "http://webAddress.com"
target_links = []


# Spider
def extract_links_from(url):
    response = requests.get(target_url3)

    # Matches the regex with the response from the spider
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)

        if "#" in link:
            link = link.split('#')[0]

        if target_url3 in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
