"""
@name: lab1.py
@Describe: 通过python的串口库与下位机单片机通信
"""

import serial

serialPort = "COM4"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5) # 连接串口
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

demo0 = b"0"  # 将0转换为bytes类型的ASCII码方便发送
demo1 = b"1"  # 同理

while 1:
    str = ser.readline() # 接收下位机上传的
    print(str)
    x = int(input("请输入0 or 1："))
    if(x == 1):
        ser.write(demo1) # 发送字节1
    else:
        ser.write(demo0) # 发送字节0        

ser.close()