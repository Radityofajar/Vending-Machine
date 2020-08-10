import serial
import time

print('1 = 1ON / 0 = OFF')

ser = serial.Serial('COM8', 9600)
time.sleep(2)

while 1:
    user_input = input()
    if user_input == '1':
        ser.write(b'1')
        print("LED Nyala")
    elif user_input == '0':
        ser.write(b'0')
        print("LED Mati")

