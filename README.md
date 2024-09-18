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
- [Install on Windows](#install-on-windows)
  - [Install PIP en Windows](#install-pip-en-windows)
- [Install on Ubuntu](#install-on-ubuntu)
- [Upgrade pip](#upgrade-pip)
- [Indentación python](#indentación-python)
  - [vscode](#vscode)
  - [Summary coomands Python](#summary-coomands-python)
  - [Check environment variables](#check-environment-variables)
  - [Reinstall a package (Para reinstalar completamente un paquete)](#reinstall-a-package-para-reinstalar-completamente-un-paquete)
  - [Para buscar PyPI para un paquete particular:](#para-buscar-pypi-para-un-paquete-particular)
  - [Para ver detalles sobre un paquete instalado:](#para-ver-detalles-sobre-un-paquete-instalado)
  - [Para enumerar todos los paquetes desactualizados:](#para-enumerar-todos-los-paquetes-desactualizados)
  - [Para actualizar un paquete desactualizado:](#para-actualizar-un-paquete-desactualizado)
  - [Para deshacerse completamente de un paquete:](#para-deshacerse-completamente-de-un-paquete)
  - [Update package](#update-package)
  - [remueve package](#remueve-package)
  - [See package version](#see-package-version)
  - [Install a specific version of a package](#install-a-specific-version-of-a-package)
  - [Install a smaller package than the current one](#install-a-smaller-package-than-the-current-one)
  - [Clear the screen after each message is printed.](#clear-the-screen-after-each-message-is-printed)
  - [Simple comments (sample)](#simple-comments-sample)
  - [En construcción](#en-construcción)
- [Como forzar la salida en consola en una misma linea](#como-forzar-la-salida-en-consola-en-una-misma-linea)
- [Read Keyboard](#read-keyboard)
- [Read Gamepad](#read-gamepad)
- [python-guide](#python-guide)
  
<br>

# Install on RPi
Find the latest Python version: https://raspberrytips.com/install-latest-python-raspberry-pi/

``` Option 1 ``` <br>

instala python & pip a la ultima version 
```python
sudo apt update && sudo apt upgrade -y && sudo apt-get install python3-pip && pip install -U pip
```

``` Option 2``` <br>

python
```python
sudo apt update && sudo apt upgrade -y && sudo apt install python3 idle3
```
pip (Python 2.x)-> python / (Python 3.x)-> python3
```python
sudo apt-get install python3-pip -y && sudo python3 -m pip install --upgrade pip
```

```Install the required build-tools```
```python
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```
```python
python --version
python3 -V
pip -V
```

<br>

# Install on Windows
Download the latest version for Windows: https://www.python.org/downloads/

## Install PIP en Windows
Las siguientes instrucciones deberían funcionar en Windows 7, Windows 8.1 y Windows 10:

Descargue el script del instalador get-pip.py (https://pip.pypa.io/en/stable/installation/). Si estás en Python 3.2, necesitarás esta versión de get-pip.py. En caso de tener Python 3.3 o 3.4 usar estas versiones de PiP correspondientemente Python 3.3 get-pip.py o Python 3.4 get-pip.py. De cualquier manera, haga clic derecho en el enlace y seleccione Guardar como y guárdelo en cualquier carpeta del pc, como su carpeta de Descargas.

Abra el símbolo del sistema y navegue hasta el archivo get-pip.py.

Ejecute el siguiente comando: 
```python
python get-pip.py
```

📝 Nota: Ejecutar la terminal (CMD o Powershell) con privilegios de administrador

actualizar PIP en windows: 
```python
python -m pip install -U pip
```
```python
python --version
python3 -V
pip -V
```

<br>

# Install on Ubuntu

```python
sudo apt update
```

```python
sudo apt install python3
```
```python
sudo apt install python3.12
```
Install Supporting Software
```python
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```

```python
python --version
python3 --version
pip -V
```
<br>

# Upgrade pip
```python
python -m pip install --upgrade pip 
sudo python3 -m pip install --upgrade pip
```

<br>

# Indentación python
## vscode
indent a whole block manually: select the whole block, and then click ```Tab```. If you want to indent backward, you do it with ```Shift+Tab```. That's it, and I think that can be useful in several places.

<br>

## Summary coomands Python 

## Check environment variables
```python
python -c "import os; print('PYTHONPATH:', os.environ.get('PYTHONPATH')); print('PATH:', os.environ.get('PATH'))"
```
respuesta en RPi:
```
PYTHONPATH: None
PATH: /home/carjavi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
```

## Reinstall a package (Para reinstalar completamente un paquete)
```python
pip install --force-reinstall package_name
```

## Para buscar PyPI para un paquete particular:
```python
pip search "query"
```

## Para ver detalles sobre un paquete instalado:
```python
pip show nombre-paquete
```

Para enumerar todos los paquetes instalados:
```python
pip list
```

## Para enumerar todos los paquetes desactualizados:
```python
pip list --outdated
```

## Para actualizar un paquete desactualizado:
```python
pip install nombre-paquete --upgrade
```

## Para deshacerse completamente de un paquete:
```python
pip uninstall nombre-paquete
```

## Update package
```python
pip install package_name --upgrade
```

## remueve package
```python
pip3 uninstall package_name
python3 -m pip uninstall package_name
```

## See package version
```python
python -c "import package_name; print(package_name.__version__)"
```

## Install a specific version of a package
```python
pip install package_name==2.1.1
python3 -m pip install package_name==0.16.0
```

## Install a smaller package than the current one
```python
pip3 install package_name<1 # se necesita una libreria menor a 1.0.0
```


## Clear the screen after each message is printed. 
```python
import time
print(i, end='\r')  --> probar
time.sleep(1)
```

## Simple comments (sample)
```python
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

<br>

## En construcción 

manejo de error python: 
https://controlautomaticoeducacion.com/python-desde-cero/manejo-de-errores-en-python/

```python
try:
    #Some code
except:
    #Executed if error in the try block
else:
    # execute if no exception
finally:
    #some code .... (always executed)
```

```python
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
```python
import time

def print_and_clear():
    for i in range(25):
        print(f"Numero: {i}" , end = "\r")
        time.sleep(0.5)
        
print_and_clear()
```


# Read Keyboard
Install through pypi:
```python
pip install inputs
```
```python
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
```python
pip install inputs
```
```python
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
```python
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
```python

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

