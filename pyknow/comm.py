from queue import Queue
import time,threading
#import serial
import random
serialPort = "COM10"  # 串口
baudRate = 9600  # 波特率

recQueue = Queue(maxsize=0)
sendQueue = Queue(maxsize=0)

stopSign = [False]
paras=[False,'COM1',9600]

def start(com='COM1',baudRate= 9600):
    paras[0] = False
    paras[1] = com
    paras[2] = baudRate
    commThread.start()
    
def stop():
    paras[0] = False
    
    
def send(frames):
    for i in frames:
        recQueue.put(i)
def receive():
    frames = b''
    bIfEmpyt = False
    while not bIfEmpyt:
        try:
            temp = recQueue.get(block = False)
        except(Exception):
            bIfEmpyt = True
        else:
            frames = frames + temp
    return frames       
        
def comm():
    ser = serial.Serial(serialPort, baudRate, timeout=0) # 连接串口
    print("serial port opened successfully! 串口=%s ，波特率=%d" % (serialPort, baudRate))
    while not paras[0]:
        #read
        recBytes = set.read()
        if isinstance(recBytes,bytes):
            recQueue.put(recBytes)
            print("received:",recBytes)
        
        # write    
        frames = b''
        bIfEmpyt = False
        while not bIfEmpyt:
            try:
                temp = sendQueue.get(block = False)
            except(Exception):
                bIfEmpyt = True
            else:
                frames = frames + temp    
        if len(frames)>0:
            ser.write(frames)
            print('sent:',frames)
    ser.close()
    print('serial port closed successfully!')
        
commThread=threading.Thread(target=comm)

        
def control():
    ticks = 0
    while not stopSign[0]:
        ticks =  ticks + 1
        if ticks >= 10:
            stop()
        else:
            time.sleep(1)
    print('bye')
        
        
def product():
    while not stopSign[0]:
        t = []
        t.append(b'\x11\x12')
        send(t)
        time.sleep(random.randint(1,100)/300)
    print('producer stop')
def consume():
    while not stopSign[0]:
        frames = receive()
        print('receive=',frames)
        #for i in frames:
        #    for j in i:
        #        print('{:0>2X}'.format(j),end=',')
        #print('\n')
        time.sleep(random.randint(1,100)/100)
        #recQueue.task_done()
    print('consumer stop')
controler =threading.Thread(target=control)
t1=threading.Thread(target=product)
t2=threading.Thread(target=consume)
 
controler.start()
t1.start()
t2.start()
