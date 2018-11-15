#!/usr/bin/python
import smbus
import time
from kontowecker import getKontostand
bus = smbus.SMBus(1)
alterKontostand = ""
while True:
	kontostand = getKontostand()
	if alterKontostand != kontostand:
		print("Alter Kontostand: " + alterKontostand)
		print("Neuer Kontostand: " + kontostand)
		sendi2c = list(kontostand)
		for i in sendi2c:
			bus.write_byte(0x04, ord(str(i)))
		bus.write_byte(0x04, 10);
		alterKontostand = kontostand
	time.sleep(3600)
