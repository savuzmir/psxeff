import serial

timeout = 0
params = {
	'timeout'  : timeout,
    'baudrate' : 19200,
    'bytesize' : serial.EIGHTBITS,
    'parity'   : serial.PARITY_ODD,
    'stopbits' : serial.STOPBITS_ONE,
}

dev = serial.Serial('COM3', **params)


- if I send this, it goes purple indicating it should work:
1 1 + 1 0 1 0
49 49 43 49 48 49 48

If I send codes individually through presentation such as in the description
it seems to work as it should.

For example  if I individually send 11 (pump 1) followed by 5 followed by 3 this will first
change the amount of juice being squirted by pump 1 and followed by a sequence of squirting from 
pump 3

what doesnt work in python (after converting to decimal)
13+30: either as 49 51 43 51 48 or 4951435148
it needs to have spaces in between because otherwise it scrambles the information
1330: 49 51 51 48 
13 30: 49 51 32 51 48

running 
dev2.write(b'\rL1\r') 
changes pump 3 to 7600 
so does setting just L 
 
4L changes pump 3 to 1300
 
maybe check the .dll file from presentation that were installed to see how it communicates, i.e.
what are the relevant commands?
 
 
if i send dev.wirte('\1-4\r\n') this correctly starts my pumps
now i need to figure out how to correctly change amounts on individual pumps 
 
 commands and corresponding values:
 1 to 7 goes from 100-700
 8 and 9 go to 9200
 10 to 17 goes from 800-1500
 18 and 19 go to 100
 20 to 27 goes from 1600-2300
 28 and 29 go to 200
 30 to 37 go goes from 2400-3100
 38 and 39 go to 300
 
 11 goes to 900
 12 goes to 1000
 13 goes to 1100
 14 goes to 1200
 15 goes to 1300
 16 goes to 1400
 17 goes to 1500
 18 goes to 100
 19 goes to 100
 20 goes to 1600
 21 goes to 1700
 22 goes to 1800
 23 goes to 1900
 24 goes to 2000
 25 goes to 2100
 26 goes to 2200
 27 goes to 2300
 28 goes to 200
 29 goes to 200
 30 goes to 2400
 31 goes to 2500
 32 goes to 2600
 33 goes to 2700
 34 goes to 2800
 35 goes to 2900
 36 goes to 3000
 37 goes to 3100
 38 goes to 300
 39 goes to 300
 40 goes to 3200
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 






 