import time
from machine import Pin, SPI, I2C
from mfrc522 import MFRC522
sole=Pin(26,Pin.OUT)
buzzer=Pin(4, Pin.OUT)
led1=Pin(5, Pin.OUT)
led2=Pin(14, Pin.OUT)
sck=Pin(18, Pin.OUT)
mosi=Pin(23, Pin.OUT)
miso=Pin(19, Pin.OUT)
sda=Pin(21, Pin.OUT)
rst=Pin(22, Pin.OUT)
spi=SPI(2, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1="0x7208ed72"
card2="0xe4cdee81"
card3="0x04cfef81"

while True:
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1:
                    print("Acesso concedido")
                    buzzer.value(0)
                    time.sleep(0.3)
                    buzzer.value(1)
                    time.sleep(1)
                    buzzer.value(0)
                    time.sleep(1)
                    buzzer.value(1)
                    time.sleep(1)
                    buzzer.value(0)
                    led1.value(1)
                    sole.on()
                    time.sleep(3)
                    led1.value(0)
                    sole.off()
                    time.sleep(1)
            elif uid == card2:
                    print("Acesso concedido")
                    buzzer.value(0)
                    time.sleep(0.3)
                    buzzer.value(1)
                    time.sleep(1)
                    buzzer.value(0)
                    led1.value(1)
                    sole.on()
                    time.sleep(3)
                    led1.value(0)
                    sole.off()
                    time.sleep(1)
            elif uid == card3:
                    print("Acesso concedido")
                    buzzer.value(0)
                    time.sleep(0.3)
                    buzzer.value(1)
                    time.sleep(1)
                    buzzer.value(0)
                    led1.value(1)
                    sole.on()
                    time.sleep(3)
                    led1.value(0)
                    sole.off()
                    time.sleep(1)

            else:
                
                    print("Acesso denegado")
                    buzzer.value(0)
                    time.sleep(0.3)
                    buzzer.value(1)
                    led2.value(1)
                    time.sleep(3)
                    led2.value(0)
                    buzzer.value(0)
                    time.sleep(1)


