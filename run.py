#!/usr/bin/env python3

import subprocess

server = subprocess.Popen(["python3","server.py"])
client = subprocess.Popen(["python3","client.py"])

client.wait()
server.kill()
