from pynput.mouse import Button, Controller
import os
from termcolor import colored
mouse = Controller()
pos = mouse.position
os.system('mode con:cols=17 lines=2')
print (colored("pranked",'red'))
while True:
    mouse.position = (pos)
