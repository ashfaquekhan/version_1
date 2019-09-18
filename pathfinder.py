import os
import sys
import RPi.GPIO as  GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # BACK_BUTTON-gpio-13
back =  GPIO.input(27)

# name|go_src|def_src|operation

if __name__== '__main__':
    name = str(sys.argv[1])+".py"
    print (name)
    go_sr = str(sys.argv[2])
    def_sr = str(sys.argv[3])
    os.system("python "+ str(name) +" "+ str(go_sr) +" "+ str(def_sr))

elif back == False:
    os.system('python main_menu.py')

