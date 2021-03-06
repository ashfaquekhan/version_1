import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import os
import sys
import RPi.GPIO as  GPIO
import shutil

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # SELECT_BUTTON-PIN-31

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # UP_ARROW_BUTTON-PIN-13

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DOWN_ARROW_BUTTON-PIN-29

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # BACK_BUTTON-PIN-15

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # ENTER_BUTTON-PIN-18

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DELETE_BUTTON-PIN-16

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
heading = "DATA TRANSFER"
note = "PRESS ANY KEY"
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

def copydir(src, dst):
    dis = "SENDING.."
    led.draw_text2(0, 0, dis, 1)
    led.display()
    if os.path.isfile(src) == True:
        shutil.copy(src, dst)

    elif os.path.isdir(src) == True:
        ssrc = os.listdir(src)
        h = 0
        for names in ssrc:
            if os.path.isdir(ssrc[h]) == True:
                path_ssrc = str(src) + "/" + str(ssrc[int(h)])
                shutil.copytree(path_ssrc, dst)
                h = h + 1
            else:
                path_ssrc_f = str(src) + "/" + str(ssrc[int(h)])
                copydir(path_ssrc_f, dst)
                h = h + 1

led.clear_display()
path = ('/media/pi')
files = os.listdir(path)
siz1 = len(files)
siz2 = siz1 -1
nu = 0
titl = "SELECT RECIVER"
#led.draw_text2(0, 0, titl, 1)

if siz1 == 0:
    led.clear_display()
    te = "NO PENDRIVE FOUND"
    led.draw_text2(13, 15, te, 1)
    led.display()
    time.sleep(2)
    os.system('python main_menu.py')

if siz1 == 1:
    texn = "CONNECT THE"
    texm = "2nd PENDRIVE"
    led.draw_text2(0, 10, texn, 1)
    led.draw_text2(0, 19, texm, 1)
    led.display()
    time.sleep(2)
    os.system('python main_menu.py')

while True:
    scrol = GPIO.input(21)
    enter = GPIO.input(24)
    d_scrol = GPIO.input(5)
    back = GPIO.input(22)
    select = GPIO.input(6)
    d='d'
    u='u'
    if scrol == False:
        nu = menu_pos(nu,d,siz2)
        led.clear_display()
        led.draw_text2(0, 0, titl, 1)
        led.draw_text2(0, 15, files[nu], 1)
        led.display()
        time.sleep(0.2)

    elif d_scrol == False:
        nu = menu_pos(nu,u,siz2)
        led.clear_display()
        led.draw_text2(0, 0, titl, 1)
        led.draw_text2(0, 15, files[nu], 1)
        led.display()
        time.sleep(0.2)

    elif enter == False:
        src = nu
        time.sleep(0.2)
        break

    elif back == False:
        os.system('python main_menu.py')

led.clear_display()
n_head="SOURCE LOCATION"
n_head2="PRESS ARROW KEY"
led.draw_text2(0, 0, n_head, 1)
led.draw_text2(12, 15, n_head2, 1)
led.display()
un = 0
title = "SELECT SENDER"
#led.draw_text2(0, 0, title, 1)
while True:
    scrol = GPIO.input(21)
    enter = GPIO.input(24)
    d_scrol = GPIO.input(5)
    back = GPIO.input(22)
    select = GPIO.input(6)
    d='d'
    u='u'
    if scrol == False:
        un=menu_pos(un,d,siz2)
        led.clear_display()
        led.draw_text2(0, 0, title, 1)
        led.draw_text2(0, 15, files[un], 1)
        led.display()
        time.sleep(0.2)

    if d_scrol == False:
        un=menu_pos(un,u,siz2)
        led.clear_display()
        led.draw_text2(0, 0, title, 1)
        led.draw_text2(0, 15, files[un], 1)
        led.display()
        time.sleep(0.2)

    elif enter == False:
        des = un
        time.sleep(0.2)
        break

    elif back == False:
        os.system('python main_menu.py')

led.clear_display()
rinpt = des
sinpt = src
spath_name = "/media/pi/" + str((files[int(sinpt)]))
spath = (spath_name)
lst_spath = os.listdir(spath)
siz_spath = len(lst_spath)
siz_spath2 = siz_spath - 1
x = 0

while True:
    scrol = GPIO.input(21)
    enter = GPIO.input(24)
    d_scrol = GPIO.input(5)
    back = GPIO.input(22)
    select = GPIO.input(6)
    d='d'
    u='u'
    if scrol == False:
        x=menu_pos(x,d,siz_spath2)
        led.clear_display()
        led.draw_text2(0, 15, lst_spath[x], 1)
        led.display()
        time.sleep(0.2)

    if d_scrol == False:
        x=menu_pos(x,u,siz_spath2)
        led.clear_display()
        led.draw_text2(0, 15, lst_spath[x], 1)
        led.display()
        time.sleep(0.2)

    elif enter == False:
        nsrc = "/media/pi/" + str((files[int(sinpt)])) + "/" + str((lst_spath[int(x)]))
        ndes = "/media/pi/" + str((files[int(rinpt)]))
        dis1 = "SENT"
        copydir(nsrc, ndes)
        led.draw_text2(0, 24, dis1, 1)
        led.display()
        time.sleep(0.2)
        
    elif back == False:
        os.system('python main_menu.py')
