import os
import sys
import RPi.GPIO as  GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # SELECT_BUTTON-PIN-31

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # UP_ARROW_BUTTON-PIN-13

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DOWN_ARROW_BUTTON-PIN-29

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # BACK_BUTTON-PIN-15

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # ENTER_BUTTON-PIN-18

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DELETE_BUTTON-PIN-16
back =  GPIO.input(27)

# name|go_src|def_src|operation

if __name__== '__main__':
    name = str(sys.argv[1])+".py"
    go_sr = str(sys.argv[2])
    def_sr = str(sys.argv[3])
    os.system("python "+ str(name) +" "+ str(go_sr) +" "+ str(def_sr))

elif back == False:
    os.system('python main_menu.py')

