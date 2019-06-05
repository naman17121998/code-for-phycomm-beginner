from PhySyncFirmata import ArduinoNano, util
import time

board = ArduinoNano('COM9')

#switching off all LEDs and buzzer at start
for i in range(2,10):
    board.digital[i].write(1)
board.digital[12].write(1)

it = util.Iterator(board)
it.start()

#defining switches as input
s1 = board.get_pin('a:2:i')
s2 = board.get_pin('a:3:i')
s3 = board.get_pin('a:4:i')
s4 = board.get_pin('a:5:i')
s5 = board.get_pin('a:6:i')
s6 = board.get_pin('a:7:i')
s7 = board.get_pin('d:11:i')
s8 = board.get_pin('d:10:i')

#defining switches as output
led_1 = board.get_pin('d:9:o')
led_2 = board.get_pin('d:8:o')
led_3 = board.get_pin('d:7:o')
led_4 = board.get_pin('d:6:o')
led_5 = board.get_pin('d:5:o')
led_6 = board.get_pin('d:4:o')
led_7 = board.get_pin('d:3:o')
led_8 = board.get_pin('d:2:o')

arr_sense = [1 for z in range(0,8)]  
arr_count = [1 for a in range(0,8)]


while True:
    
#storing reads from all button
    for j in range(2,8):
        arr_sense[j-2] = board.analog[j].read()
    for k in range(7,9):
        x = board.digital[18-k].read()
        if x == True:
            x = 1
        elif x == False:
            x = 0
        arr_sense[k-1]=x
        
#increasing count and storing in arr_count
    for c in range(0,8):
        out = arr_sense[c]
        if out == 0:
            arr_count[c] = arr_count[c]+1

    for n in range(0,8):
        f = arr_count[n]
        if f%2 == 0:
            board.digital[9-n].write(0)
        else:
            board.digital[9-n].write(1)
    board.pass_time(0.2)
