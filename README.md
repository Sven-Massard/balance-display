# balance-display
Parses gmail for emails sent by my bank to get most recent balance and displays it on lcd

The python program is run on my raspberry pi. It sends the balance to an atmega328 microchip over the I2C protocoll.
The microchip then uses an LCD-Display to display the balance.
The atmega328 was first programmed on an arduino uno and then taken out and moved to a breadboard.
