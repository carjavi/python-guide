<p align="center"><img src="./img/python.webp" width="800"  alt=" " /></p>
<h1 align="center"> Python Guide </h1> 
<h4 align="right">March 24</h4>
<img src="https://img.shields.io/badge/OS-Windows%2011-blue">
<img src="https://img.shields.io/badge/OS-Linux%20GNU-yellowgreen">
<img src="https://img.shields.io/badge/OS%20-Raspbian%20GNU%2FLinux%2011%20(bulleye)-yellowgreen">
<img src="https://img.shields.io/badge/Python%20-V3.9.2-orange">

<br>

# Table of contents
- [Table of contents](#table-of-contents)
- [Install on RPi](#install-on-rpi)
  - [Install the required build-tools](#install-the-required-build-tools)
- [Instalando la version mas actualizada desde el sitio oficial](#instalando-la-version-mas-actualizada-desde-el-sitio-oficial)
- [Install on Ubuntu](#install-on-ubuntu)
  - [Install Supporting Software](#install-supporting-software)
- [Upgrade pip](#upgrade-pip)
- [Indentación python](#indentación-python)
  - [vscode](#vscode)
  - [Simple comments (sample)](#simple-comments-sample)
  - [En construcción](#en-construcción)
- [Como forzar la salida en consola en una misma linea](#como-forzar-la-salida-en-consola-en-una-misma-linea)
- [Read Keyboard](#read-keyboard)
- [Read Gamepad](#read-gamepad)
- [python-guide](#python-guide)
  
<br>

# Install on RPi
Find the latest Python version available

## Install the required build-tools
```
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 idle3
```

# Instalando la version mas actualizada desde el sitio oficial
more information: https://raspberrytips.com/install-latest-python-raspberry-pi/


# Install on Ubuntu

```
sudo apt update
```

```
sudo apt install python3
```
```
sudo apt install python3.12
```

```
python --version
python3 --version
pip -V
```

## Install Supporting Software
```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```

# Upgrade pip
```
python -m pip install --upgrade pip 
sudo python3 -m pip install --upgrade pip
```

# Indentación python
## vscode
indent a whole block manually: select the whole block, and then click ```Tab```. If you want to indent backward, you do it with ```Shift+Tab```. That's it, and I think that can be useful in several places.

## Simple comments (sample)
```
"""
This Program is for Voice less video Streaming using UDP protocol 
-------
This is a Server
    - Run Client Code first then run Server Code
    - Configure IP and PORT number of your Server
    
Requirements
    - Outside Connection 
    - IP4v needed select unused port number
"""   
```

## En construcción 

manejo de error python: 
https://controlautomaticoeducacion.com/python-desde-cero/manejo-de-errores-en-python/

```
try:
    #Some code
except:
    #Executed if error in the try block
else:
    # execute if no exception
finally:
    #some code .... (always executed)
```

```
salir de python 

desde el terminal
quit()

Ctrl + C debe estar programad para que funcione



def main():
if __name__ == "__main__":
    main()
```


# Como forzar la salida en consola en una misma linea
sample:
```
import time

def print_and_clear():
    for i in range(25):
        print(f"Numero: {i}" , end = "\r")
        time.sleep(0.5)
        
print_and_clear()
```


# Read Keyboard
Install through pypi:
```
pip install inputs
```
```
"""Simple example showing how to get keyboard events."""

from __future__ import print_function

from inputs import get_key


def main():
    """Just print out some event infomation when keys are pressed."""
    while 1:
        events = get_key()
        if events:
            for event in events:
                print(event.ev_type, event.code, event.state)

if __name__ == "__main__":
    main()
```

# Read Gamepad
Install through pypi:
```
pip install inputs
```
```
"""Simple example showing how to get gamepad events."""

from __future__ import print_function


from inputs import get_gamepad


def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)


if __name__ == "__main__":
    main()
```


joystick python
```
joystick.py 

while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)

event.ev_type --> Absolute o Sync
event.code --> ABS_HAT0Y

if event.code == 'BTN_SOUTH' and event.state == 1:
  print('Celebrate!')

* botones
Key BTN_SOUTH


Absolute ABS_RZ
Absolute ABS_HAT0Y

*palanca analoguica izquierda
palanca analogica abajo derecha

```
```

import inputs

while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
        if event.code == 'BTN_SOUTH' and event.state == 1:
            print('Boton X')
```

https://learn.robotical.io/activity/control-your-marty-with-a-gamepad-using-python-

<br>

---
Copyright &copy; 2022 [carjavi](https://github.com/carjavi). <br>
```www.instintodigital.net``` <br>
carjavi@hotmail.com <br>
<p align="center">
    <a href="https://instintodigital.net/" target="_blank"><img src="./img/developer.png" height="100" alt="www.instintodigital.net"></a>
</p>

# python-guide

