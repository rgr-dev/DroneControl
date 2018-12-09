#!/usr/bin/python3
from time import gmtime, strftime
import subprocess
import time

f = open('log.txt','w')


def send_command():
	fecha = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	f.write(fecha +" "+ str(subprocess.check_output(["vcgencmd","get_throttled"]).decode()))
	# subprocess.call(["vcgencmd","get_throttled"])

while True:
	send_command()
	time.sleep(60)