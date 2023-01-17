import socket
import pickle

from gpiozero import PWMLED,LED
import time

FL_pwm = PWMLED(22)
FL_in1 = LED(27)
FL_in2 = LED(17)

FR_pwm = PWMLED(24)
FR_in1 = LED(23)
FR_in2 = LED(18)

BL_pwm = PWMLED(21)
BL_in1 = LED(20)
BL_in2 = LED(16)

BR_pwm = PWMLED(26)
BR_in1 = LED(19)
BR_in2 = LED(13)

BUF_SIZE = 4096
server_addr = ('172.20.10.3',8088)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_addr)

server.listen(5)
print('wait... ...')

client, client_addr = server.accept() 
print('Successful')

count = 0
flag = 0
    
def FL(input1,input2,pwm):
    FL_in1.value = input1
    FL_in2.value = input2
    FL_pwm.value = pwm
    
def FR(input1,input2,pwm):
    FR_in1.value = input1
    FR_in2.value = input2
    FR_pwm.value = pwm
    
def BL(input1,input2,pwm):
    BL_in1.value = input1
    BL_in2.value = input2
    BL_pwm.value = pwm
    
def BR(input1,input2,pwm):
    BR_in1.value = input1
    BR_in2.value = input2
    BR_pwm.value = pwm

while True:
    cmd = pickle.loads(client.recv(BUF_SIZE))
    print(f'read command = {cmd}')
    count += 1
    print(count)
    action = cmd[0]
    brake = cmd[1]
    pwm = 0
    if brake != 'LT':
        if action == 'Forward':
            flag = 0
            print('forward')
            '''8F
            BL(1,0,0.66)
            BR(1,0,0.7)
            FL(1,0,0.6)
            FR(1,0,0.7)
            '''
            BL(1,0,0.66)
            BR(1,0,0.8)
            FL(1,0,0.6)
            FR(1,0,0.7)
            
        elif action == 'Back':
            flag = 0
            print('back')
            '''8F
            BL(0,1,0.45)
            BR(0,1,0.5)
            FL(0,1,0.45)
            FR(0,1,0.5)
            '''
            BL(0,1,0.45)
            BR(0,1,0.55)
            FL(0,1,0.45)
            FR(0,1,0.5)
            
        elif action == 'Left':
            flag = 0
            print('left')
            '''8F
            BL(1,0,0.55)
            BR(0,1,0.4)
            FL(0,1,0.45)
            FR(1,0,0.45)
            '''
            BL(1,0,0.52)
            BR(0,1,0.3)
            FL(0,1,0.4)
            FR(1,0,0.4)
        elif action == 'Right':
            flag = 0
            print('right')
            '''8F
            BL(0,1,0.55)
            BR(1,0,0.43)
            FL(1,0,0.45)
            FR(0,1,0.55)
            '''
            BL(0,1,0.55)
            BR(1,0,0.43)
            FL(1,0,0.45)
            FR(0,1,0.55)
        elif action == 'RF':
            flag = 0
            print('rf')
            '''8F
            BL(0,0,0)
            BR(1,0,0.55)
            FL(1,0,0.5)
            FR(0,0,0)
            '''
            BL(0,0,0)
            BR(1,0,0.55)
            FL(1,0,0.5)
            FR(0,0,0)
        elif action == 'RB':
            flag = 0
            print('rb')
            '''8F
            BL(0,1,0.5)
            BR(0,0,0)
            FL(0,0,0)
            FR(0,1,0.6)
            '''
            BL(0,1,0.5)
            BR(0,0,0)
            FL(0,0,0)
            FR(0,1,0.65)

        elif action == 'LF':
            flag = 0
            print('lf')
            '''8F
            BL(1,0,0.5)
            BR(0,0,0)
            FL(0,0,0)
            FR(1,0,0.53)
            '''
            BL(1,0,0.5)
            BR(0,0,0)
            FL(0,0,0)
            FR(1,0,0.53)
        elif action == 'LB':
            flag = 0
            print('lb')
            '''8F
            BL(0,0,0)
            BR(0,1,0.5)
            FL(0,1,0.5)
            FR(0,0,0)
            '''
            BL(0,0,0)
            BR(0,1,0.5)
            FL(0,1,0.5)
            FR(0,0,0)
        elif action == 'STOP':
            flag = 0
            print('stop')
            BL(1,1,1)
            BR(1,1,1)
            FL(1,1,1)
            FR(1,1,1)
        elif action == 'Quit':
            print('A')
            server.close()
            exit()
        elif action == 'B':
            print('B')
            flag += 1
            if flag%2 == 1:
                '''8F
                BL(1,0,0.3)
                BR(0,1,0.5)
                FL(1,0,0.3)
                FR(0,1,0.3)
                '''
                BL(1,0,0.3)
                BR(0,1,0.5)
                FL(1,0,0.3)
                FR(0,1,0.3)
            else:
                BL(1,1,1)
                BR(1,1,1)
                FL(1,1,1)
                FR(1,1,1)
    else:
        print('Brake')
        BL(0,0,0)
        BR(0,0,0)
        FL(0,0,0)
        FR(0,0,0)

