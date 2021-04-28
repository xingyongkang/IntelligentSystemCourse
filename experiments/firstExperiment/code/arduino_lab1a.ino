/*
 * 将模块与UNO控制器正确连接，切勿接错；
 * 程序效果：首先使得前方无障碍物，此时避障传感器为输出接口为高电平，设定LED 为输出接口为低电平灯灭；
 *          将避障模块的红外探头对准障碍物，距离为3 – 30cm厘米以内，此时避障传感器为输出接口为低电平，设定LED 为输出接口为高电平灯亮；
 */
int Led = 13;      //定义LED 接口
int buttonpin = 3; //定义避障传感器接口
int val;           //定义数字变量val
void setup()
{
    pinMode(Led, OUTPUT);      //定义LED 为输出接口
    Serial.begin(9600);       //连接上位机，波特率为9600
    pinMode(buttonpin, INPUT); //定义避障传感器为输入接口
    digitalWrite(Led, LOW);
}
void loop()
{
    val = digitalRead(buttonpin); //将数字接口3的值读取赋给val
    if (val == LOW)               //当避障传感器检测低电平时，有障碍物，LED 亮
    {
        digitalWrite(Led, HIGH);
        delay(1000);              //延迟1s，亮灯时间明显
    }
    else // 避障传感器检测为高电平，无障碍物
    {
        digitalWrite(Led, LOW);
    }
}
