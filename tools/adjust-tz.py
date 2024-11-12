#!/usr/bin/env python3
from urllib.request import urlopen
from xml.etree import ElementTree
from subprocess import run

with urlopen('https://geoip.ubuntu.com/lookup') as resp:
    doc = resp.read()
tz = ElementTree.fromstring(doc).find('TimeZone').text
cmd = f'echo {tz} | sudo tee /etc/timezone && sudo ln -snf /usr/share/zoneinfo/{tz} /etc/localtime'
print(cmd)
run(cmd, shell=True, check=True)
