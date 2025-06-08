import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
b_dir = '/sys/bus/w1/devices/'
dev_folder = glob.glob(b_dir + '28*')[0]
dev_file = dev_folder + '/w1_slave'

def read_t_raw():
    file = open(dev_file, 'r')
    lines = file.readlines()
    file.close()
    return lines

def read_t():
    lines = read_t_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_t_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        t_string = lines[1][equals_pos+2:]
        t_c = float(t_string) / 1000.0
        return t_c

while True:
	data=(read_t())
	print data, 'C'	
	time.sleep(1)
