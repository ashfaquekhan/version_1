import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import os
import sys
import RPi.GPIO as  GPIO
import shutil


GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # SELECT_BUTTON-gpio-31

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # UP_ARROW_BUTTON-gpio-11

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DOWN_ARROW_BUTTON-gpio-29

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # BACK_BUTTON-gpio-13

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # ENTER_BUTTON-gpio-18



RESET_PIN = 15  # WiringPi pin 15 is GPIO14.
DC_PIN = 16  # WiringPi pin 16 is GPIO15.

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32,
                               cols=128)  # Change rows & cols values depending on your display dimensions.
led.begin()
led.clear_display()
led.display()
led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)
heading = "VIEW"
note = "PRESS ARROW KEY"
led.draw_text2(0, 0, heading, 1)
led.draw_text2(12, 15, note, 1)
led.display()

def menu_pos(pos,opr,lim):
    x=pos
    if opr =='d':
        x=x+1
    if x>lim and opr == 'd':
        x=0
    if opr == 'u':
        x=x-1
    if opr == 'u' and x<0:
        x=lim
    return x

path = str(sys.argv[1])+"/"+str(sys.argv[2])
files = os.listdir(path)
siz1 = len(files)
siz2 = siz1 -1
nu = 0
titl = "VIEW"

while True:
    scrol = GPIO.input(17)
    d_scrol= GPIO.input(5)
    select = GPIO.input(6)
    back = GPIO.input(27)
    enter = GPIO.input(24)
    d='d'
    u='u'
    if scrol == False:
        nu=menu_pos(nu,d,siz2)
        led.clear_display()
        led.draw_text2(0, 0, titl, 1)
        led.draw_text2(0, 15, files[nu], 1)
        led.display()
        time.sleep(0.2)

    elif d_scrol == False:
        nu=menu_pos(nu,u,siz2)
        led.clear_display()
        led.draw_text2(0, 0, titl, 1)
        led.draw_text2(0, 15, files[nu], 1)
        led.display()
        time.sleep(0.2)

    elif select == False:
        name = "showlist"
        go_src = path
        def_src = str(files[nu])
        os.system("python pathfinder.py " + str(name) +" "+ str(go_src) +" "+ str(def_src))
        break

    elif back == False:
        if str(sys.argv[1]) == "/media/pi" :
            os.system('python view_menu.py')
        else:
            name="showlist"
            go_src=str(sys.argv[1])
            def_src=str(sys.argv[2])
            os.system("python pathfinder.py " + str(name) +" "+ str(go_src) +" "+ str(def_src))


