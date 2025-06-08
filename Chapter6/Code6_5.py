import pyfirmata
import time
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
plt.show()
t = []
v = []
board = pyfirmata.Arduino('/dev/ttyACM0')#Arduino orginale
#board = pyfirmata.Arduino('/dev/ttyUSB0')
it = pyfirmata.util.Iterator(board)
it.start()
analog_input = board.get_pin('a:0:i') 
led = board.get_pin('d:7:o')
previous = time.perf_counter()
tempo = 0.
on = 1
off = 1
measure = 0.0

while tempo<4:
    now = time.perf_counter()
    deltat = now - previous
    previous = now
    tempo = tempo + deltat
    time.sleep(0.005)
    measure = analog_input.read()
    t.append(tempo)
    v.append(0 if measure is None else measure*5)
    plt.plot(t,v)
    plt.pause(0.001)
    plt.draw()
    print(tempo,"  ",measure)
    if tempo > 0 and on == 1:
        led.write(1)
        on = 0
    if tempo > 2 and off == 1:
        led.write(0)
        off = 0

times = np.array(t)
volts = np.array(v)
outputFile='RCSeguenza.dat'
np.set_printoptions(precision = 20)
np.savetxt(outputFile, np.column_stack((times, volts)))
