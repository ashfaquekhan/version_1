import os
import sys
import RPi.GPIO as  GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) # BACK_BUTTON-gpio-37
back =  GPIO.input(26)
# go_src def_src name operation
if __name__== '__main__':
    name = str(sys.argv[1])+".py"
    print (name)
    go_sr = str(sys.argv[2])
    def_sr = str(sys.argv[3])
    operation = int(sys.argv[4])
    if operation == 0:
        os.system("python showlist.py" +" "+ str(go_sr) +" " +str(def_sr))
    elif operation ==1:
        os.system("python "+ str(name) +" "+ str(go_sr) +" "+ str(def_sr))

elif back == False:
    os.system('python main_menu.py')

