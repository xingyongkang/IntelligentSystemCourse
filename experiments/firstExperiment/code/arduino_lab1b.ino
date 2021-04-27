/*
 * 将模块与UNO控制器正确连接，切勿接错；
 * 程序效果：首先使得前方无障碍物，此时避障传感器为输出接口为低电平，将“NO”发送给上位机；
 *          将避障模块的红外探头对准障碍物，距离为3 – 30cm厘米以内，将“YES”发送给上位机；
 *          然后接受上位机信号，若为0，则设定LED 为输出接口为低电平灯灭，否则高电平灯亮
 */

int Led = 13;      //定义LED 接口
int buttonpin = 3; //定义避障传感器接口
int val;           //定义避障传感器接口的数字变量val
char chr;           //定义上位机的输入字符信号
void setup()
{
    pinMode(Led, OUTPUT);      //定义LED 为输出接口
    pinMode(buttonpin, INPUT); //定义避障传感器为输出接口
    Serial.begin(9600);       //连接上位机，波特率为9600
}
void loop()
{
    // 接收传感器信号然后发送给上位机
    val = digitalRead(buttonpin); //将数字接口3的值读取赋给val
    
    if (val == LOW)               //当避障传感器检测低电平时，LED 灭
    {
        Serial.print("NO\n");
    }
    else
    {
        Serial.print("YES\n");
    }

    // 接收上位机信号控制小灯开关
    chr = Serial.read();
    if (chr == '0')               //当避障传感器检测低电平时，LED 灭
    {
        digitalWrite(Led, LOW);
    }
    else
    {
        digitalWrite(Led, HIGH);
        delay(1000);              //延迟1s，亮灯时间明显
    }
}
